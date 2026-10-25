# --------------------------------------------------
# File: sparse.py
# Purpose: Sparse keyword retrieval using BM25 scoring algorithm.
# Module: RAG Engine / Retrieval
# Used By: Hybrid Retriever
# Future Phase: Phase 2D Hybrid RAG
# --------------------------------------------------

import math
from typing import List, Tuple, Dict
from backend.app.rag.models import DocumentChunk


class SparseBM25Retriever:
    """
    BM25 Sparse Keyword Retriever.

    Why it exists:
        Provides high-precision keyword search for exact medical parameter names and diagnostic terms.
    """

    def __init__(self, k1: float = 1.5, b: float = 0.75):
        self.k1 = k1
        self.b = b
        self._chunks: List[DocumentChunk] = []
        self._doc_len: List[int] = []
        self.avg_doc_len: float = 1.0

    def index(self, chunks: List[DocumentChunk]):
        self._chunks = chunks
        self._doc_len = [len(c.text.lower().split()) for c in chunks]
        self.avg_doc_len = sum(self._doc_len) / len(self._doc_len) if self._doc_len else 1.0

    def retrieve(self, query: str, top_k: int = 5) -> List[Tuple[DocumentChunk, float]]:
        if not self._chunks:
            return []

        query_terms = query.lower().split()
        scores: List[Tuple[DocumentChunk, float]] = []

        for idx, chunk in enumerate(self._chunks):
            words = chunk.text.lower().split()
            doc_len = self._doc_len[idx]
            bm25_score = 0.0

            for term in query_terms:
                freq = words.count(term)
                if freq > 0:
                    numerator = freq * (self.k1 + 1)
                    denominator = freq + self.k1 * (1 - self.b + self.b * (doc_len / self.avg_doc_len))
                    bm25_score += (numerator / denominator)

            scores.append((chunk, bm25_score))

        scores.sort(key=lambda x: x[1], reverse=True)
        return scores[:top_k]


sparse_bm25_retriever = SparseBM25Retriever()
