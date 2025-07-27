  # ZeroLeak-RAGGPT


# 🔒 PrivateGPT-LocalAI: Fully Offline, Secure RAG-based Chatbot for Organizations

🚫 No Cloud | 🚀 100% Offline | 🔐 Zero Data Leaks | 🧠 Powered by Local LLM + RAG

---

## 🌟 What is this?

**PrivateGPT-LocalAI** is a secure, fully offline AI chatbot designed for **organizations** that require **absolute data privacy**. Built with a **Retrieval-Augmented Generation (RAG)** architecture and powered by a **local Large Language Model (LLM)**, it retrieves organization-specific data without connecting to the internet or external APIs.

🚧 🔴**Note:** This is just the beginning. Many features like PDF upload, authentication, document sources (URLs, images, live feeds), and dashboards are **planned but not implemented** due to limited resources. If you believe in the power of open, private AI — feel free to contribute, fork, or support it! 💪

---

## ✅ Features

- 🔐 **100% Offline & Secure** – No cloud, no external API calls
- 🏢 **Private ChatGPT for your organization**
- 📁 **Custom knowledge base** (PDFs, DOCs, TXT, etc.)
- 🧠 **RAG architecture** – Combines LLM + data retriever for accurate answers
- 🧱 **Open-source and lightweight**
- 🖥️ Runs on local machine (no high-end GPU required)
- 🛠️ Easy to deploy and extend

---

## 🚀 Use Cases

- Internal IT helpdesks
- Company HR bots
- Legal or Compliance assistants
- Private researcher chatbot
- Any sensitive-use environment where **data privacy is critical**

---

## 🛠️ How It Works

1. Load your internal documents into the system.(Inthis I have Used Database.txt Document AND you will see the Result.✅)
2. Vectorize and store using a local vector DB (e.g., FAISS).
3. Ask questions via local UI or terminal.
4. The system fetches relevant context and sends it to your local LLM.
5. You get private, accurate answers — **nothing leaves your machine**.

---

# 🔒 PrivateGPT - Offline RAG Chatbot using LLaMA on CPU

> Ask questions about your **PDFs**, **DOCX**, or **Web Links** – securely and offline using a private LLaMA model (GGUF format).

<img src="https://raw.githubusercontent.com/UddavGoshika/ZeroLeak-RAGGPT/refs/heads/main/privateRag.png">
---

## ⚡ Why This Project?

✅ No API keys. No cloud. No data leakage. 100% private.  
✅ LLaMA runs **locally on CPU** using `llama-cpp`  
✅ Supports **RAG (Retrieval-Augmented Generation)**  
✅ Ask anything from PDFs, Word docs, websites  
✅ Comes with **FastAPI + HTML UI**  
✅ Built for enterprises, devs, and students

> 🚧 **Note:** This is just the beginning. Many features like PDF upload, authentication, document sources (URLs, images, live feeds), and dashboards are **planned but not implemented** due to limited resources. If you believe in the power of open, private AI — feel free to contribute, fork, or support it! 💪

---

## 🧠 Tech Stack

- [x] 🔗 **LangChain** for RAG logic
- [x] 🧠 **LLaMA-2 GGUF** via `llama-cpp-python`
- [x] 📚 ChromaDB for vector storage
- [x] 📝 HuggingFace Embeddings (MiniLM-L6-v2)
- [x] 🌐 FastAPI for backend
- [x] 💬 HTML/CSS/JS UI (dark mode)

---



## 📂 Project Structure

```
privategpt/
├── docs/             # Your documents (PDF/DOCX/TXT)
├── db/               # Vector DB from RAG
├── llama_model/      # GGUF model here
├── frontend/index.html
├── rag_loader_all.py # Loads + indexes your docs
├── rag_backend_api.py # Backend with LLaMA inference
└── ask.py            # CLI script (optional)
```

---

## 🛠 Setup Instructions

### 1. Clone and Setup
```bash
git clone https://github.com/yourusername/privategpt.git
cd privategpt
pip install -r requirements.txt
```

### 2. Put Your Model
Download GGUF file like:
```bash
llama-2-7b-chat.Q4_K_M.gguf → /llama_model/
```

### 3. Index Your Docs
```bash
python rag_loader_all.py
```

### 4. Run the Chat App
```bash
uvicorn rag_backend_api:app --reload
```
Then open 👉 `http://127.0.0.1:8000`

---

## 🤖 Ask Anything Like:
```txt
✅ What are the key proposals in this PDF?
✅ Who is the target audience of this document?
✅ Summarize this doc in 3 bullet points.
```

---

## 🔐 Use Cases
- Enterprises with internal docs
- Students asking their lecture PDFs
- Legal, policy, HR document exploration
- Govt/Defense (confidential, offline)
- NGOs or startups needing offline AI

> 🧠 Want to run AI without depending on cloud services or leaking data? This is your foundation.

---

## 📣 Show Some Love!

If you found this useful:
⭐ Star the repo  
🍴 Fork and customize it  
🚀 Share on LinkedIn with #PrivateGPT

---


## 👋 Author
Made with ❤️ by UddavGoshika(https://linkedin.com/in/GoshikaUddav)


