# --------------------------------------------------
# File: test_rrf.py
# Purpose: Unit tests for Reciprocal Rank Fusion (RRF) algorithm.
# Module: Backend Test Suite / RAG
# Used By: Pytest Execution
# Future Phase: Phase 2D Validation
# --------------------------------------------------

from backend.app.rag.models import DocumentChunk
from backend.app.rag.retrieval import reciprocal_rank_fusion


def test_reciprocal_rank_fusion():
    c1 = DocumentChunk(chunk_id="c1", doc_id="d1", title="A", source="WHO", medical_topic="T", text="text1", chunk_index=0)
    c2 = DocumentChunk(chunk_id="c2", doc_id="d2", title="B", source="CDC", medical_topic="T", text="text2", chunk_index=0)

    dense_res = [(c1, 0.9), (c2, 0.5)]
    sparse_res = [(c2, 3.5), (c1, 1.2)]

    fused = reciprocal_rank_fusion(dense_res, sparse_res, top_k=2)

    assert len(fused) == 2
    assert fused[0].score > 0
