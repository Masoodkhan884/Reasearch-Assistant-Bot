import os
from config import *

from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone


def load_documents():
    loader = PyPDFDirectoryLoader("./papers")
    documents = loader.load()

    # Add clean metadata
    for doc in documents:
        doc.metadata["source"] = os.path.basename(doc.metadata["source"])

    return documents


def split_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )
    return splitter.split_documents(documents)


def create_embeddings():
    return HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)


def store_in_pinecone(docs, embeddings):
    pc = Pinecone(api_key=PINECONE_API_KEY)

    PineconeVectorStore.from_documents(
        docs,
        embedding=embeddings,
        index_name=INDEX_NAME
    )


if __name__ == "__main__":
    print("📥 Loading documents...")
    documents = load_documents()

    print("✂️ Splitting documents...")
    docs = split_documents(documents)

    print(f"✅ Total chunks: {len(docs)}")

    print("🔢 Creating embeddings...")
    embeddings = create_embeddings()

    print("☁️ Uploading to Pinecone...")
    store_in_pinecone(docs, embeddings)

    print("🎉 Ingestion complete!")