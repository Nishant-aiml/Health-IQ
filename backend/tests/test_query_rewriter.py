# --------------------------------------------------
# File: test_query_rewriter.py
# Purpose: Unit tests for Query Expansion Rewriter.
# Module: Backend Test Suite / RAG
# Used By: Pytest Execution
# Future Phase: Phase 2D Validation
# --------------------------------------------------

from backend.app.rag.query import query_rewriter


def test_query_expansion_rewriting():
    raw = "Why is my sugar level high?"
    rewritten = query_rewriter.rewrite_query(raw)

    assert "fasting blood sugar" in rewritten.lower()
    assert "hyperglycemia" in rewritten.lower()
