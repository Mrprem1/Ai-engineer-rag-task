from fastapi import FastAPI, UploadFile, File
import os
import uuid
import datetime

from app.database import connection, cursor
from app.embedding_model import get_embedding
from app.vector_db import save_chunk, search_chunks
from app.helpers import read_pdf, split_into_chunks
from app.llm_local import ask_llm

app = FastAPI()

UPLOAD_FOLDER = "data/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.get("/health")
def health_check():
    return {"status": "running"}


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as f:
        f.write(await file.read())

    text = read_pdf(file_path)
    chunks = split_into_chunks(text)

    cursor.execute(
        "INSERT INTO documents (filename, uploaded_at) VALUES (?, ?)",
        (file.filename, str(datetime.datetime.now()))
    )
    connection.commit()

    for chunk in chunks:
        embedding = get_embedding(chunk)
        chunk_id = str(uuid.uuid4())

        save_chunk(
            chunk_id,
            embedding,
            chunk,
            {"source": file.filename}
        )

    return {"message": "File uploaded and processed"}


@app.post("/query")
def ask_question(question: str):
    query_embedding = get_embedding(question)
    results = search_chunks(query_embedding)

    retrieved_text = " ".join(results["documents"][0])
    answer = ask_llm(retrieved_text, question)

    return {
        "answer": answer,
        "context": retrieved_text
    }
