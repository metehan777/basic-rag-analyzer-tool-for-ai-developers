import os
from typing import List
from openai import OpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Initialize OpenAI client
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
openai_client = OpenAI(api_key=OPENAI_API_KEY)

def get_embedding(text: str) -> List[float]:
    """Generate embedding for a text using OpenAI's API."""
    response = openai_client.embeddings.create(
        model="text-embedding-ada-002",
        input=text
    )
    return response.data[0].embedding

def process_documents(chunks: List[str], vector_store) -> None:
    """Process document chunks and add them to the vector store."""
    for chunk in chunks:
        embedding = get_embedding(chunk)
        vector_store.add_document(chunk, embedding)
