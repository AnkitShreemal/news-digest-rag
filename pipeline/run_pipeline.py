# run_pipeline.py

from ingest_news import fetch_articles
from preprocess_and_chunk import chunk_articles
from embed_chunks import embed_chunks
from store_faiss import store_faiss_index

def run_pipeline():
    print("📥 Step 1: Ingesting news articles...")
    articles = fetch_articles()
    print(f"✅ Fetched {len(articles)} articles.")

    print("🧹 Step 2: Preprocessing and chunking...")
    chunks = chunk_articles(articles)
    print(f"✅ Generated {len(chunks)} chunks.")

    print("🔢 Step 3: Generating embeddings...")
    embedded_chunks = embed_chunks(chunks)
    print("✅ Embeddings created.")

    print("💾 Step 4: Storing in FAISS index...")
    store_faiss_index(embedded_chunks)
    print("✅ Stored {0} vectors in FAISS.".format(len(embedded_chunks)))

if __name__ == "__main__":
    run_pipeline()
