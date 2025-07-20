from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from llama_cpp import Llama
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.prompts import PromptTemplate
import os

def clean_structured_output(response_text):
    lines = response_text.strip().splitlines()
    cleaned_lines = []

    for line in lines:
        # Skip lines like "🔹 5" or any line that starts with "🔹" followed by just a number
        if line.strip().startswith("🔹") and line.strip()[2:].strip().isdigit():
            continue
        cleaned_lines.append(line.strip())

    return "\n".join(cleaned_lines)


# ✅ Setup
app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

# ✅ Serve static HTML
app.mount("/static", StaticFiles(directory=".", html=True), name="static")

# ✅ Load Embeddings + Vector DB
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectordb = Chroma(persist_directory="db", embedding_function=embedding)

# ✅ Load LLaMA Model (on CPU)
llm = Llama(
    model_path="C:\\Users\\Charlie\\Documents\\private_llm\\llama-2-7b-chat.Q4_K_M.gguf",
    n_ctx=1024,
    n_threads=6,
    n_batch=32,
    verbose=False
)

@app.post("/ask")
async def ask_question(request: Request):
    data = await request.json()
    query = data.get("query", "")
    docs = vectordb.similarity_search(query, k=1)
    context = "\n".join([doc.page_content for doc in docs])

    # prompt = f"""You are a helpful assistant. Use the context below to answer the question.\n\nContext:\n{context}\n\nQuestion:\n{query}\n\nAnswer:"""
    prompt = f"""
    You are a structured AI assistant. Use the context to answer the question in a professional format.

    👉 Use:
    - Headings (🔹 or ###)
    - Bullet points
    - Short sentences

    📘 Example:
    🔹 1. Planning Phase
    - Conduct user research
    - Create UI design

    🔹 2. Implementation
    - Use FastAPI for backend
    - Integrate vector DB

    📚 Context:
    \"\"\"
    {context}
    \"\"\"

    ❓ Question:
    {query}

    ✍️ Structured Answer:
    """

    
    prompt = prompt[:3000]  # Trim to fit within 1024 token window

    try:
        response = llm(prompt, max_tokens=300)
        raw_answer = response['choices'][0]['text']

# ✅ Clean it up
        answer = clean_structured_output(raw_answer).replace("🔹", "<br>🔹")

        print(answer)


    except Exception as e:
        answer = f"❌ Error: {str(e)}"

    return JSONResponse({"answer": answer})

# ✅ Serve index.html when opening root URL
@app.get("/")
async def serve_ui():
    return FileResponse("index.html")
