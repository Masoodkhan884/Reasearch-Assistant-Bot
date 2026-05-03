from config import *

from langchain_pinecone import PineconeVectorStore
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq


# 1. Embeddings
embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)

# 2. Vector DB
vectorstore = PineconeVectorStore(
    index_name=INDEX_NAME,
    embedding=embeddings
)

retriever = vectorstore.as_retriever(search_kwargs={"k": 8})

# 3. LLM (Groq)
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

# 4. Prompt
prompt = PromptTemplate.from_template("""
You are an expert research assistant.

Use the context from multiple research papers.

Instructions:
- Combine insights from multiple papers
- Highlight agreements and differences
- Cite sources using (source)
- If unsure, say "Not enough information"

Context:
{context}

Question:
{question}

Answer:
""")

# 5. Helper: format retrieved docs
def format_docs(docs):
    return "\n\n".join([doc.page_content for doc in docs])


# 6. Chain (MODERN WAY)
chain = (
    {
        "context": retriever | format_docs,
        "question": lambda x: x
    }
    | prompt
    | llm
    | StrOutputParser()
)


# 7. Run loop
if __name__ == "__main__":
    print("🔍 Research Assistant Ready!")

    while True:
        query = input("\n❓ Ask (or 'exit'): ")

        if query.lower() == "exit":
            break

        response = chain.invoke(query)

        print("\n🧠 Answer:\n", response)