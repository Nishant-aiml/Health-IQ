# --------------------------------------------------
# File: test_embeddings.py
# Purpose: Unit tests for vector embedding provider & cache.
# Module: Backend Test Suite / RAG
# Used By: Pytest Execution
# Future Phase: Phase 2D Validation
# --------------------------------------------------

from backend.app.rag.providers import embedding_provider


def test_embedding_generation_and_caching():
    text = "Hemoglobin concentration in blood sample"
    vec1 = embedding_provider.get_embedding(text)
    vec2 = embedding_provider.get_embedding(text)

    assert len(vec1) == 384
    assert vec1 == vec2  # Must be cached & identical
