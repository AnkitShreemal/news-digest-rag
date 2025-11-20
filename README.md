📘 RAG-Based News Digest Application

A lightweight, fast, and fully local Retrieval-Augmented Generation app built with Streamlit, FAISS, GGUF models, and a complete ingestion → preprocessing → embedding → indexing pipeline.

🚀 Overview

This application generates daily news digests using a complete RAG (Retrieval-Augmented Generation) workflow.
It ingests online news, cleans and chunks text, embeds it, stores embeddings in a FAISS vector store, and answers queries using a quantized GGUF LLM running on CPU.

The app is designed to be:

Fast (GGUF quantized models, FAISS search)

Fully local (no API calls)

Cloud deployable (Hugging Face Spaces, AWS EC2, GCP, Azure)

Modular (each pipeline step as a separate script)

Cost-efficient (runs on CPU)





news-digest-rag/
│
├── app.py                     ← Streamlit UI (entrypoint)
├── rag_query.py               ← Will be modified for HF caching + relative paths
│
├── models/                    ← Quantized model + tokenizer
│   ├── mistral-7b-instruct-v0.2.Q4_K_M.gguf
│   ├── tokenizer.model        ← (if needed)
│
├── index/                     ← FAISS index + metadata (generated locally)
│   ├── news_index.index
│   ├── news_index.pkl
│
├── pipeline/                  ← Local-only RAG pipeline steps
│   ├── ingest_news.py
│   ├── preprocess_and_chunk.py
│   ├── embed_chunks.py
│   ├── store_faiss.py
│   └── run_pipeline.py
│
├── requirements.txt           ← HF-friendly deps
├── README.md                  ← Instructions
└── .gitignore


🚀 Overview

This project builds a full News RAG (Retrieval-Augmented Generation) system:

Ingests real news from multiple RSS feeds

Preprocesses and chunks the text

Embeds all chunks using Sentence Transformers

Stores vectors in FAISS for high-speed retrieval

Runs a GGUF quantized LLM locally via llama-cpp-python

Serves results in a clean Streamlit UI

🔄 RAG Pipeline (Local Only)

All pipeline files are inside:

pipeline/

Steps:

Fetch news

ingest_news.py


Clean + chunk articles

preprocess_and_chunk.py


Generate embeddings

embed_chunks.py


Store FAISS index + metadata

store_faiss.py


Run full pipeline

run_pipeline.py


⚠️ This pipeline MUST be run locally. Hugging Face Spaces cannot run it due to time & memory limits.

It generates:

index/news_index.index
index/news_index.pkl


These should be committed to Git so they load instantly on Hugging Face.

🧠 Models Used

Stored in:

models/


Includes:

mistral-7b-instruct-v0.2.Q4_K_M.gguf (quantized for CPU-fast inference)

tokenizer.model (optional depending on the GGUF file)

Inference is handled by:

llama-cpp-python


No GPU is required.

🎛️ Running Locally
1. Install dependencies
pip install -r requirements.txt

2. Build the FAISS index (first-time only)
python pipeline/run_pipeline.py

3. Run the Streamlit application
streamlit run app.py


The app loads:

The GGUF model from /models

The FAISS index from /index

All metadata from /index/news_index.pkl

🌐 Deploying to Hugging Face Spaces

This project is optimized for Spaces (Streamlit runtime).

Steps

Commit the whole folder to GitHub

Create a Hugging Face Space → select Streamlit

Connect repository → Spaces auto-builds and runs

Ensure your requirements.txt contains:

streamlit
llama-cpp-python
faiss-cpu
sentence-transformers
numpy
requests
feedparser
newspaper3k
torch


(Optional extras removed for faster build.)

During inference:

The GGUF model loads from /models

The FAISS index loads from /index

No pipeline scripts run on Spaces

This keeps startup fast and avoids HF RAM/time limits.

📦 What Runs on Hugging Face

✔ app.py
✔ rag_query.py
✔ Model loading (GGUF)
✔ FAISS search
✔ Generation with llama-cpp

❌ News ingestion
❌ Chunking
❌ Embedding
❌ FAISS index creation

Pipeline must run locally and only outputs are pushed to Git.

🧹 .gitignore Essentials

Included so we avoid committing:

news_digest_venv/
__pycache__/
*.pyc
*.DS_Store

🤝 Contributing

Feel free to open issues or PRs for improvements:

More news sources

Better chunking logic

Faster embedding/model options

UI enhancements

📄 License

MIT License