# app.py
import streamlit as st
from rag_query import query_rag

st.title("🏠NewsDigest")

query = st.text_input("Ask a question (e.g. 'What’s is the important news related to AI (artifical intelligence)?')")

if st.button("Get Answer") and query:
    with st.spinner("Thinking..."):
        answer, sources = query_rag(query)

        st.markdown("### 🧠 Answer")
        st.markdown(answer)

        st.markdown("---")
        st.markdown("### 🔍 Sources Used")

        for i, src in enumerate(sources):
            title = src["title"]
            url = src["url"]
            published = src["published"]

            if url:
                st.markdown(f"{i+1}. [{title}]({url})  \n📅 *{published}*")
            else:
                st.markdown(f"{i+1}. {title}  \n📅 *{published}*")
