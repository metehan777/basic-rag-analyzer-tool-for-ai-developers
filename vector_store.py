from typing import List, Tuple
import faiss
import numpy as np

class VectorStore:
    def __init__(self, dimension: int = 1536):  # OpenAI ada-002 embedding dimension
        self.dimension = dimension
        self.index = faiss.IndexFlatL2(dimension)
        self.documents = []

    def add_document(self, document: str, embedding: List[float]) -> None:
        """Add a document and its embedding to the store."""
        self.documents.append(document)
        self.index.add(np.array([embedding], dtype=np.float32))

    def search(self, query: str, k: int = 3) -> List[Tuple[str, float]]:
        """Search for similar documents using the query embedding."""
        from document_processor import get_embedding
        
        query_embedding = get_embedding(query)
        distances, indices = self.index.search(
            np.array([query_embedding], dtype=np.float32),
            k
        )
        
        # Convert L2 distances to similarity scores (1 / (1 + distance))
        similarities = 1 / (1 + distances[0])
        
        return [
            (self.documents[idx], float(sim))
            for idx, sim in zip(indices[0], similarities)
            if idx < len(self.documents)
        ]
