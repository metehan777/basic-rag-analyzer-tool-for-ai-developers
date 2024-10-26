import streamlit as st
import os
from document_processor import process_documents
from vector_store import VectorStore
from visualization import plot_similarity_scores
from utils import chunk_text

# Page configuration
st.set_page_config(
    page_title="RAG Analysis Tool",
    layout="wide"
)

# Initialize session state
if 'vector_store' not in st.session_state:
    st.session_state.vector_store = VectorStore()

def main():
    st.title("RAG Analysis Tool")
    st.subheader("Document Processing and Retrieval")

    # Document upload section
    st.header("1. Upload Documents")
    uploaded_files = st.file_uploader(
        "Upload your text documents",
        type=['txt', 'md', 'pdf'],
        accept_multiple_files=True
    )

    if uploaded_files:
        with st.spinner('Processing documents...'):
            for file in uploaded_files:
                content = file.read().decode()
                chunks = chunk_text(content)
                process_documents(chunks, st.session_state.vector_store)
        st.success(f"Processed {len(uploaded_files)} documents")

    # Query section
    st.header("2. Query Documents")
    query = st.text_input("Enter your query")
    top_k = st.slider("Number of results", min_value=1, max_value=10, value=3)

    if query and st.button("Search"):
        with st.spinner('Searching...'):
            results = st.session_state.vector_store.search(query, top_k)
            
            # Display results
            st.header("3. Results")
            for i, (doc, score) in enumerate(results, 1):
                with st.expander(f"Result {i} (Similarity: {score:.4f})"):
                    st.markdown(doc)
            
            # Visualize similarity scores
            st.header("4. Similarity Score Distribution")
            fig = plot_similarity_scores([score for _, score in results])
            st.plotly_chart(fig)

if __name__ == "__main__":
    main()
