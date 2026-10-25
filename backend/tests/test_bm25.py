# --------------------------------------------------
# File: test_bm25.py
# Purpose: Unit tests for BM25 sparse keyword retrieval.
# Module: Backend Test Suite / RAG
# Used By: Pytest Execution
# Future Phase: Phase 2D Validation
# --------------------------------------------------

from backend.app.rag.models import DocumentChunk
from backend.app.rag.retrieval import sparse_bm25_retriever


def test_bm25_sparse_retrieval():
    chunks = [
        DocumentChunk(
            chunk_id="c1",
            doc_id="d1",
            title="Renal Guide",
            source="NIH",
            medical_topic="Nephrology",
            text="Serum creatinine elevation indicates reduced renal clearance.",
            chunk_index=0,
        ),
        DocumentChunk(
            chunk_id="c2",
            doc_id="d2",
            title="Lipid Guide",
            source="ICMR",
            medical_topic="Cardiology",
            text="Triglycerides and total cholesterol evaluate lipid health.",
            chunk_index=0,
        ),
    ]

    sparse_bm25_retriever.index(chunks)
    results = sparse_bm25_retriever.retrieve("creatinine renal clearance", top_k=1)

    assert len(results) == 1
    assert results[0][0].chunk_id == "c1"
