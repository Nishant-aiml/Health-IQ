# --------------------------------------------------
# File: __init__.py
# Purpose: Citations package index.
# Module: RAG Engine / Citations
# Used By: Grounded Chat Engine
# Future Phase: Phase 2D
# --------------------------------------------------

from backend.app.rag.citations.models import CitationReference
from backend.app.rag.citations.generator import CitationGenerator, citation_generator

__all__ = [
    "CitationReference",
    "CitationGenerator",
    "citation_generator",
]
