from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

def embed_chunks(chunks):
    texts = [c["chunk"] for c in chunks]
    embeddings = model.encode(texts, show_progress_bar=True)
    for i, emb in enumerate(embeddings):
        chunks[i]["embedding"] = emb
    return chunks
