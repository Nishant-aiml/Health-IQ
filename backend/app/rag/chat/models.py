# --------------------------------------------------
# File: models.py
# Purpose: Strongly typed Request/Response models for Grounded Chat Engine.
# Module: RAG Engine / Chat
# Used By: Chat Engine & API Endpoint
# --------------------------------------------------

from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field
from backend.app.rag.citations.models import CitationReference


class ChatRequest(BaseModel):
    """Chat query payload."""
    question: str = Field(..., example="What does my cholesterol level mean?")
    conversation_id: Optional[str] = Field(None, example="conv_12345")
    language: Optional[str] = Field("en", example="hi", description="Preferred language code: en, hi, mr, ta, te, kn, gu, pa, bn, ml")


class ChatResponse(BaseModel):
    """Grounded RAG chat response payload."""
    answer: str
    citations: List[CitationReference] = Field(default_factory=list)
    confidence: str = Field("HIGH", example="HIGH")
    retrieved_chunks: List[Dict[str, Any]] = Field(default_factory=list)
    used_patterns: List[str] = Field(default_factory=list)
    used_recommendations: List[str] = Field(default_factory=list)
    conversation_id: str
    language: str = Field("en", example="en")
