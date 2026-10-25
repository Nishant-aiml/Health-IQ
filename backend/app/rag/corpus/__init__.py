# --------------------------------------------------
# File: __init__.py
# Purpose: Corpus package index.
# Module: RAG Engine / Corpus
# Used By: Hybrid Retriever
# Future Phase: Phase 2D
# --------------------------------------------------

from backend.app.rag.corpus.loader import CorpusLoader, corpus_loader
from backend.app.rag.corpus.document import create_chunks_from_document
from backend.app.rag.corpus.index_builder import get_indexed_chunks

__all__ = [
    "CorpusLoader",
    "corpus_loader",
    "create_chunks_from_document",
    "get_indexed_chunks",
]
