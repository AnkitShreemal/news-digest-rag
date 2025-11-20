import faiss
import numpy as np
import pickle

def store_faiss_index(chunks, index_path="news_index"):
    dim = len(chunks[0]["embedding"])
    index = faiss.IndexFlatL2(dim)
    vectors = np.array([c["embedding"] for c in chunks])
    index.add(vectors)

    with open(f"{index_path}.pkl", "wb") as f:
        pickle.dump(chunks, f)
    faiss.write_index(index, f"{index_path}.index")
