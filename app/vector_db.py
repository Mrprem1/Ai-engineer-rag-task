import chromadb

client = chromadb.Client()
collection = client.get_or_create_collection("doc_chunks")

def save_chunk(chunk_id, embedding, text, metadata):
    collection.add(
        ids=[chunk_id],
        embeddings=[embedding],
        documents=[text],
        metadatas=[metadata]
    )

def search_chunks(query_embedding, limit=3):
    return collection.query(
        query_embeddings=[query_embedding],
        n_results=limit
    )
