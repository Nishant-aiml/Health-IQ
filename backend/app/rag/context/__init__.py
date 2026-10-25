# --------------------------------------------------
# File: __init__.py
# Purpose: Context package index.
# Module: RAG Engine / Context
# Used By: Grounded Chat Engine
# Future Phase: Phase 2D
# --------------------------------------------------

from backend.app.rag.context.ranker import ContextRanker, context_ranker
from backend.app.rag.context.compressor import ContextCompressor, context_compressor
from backend.app.rag.context.builder import ContextBuilder, context_builder
from backend.app.rag.context.formatter import format_context_for_prompt

__all__ = [
    "ContextRanker",
    "context_ranker",
    "ContextCompressor",
    "context_compressor",
    "ContextBuilder",
    "context_builder",
    "format_context_for_prompt",
]
