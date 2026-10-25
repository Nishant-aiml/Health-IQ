# --------------------------------------------------
# File: vector_store_provider.py
# Purpose: FAISS / Cosine similarity vector store index provider.
# Module: RAG Engine / Providers
# Used By: Dense Retriever
# Future Phase: Phase 2D Hybrid RAG
# --------------------------------------------------

import math
from typing import List, Tuple
from backend.app.rag.models import DocumentChunk
from backend.app.rag.providers.embedding_provider import embedding_provider
from backend.app.core.logging import logger


class VectorStoreProvider:
    """
    Vector Store Index Provider (FAISS / Cosine Similarity).

    Why it exists:
        Indexes dense vectors for corpus chunks and provides fast nearest-neighbor similarity search.
    """

    def __init__(self):
        self._chunks: List[DocumentChunk] = []
        self._vectors: List[List[float]] = []

    def build_index(self, chunks: List[DocumentChunk]):
        self._chunks = chunks
        self._vectors = [embedding_provider.get_embedding(c.text) for c in chunks]
        logger.info(f"Vector Store Index built with {len(self._vectors)} vectors.")

    def search(self, query_vector: List[float], top_k: int = 5) -> List[Tuple[DocumentChunk, float]]:
        if not self._vectors:
            return []

        scores: List[Tuple[DocumentChunk, float]] = []
        for chunk, vec in zip(self._chunks, self._vectors):
            # Cosine similarity dot product (since vectors are L2 normalized)
            sim = sum(q * v for q, v in zip(query_vector, vec))
            scores.append((chunk, sim))

        scores.sort(key=lambda x: x[1], reverse=True)
        return scores[:top_k]


vector_store_provider = VectorStoreProvider()
