# --------------------------------------------------
# File: embedding_provider.py
# Purpose: Vector embedding generation provider with in-memory caching.
# Module: RAG Engine / Providers
# Used By: Hybrid Retriever & Vector Store
# Future Phase: Phase 2D Hybrid RAG
# --------------------------------------------------

import math
import hashlib
from typing import List, Dict, Any
from backend.app.core.config.rag import rag_settings


class EmbeddingProvider:
    """
    Medical Vector Embedding Provider.

    Why it exists:
        Generates dense vector representations for text queries and corpus chunks.
        Uses a deterministic feature-hash embedding generator with caching to avoid
        recomputing vectors unnecessarily.
    """

    def __init__(self):
        self.dimension = rag_settings.VECTOR_DIMENSION
        self._cache: Dict[str, List[float]] = {}

    def get_embedding(self, text: str) -> List[float]:
        """Generates or retrieves cached dense embedding vector."""
        cache_key = hashlib.md5(text.encode("utf-8")).hexdigest()
        if cache_key in self._cache:
            return self._cache[cache_key]

        vector = [0.0] * self.dimension
        words = text.lower().split()
        for idx, word in enumerate(words):
            word_hash = int(hashlib.sha256(word.encode("utf-8")).hexdigest(), 16)
            dim_idx = word_hash % self.dimension
            val = ((word_hash >> 8) % 100) / 50.0 - 1.0
            vector[dim_idx] += val

        # L2 normalize
        norm = math.sqrt(sum(x * x for x in vector)) or 1.0
        normalized_vector = [x / norm for x in vector]

        self._cache[cache_key] = normalized_vector
        return normalized_vector


embedding_provider = EmbeddingProvider()
