# --------------------------------------------------
# File: models.py
# Purpose: Citation reference domain models with rich provenance metadata.
# Module: RAG Engine / Citations
# Used By: Citation Generator & API
# Future Phase: Phase 2D Hybrid RAG
# --------------------------------------------------

from pydantic import BaseModel, Field


class CitationReference(BaseModel):
    """
    Represents an explicit medical citation reference.
    """

    citation_id: str
    source_organization: str = Field(..., description="WHO, CDC, NIH, ICMR, or Report")
    title: str
    medical_topic: str
    excerpt: str
    relevance_score: float
