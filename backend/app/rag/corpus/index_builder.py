# --------------------------------------------------
# File: index_builder.py
# Purpose: Builds and refreshes corpus indices.
# Module: RAG Engine / Corpus
# Used By: Hybrid Retriever
# Future Phase: Phase 2D Hybrid RAG
# --------------------------------------------------

from typing import List
from backend.app.rag.models import DocumentChunk
from backend.app.rag.corpus.loader import corpus_loader


def get_indexed_chunks() -> List[DocumentChunk]:
    """Helper to return all indexed corpus chunks."""
    return corpus_loader.load_all_chunks()
