# 🤖 AI Document Search

A full-stack AI-powered document search application that allows users to upload PDF documents and ask questions in natural language, receiving AI-generated answers based on the document content.

## 🚀 Features

- 📁 Upload PDF documents
- 🔍 AI-powered semantic search
- 💬 Natural language question answering
- 🧠 Retrieval-Augmented Generation (RAG)
- ⚡ Fast and responsive UI

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | React |
| Backend | FastAPI (Python) |
| AI Model | Google Gemini |
| Vector Database | ChromaDB |
| Embeddings | Gemini Embedding |
| Version Control | Git + GitHub |

## ⚙️ Installation

### Backend
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install fastapi uvicorn chromadb pypdf python-multipart python-dotenv google-genai
uvicorn main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm start
```

## 🔑 Environment Variables

Create a `.env` file in the `backend/` folder:

### GEMINI_API_KEY=your_gemini_api_key_here

Get your free API key at: https://aistudio.google.com

## 📖 How to Use

1. Start the backend server
2. Start the frontend app
3. Open http://localhost:3000
4. Upload a PDF document
5. Type your question
6. Get AI-generated answers!

## 👩‍💻 Author

**Sanaa Jalil**
- GitHub: @SanaaJalil
