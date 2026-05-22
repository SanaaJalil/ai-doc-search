from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from services.pdf_reader import extract_text
from services.embeddings import store_embeddings
from services.qa import answer_question
from pydantic import BaseModel
import shutil

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Question(BaseModel):
    question: str

@app.get("/")
def home():
    return {"message": "AI Search API Running"}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    # Save file
    file_path = f"uploads/{file.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Extract text
    text = extract_text(file_path)

    # Store embeddings
    chunks = store_embeddings(file.filename, text)

    return {
        "filename": file.filename,
        "characters": len(text),
        "chunks_stored": chunks
    }

@app.post("/ask")
async def ask_question(body: Question):
    answer = answer_question(body.question)
    return {"answer": answer}