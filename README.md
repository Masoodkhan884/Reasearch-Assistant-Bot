# 📚 AI Research Assistant Bot (RAG-Based)

A powerful **multi-document question answering system** that uses **Retrieval-Augmented Generation (RAG)** to analyze and synthesize information from multiple research papers.

Built with **LangChain, Pinecone, Groq, and Streamlit**, this project demonstrates how to create a **research-grade AI assistant** capable of answering complex academic questions.

---

## 🚀 Features

* 🔍 **Multi-Document Retrieval**

  * Loads and processes multiple PDFs from a folder
  * Retrieves relevant chunks across different papers

* 🧠 **Advanced RAG Pipeline**

  * Combines information from multiple sources
  * Performs synthesis, comparison, and reasoning

* 💬 **Chat-Based Interface**

  * Clean and interactive UI using Streamlit
  * Maintains conversation history

* ⚡ **Fast Performance**

  * Cached embeddings and retriever
  * Optimized for low-latency responses

* 📚 **Source Attribution**

  * Displays source documents used in answers

---

## 🏗️ Tech Stack

* **LLM:** Groq (LLaMA / Gemma / other supported models)
* **Embeddings:** HuggingFace (`all-MiniLM-L6-v2`)
* **Vector Database:** Pinecone
* **Framework:** LangChain (modern runnable pipeline)
* **Frontend:** Streamlit

---

## 📁 Project Structure

```
research-bot/
│
├── papers/                  # Research PDFs
│   ├── paper1.pdf
│   ├── paper2.pdf
│   ├── paper3.pdf
│
├── ingest.py               # Load → Chunk → Embed → Store
├── rag.py                  # CLI-based Q&A
├── app.py                  # Streamlit Web App
├── config.py               # Configuration
├── .env                    # API keys
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/research-bot.git
cd research-bot
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Add API Keys

Create a `.env` file:

```
GROQ_API_KEY=your_groq_api_key
PINECONE_API_KEY=your_pinecone_api_key
```

---

### 5️⃣ Add Research Papers

Place 3–5 PDFs inside:

```
/papers/
```

---

## 📥 Data Ingestion

Run:

```bash
python ingest.py
```

This will:

* Load all PDFs
* Split into chunks
* Generate embeddings
* Store them in Pinecone

---

## 🧠 Run RAG System (CLI)

```bash
python rag.py
```

Ask questions like:

* What is Retrieval-Augmented Generation?
* What do all papers agree on?
* Compare methodologies across papers
* What research gaps exist?

---

## 🌐 Run Web App (Streamlit)

```bash
streamlit run app.py
```

Then open in browser:

```
http://localhost:8501
```

---

## 🧪 Example Queries

### 🔹 Basic

* What is RAG?

### 🔹 Synthesis

* What do all papers say about RAG limitations?

### 🔹 Comparison

* Compare different RAG methodologies

### 🔹 Advanced

* What research gaps exist in this field?

---

## ⚠️ Common Issues & Fixes

### ❌ Model Not Found (Groq)

* Check available models in Groq console
* Update model name in `rag.py` or `app.py`

---

### ❌ Pinecone Dimension Error

* Ensure index dimension = **384**
* Matches embedding model output

---

### ❌ LangChain Import Errors

* Use updated modular imports:

  * `langchain_core`
  * `langchain_text_splitters`

---

## 🧠 Key Concepts

* **RAG (Retrieval-Augmented Generation):**
  Combines retrieval with LLM generation for accurate responses

* **Vector Embeddings:**
  Converts text into numerical representations for similarity search

* **Multi-Document Reasoning:**
  Synthesizes knowledge across multiple sources

---

## 🚀 Future Improvements

* 🔥 Source citation with page numbers
* 🔥 Streaming responses
* 🔥 Upload custom PDFs via UI
* 🔥 LangGraph agent for multi-step reasoning
* 🔥 Hybrid search (keyword + semantic)

---

## 👨‍💻 Author

**Masood Khan**
Software Engineering Student | AI Enthusiast

---

## ⭐ If You Like This Project

Give it a ⭐ on GitHub and share it!

---

## 📜 License

This project is for educational purposes.
