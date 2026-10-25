# --------------------------------------------------
# File: __init__.py
# Purpose: Retrieval package index.
# Module: RAG Engine / Retrieval
# Used By: Grounded Chat Service
# Future Phase: Phase 2D
# --------------------------------------------------

from backend.app.rag.retrieval.dense import DenseRetriever, dense_retriever
from backend.app.rag.retrieval.sparse import SparseBM25Retriever, sparse_bm25_retriever
from backend.app.rag.retrieval.fusion import reciprocal_rank_fusion
from backend.app.rag.retrieval.planner import RetrievalPlanner, retrieval_planner
from backend.app.rag.retrieval.retriever import HybridRetriever, hybrid_retriever

__all__ = [
    "DenseRetriever",
    "dense_retriever",
    "SparseBM25Retriever",
    "sparse_bm25_retriever",
    "reciprocal_rank_fusion",
    "RetrievalPlanner",
    "retrieval_planner",
    "HybridRetriever",
    "hybrid_retriever",
]
