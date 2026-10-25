# --------------------------------------------------
# File: test_faiss.py
# Purpose: Unit tests for FAISS / vector store dense similarity search.
# Module: Backend Test Suite / RAG
# Used By: Pytest Execution
# Future Phase: Phase 2D Validation
# --------------------------------------------------

from backend.app.rag.models import DocumentChunk
from backend.app.rag.providers import vector_store_provider, embedding_provider


def test_vector_store_dense_search():
    chunks = [
        DocumentChunk(
            chunk_id="c1",
            doc_id="d1",
            title="Anemia Guidelines",
            source="WHO",
            medical_topic="Hematology",
            text="Low hemoglobin indicates iron deficiency anemia in adults.",
            chunk_index=0,
        ),
        DocumentChunk(
            chunk_id="c2",
            doc_id="d2",
            title="Diabetes Guidelines",
            source="CDC",
            medical_topic="Endocrinology",
            text="Fasting blood sugar above 126 mg/dL signals diabetes.",
            chunk_index=0,
        ),
    ]

    vector_store_provider.build_index(chunks)
    query_vec = embedding_provider.get_embedding("What causes low hemoglobin and anemia?")
    results = vector_store_provider.search(query_vec, top_k=1)

    assert len(results) == 1
    assert results[0][0].chunk_id == "c1"
