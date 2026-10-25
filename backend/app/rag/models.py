# --------------------------------------------------
# File: models.py
# Purpose: Shared domain models for RAG documents, chunks, and retrieval results.
# Module: RAG Engine
# Used By: Corpus Loader, Hybrid Retriever, Context Builder, Chat Engine
# Future Phase: Phase 2D Hybrid RAG
# --------------------------------------------------

from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field


class CorpusDocument(BaseModel):
    """
    Represents a medical guideline document loaded into the knowledge corpus.
    """

    doc_id: str
    title: str
    source: str = Field(..., description="WHO, CDC, NIH, ICMR")
    publication: str
    medical_topic: str
    content: str
    metadata: Dict[str, Any] = Field(default_factory=dict)


class DocumentChunk(BaseModel):
    """
    Represents a discrete text chunk indexed for vector & keyword retrieval.
    """

    chunk_id: str
    doc_id: str
    title: str
    source: str
    medical_topic: str
    text: str
    chunk_index: int
    score: float = Field(default=0.0)


class RetrievalResult(BaseModel):
    """
    Consolidated hybrid retrieval result payload.
    """

    query: str
    retrieved_chunks: List[DocumentChunk] = Field(default_factory=list)
    execution_time_ms: float = 0.0
