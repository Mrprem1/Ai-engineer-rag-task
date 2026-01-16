
This project is a simple backend service that allows users to upload PDF
documents and ask questions based on their content.

I built this project to understand how document-based question answering
works using embeddings and vector search.

Flow
- Upload a PDF
- Extract text
- Split text into overlapping chunks
- Convert chunks into embeddings
- Store embeddings in ChromaDB
- Retrieve relevant chunks during query
- Generate answer using a local LLM

Tech Used
- FastAPI
- Sentence Transformers
- ChromaDB
- SQLite
- Ollama (Mistral model)

Running the project
```bash
chmod +x setup.sh
./setup.sh
