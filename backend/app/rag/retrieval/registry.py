# --------------------------------------------------
# File: registry.py
# Purpose: Retrieval Engine Registry.
# Module: RAG Engine / Retrieval
# Used By: Grounded Chat Service
# Future Phase: Phase 2D Hybrid RAG
# --------------------------------------------------

from backend.app.rag.retrieval.retriever import HybridRetriever, hybrid_retriever

__all__ = ["HybridRetriever", "hybrid_retriever"]
