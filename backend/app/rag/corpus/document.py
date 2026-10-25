# --------------------------------------------------
# File: document.py
# Purpose: Medical corpus document data definitions.
# Module: RAG Engine / Corpus
# Used By: Corpus Loader
# Future Phase: Phase 2D Hybrid RAG
# --------------------------------------------------

from typing import List
from backend.app.rag.models import CorpusDocument, DocumentChunk
from backend.app.core.config.rag import rag_settings


def create_chunks_from_document(doc: CorpusDocument) -> List[DocumentChunk]:
    """
    Splits a medical document into fixed-size text chunks with overlap.

    Inputs:
        doc: CorpusDocument entity.

    Returns:
        List of DocumentChunk instances.
    """
    text = doc.content
    chunk_size = rag_settings.CHUNK_SIZE
    overlap = rag_settings.CHUNK_OVERLAP

    chunks: List[DocumentChunk] = []
    start = 0
    chunk_idx = 0

    while start < len(text):
        end = start + chunk_size
        chunk_text = text[start:end].strip()

        if chunk_text:
            c_id = f"{doc.doc_id}_c{chunk_idx}"
            chunks.append(
                DocumentChunk(
                    chunk_id=c_id,
                    doc_id=doc.doc_id,
                    title=doc.title,
                    source=doc.source,
                    medical_topic=doc.medical_topic,
                    text=chunk_text,
                    chunk_index=chunk_idx,
                )
            )
            chunk_idx += 1

        start += chunk_size - overlap

    return chunks
