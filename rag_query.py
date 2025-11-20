# rag_query.py
import pickle
import faiss
from sentence_transformers import SentenceTransformer
from llama_cpp import Llama
import streamlit as st

@st.cache_resource
def load_llm():
    return Llama(
        model_path="models/mistral-7b-instruct-v0.2.Q4_K_M.gguf",
        n_ctx=2048,
        n_threads=8
    )

@st.cache_resource
def load_embedder():
    return SentenceTransformer("all-MiniLM-L6-v2")

@st.cache_resource
def load_faiss():
    index = faiss.read_index("index/news_index.index")
    with open("index/news_index.pkl", "rb") as f:
        metadata = pickle.load(f)
    return index, metadata


def query_rag(question):
    llm = load_llm()
    embed_model = load_embedder()
    index, metadata = load_faiss()

    # Embed the question
    q_emb = embed_model.encode([question])
    D, I = index.search(q_emb, k=5)

    # Get top chunks
    matched = [metadata[i] for i in I[0]]
    context = "\n".join([m["chunk"] for m in matched])

    prompt = f"Context:\n{context}\n\nQuestion: {question}\nAnswer:"
    out = llm(prompt=prompt, max_tokens=250)
    answer = out["choices"][0]["text"].strip()

    # Sources
    sources = [{
        "title": m["title"],
        "url": m["url"],
        "published": m["published"]
    } for m in matched]

    return answer, sources
