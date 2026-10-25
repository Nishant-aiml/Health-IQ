# --------------------------------------------------
# File: rag.py
# Purpose: Configuration settings for Hybrid RAG Retrieval and Grounded Chat.
# Module: Core / Config
# Used By: Hybrid Retriever, Vector Store, Chat Engine
# Future Phase: Phase 2D Hybrid RAG
# --------------------------------------------------

from pydantic import BaseModel


class RAGSettings(BaseModel):
    """
    RAG Retrieval Configuration.

    Why it exists:
        Centralizes parameters for chunk size, BM25 vs FAISS weights, RRF fusion constant,
        and top-K retrieval bounds. Allows easy tuning during testing.
    """

    EMBEDDING_MODEL_NAME: str = "medical-mini-v1"
    VECTOR_DIMENSION: int = 384
    TOP_K_DENSE: int = 5
    TOP_K_SPARSE: int = 5
    TOP_K_FINAL: int = 3
    DENSE_WEIGHT: float = 0.5
    SPARSE_WEIGHT: float = 0.5
    RRF_K_CONSTANT: int = 60
    CHUNK_SIZE: int = 500
    CHUNK_OVERLAP: int = 50
    RETRIEVAL_TIMEOUT_SECONDS: float = 5.0


rag_settings = RAGSettings()
