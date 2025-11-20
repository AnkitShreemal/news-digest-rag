from langchain.text_splitter import RecursiveCharacterTextSplitter

def chunk_articles(articles):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    all_chunks = []
    for art in articles:
        chunks = splitter.split_text(art['text'])
        for i, chunk in enumerate(chunks):
            all_chunks.append({
                "chunk": chunk,
                "title": art["title"],
                "url": art["url"],
                "published": art["published"]
            })
    return all_chunks
