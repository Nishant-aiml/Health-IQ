# --------------------------------------------------
# File: test_citations.py
# Purpose: Unit tests for citation reference generator.
# Module: Backend Test Suite / RAG
# Used By: Pytest Execution
# Future Phase: Phase 2D Validation
# --------------------------------------------------

from backend.app.rag.models import DocumentChunk
from backend.app.rag.citations import citation_generator


def test_citation_generation():
    chunks = [
        DocumentChunk(chunk_id="c1", doc_id="d1", title="WHO Anemia Guide", source="WHO", medical_topic="Hematology", text="Sample excerpt text...", chunk_index=0)
    ]
    params = [
        {"canonical_name": "Hemoglobin", "value": 10.5, "unit": "g/dL", "severity": "moderate"}
    ]

    cites = citation_generator.generate_citations(chunks, params)

    assert len(cites) == 2
    assert cites[0].source_organization == "WHO"
    assert cites[1].source_organization == "Patient Report"
