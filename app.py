import streamlit as st

from langchain_pinecone import PineconeVectorStore
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq

from config import *

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(
    page_title="Research Assistant Bot",
    page_icon="📚",
    layout="wide"
)

st.title("📚 AI Research Assistant")
st.markdown("Ask questions from multiple research papers")

# -------------------------
# LOAD SYSTEM (CACHE)
# -------------------------
@st.cache_resource
def load_system():
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)

    vectorstore = PineconeVectorStore(
        index_name=INDEX_NAME,
        embedding=embeddings
    )

    retriever = vectorstore.as_retriever(search_kwargs={"k": 8})

    # ⚠️ Replace with YOUR working Groq model
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0
    )

    prompt = PromptTemplate.from_template("""
You are an expert research assistant.

Use the context from multiple research papers.

Instructions:
- Combine insights from multiple papers
- Highlight agreements and differences
- Cite sources using (source)
- Be clear and structured

Context:
{context}

Question:
{question}

Answer:
""")

    def format_docs(docs):
        return "\n\n".join([doc.page_content for doc in docs])

    chain = (
        {
            "context": retriever | format_docs,
            "question": lambda x: x
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain

chain = load_system()

# -------------------------
# CHAT MEMORY
# -------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# -------------------------
# USER INPUT
# -------------------------
if prompt := st.chat_input("Ask your research question..."):

    # Save user message
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = chain.invoke(prompt)
            st.markdown(response)

    # Save response
    st.session_state.messages.append({"role": "assistant", "content": response})