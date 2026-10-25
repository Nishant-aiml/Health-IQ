# --------------------------------------------------
# File: dense.py
# Purpose: Dense vector similarity retrieval using FAISS / Vector Store Index.
# Module: RAG Engine / Retrieval
# Used By: Hybrid Retriever
# Future Phase: Phase 2D Hybrid RAG
# --------------------------------------------------

from typing import List, Tuple
from backend.app.rag.models import DocumentChunk
from backend.app.rag.providers.embedding_provider import embedding_provider
from backend.app.rag.providers.vector_store_provider import vector_store_provider


class DenseRetriever:
    """
    Dense Vector Retriever.

    Why it exists:
        Performs semantic vector search over medical corpus chunks using FAISS/Cosine similarity.
    """

    def retrieve(self, query: str, top_k: int = 5) -> List[Tuple[DocumentChunk, float]]:
        query_vec = embedding_provider.get_embedding(query)
        return vector_store_provider.search(query_vec, top_k=top_k)


dense_retriever = DenseRetriever()
