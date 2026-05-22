from google import genai
from services.embeddings import search_documents
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def answer_question(question):

    # Step 1 - Find relevant chunks
    relevant_chunks = search_documents(question)

    # Step 2 - Join chunks into context
    context = "\n\n".join(relevant_chunks)

    # Step 3 - Build prompt
    prompt = f"""
    You are a helpful assistant.
    Answer the question based on the context below.
    If the answer is not in the context, say
    "I could not find the answer in the uploaded documents."

    Context:
    {context}

    Question: {question}

    Answer:
    """

    # Step 4 - Send to Gemini
    response = client.models.generate_content(
        model="models/gemini-2.5-flash",
        contents=prompt
    )

    return response.text