# --------------------------------------------------
# File: __init__.py
# Purpose: Medicine RAG Corpus package index.
# Module: RAG Engine / Medicine Corpus
# Used By: Hybrid RAG Engine
# Future Phase: Phase 3A Medicine Intelligence
# --------------------------------------------------

from backend.app.rag.medicine_corpus.loader import load_medicine_corpus_documents, DRUG_REFERENCE_DOCUMENTS

__all__ = [
    "load_medicine_corpus_documents",
    "DRUG_REFERENCE_DOCUMENTS",
]
