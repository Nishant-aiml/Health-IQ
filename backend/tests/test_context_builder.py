# --------------------------------------------------
# File: test_context_builder.py
# Purpose: Unit tests for RAG Context Builder, Ranker, and Compressor.
# Module: Backend Test Suite / RAG
# Used By: Pytest Execution
# Future Phase: Phase 2D Validation
# --------------------------------------------------

from backend.app.rag.models import DocumentChunk
from backend.app.rag.context import context_builder


def test_context_building():
    rep_analysis = {
        "report_id": 1,
        "source_filename": "test.pdf",
        "health_score": 85,
        "summary": "Good overall health.",
        "parameters": [{"canonical_name": "Hemoglobin", "value": 14.2, "unit": "g/dL", "severity": "normal"}],
        "detected_patterns": [],
    }
    rec_bundle = {"recommendations": []}
    chunks = [
        DocumentChunk(chunk_id="c1", doc_id="d1", title="WHO Guide", source="WHO", medical_topic="Anemia", text="WHO anemia guidance...", chunk_index=0)
    ]

    context = context_builder.build_full_context(rep_analysis, rec_bundle, chunks)

    assert "PATIENT MEDICAL REPORT CONTEXT" in context
    assert "Hemoglobin" in context
    assert "WHO Guide" in context
