# --------------------------------------------------
# File: ranking.py
# Purpose: Chunk score ranking and sorting utilities.
# Module: RAG Engine / Retrieval
# Used By: Hybrid Retriever
# Future Phase: Phase 2D Hybrid RAG
# --------------------------------------------------

from typing import List
from backend.app.rag.models import DocumentChunk


def rank_and_sort_chunks(chunks: List[DocumentChunk]) -> List[DocumentChunk]:
    """Sorts document chunks by score descending."""
    return sorted(chunks, key=lambda c: c.score, reverse=True)
