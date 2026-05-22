from google import genai
from google.genai import types
import chromadb
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

chroma_client = chromadb.Client()
collection = chroma_client.get_or_create_collection(name="documents")

def chunk_text(text, chunk_size=500):
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)
    return chunks

def store_embeddings(filename, text):
    chunks = chunk_text(text)
    for i, chunk in enumerate(chunks):
        result = client.models.embed_content(
            model="gemini-embedding-001",
            contents=chunk
        )
        embedding = result.embeddings[0].values
        collection.add(
            documents=[chunk],
            embeddings=[embedding],
            ids=[f"{filename}_chunk_{i}"]
        )
    return len(chunks)

def search_documents(query, n_results=3):
    result = client.models.embed_content(
       model="gemini-embedding-001",
        contents=query
    )
    query_embedding = result.embeddings[0].values
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )
    return results["documents"][0]