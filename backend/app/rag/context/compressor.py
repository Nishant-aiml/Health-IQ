# --------------------------------------------------
# File: compressor.py
# Purpose: Deduplicates and compresses top context before prompt construction.
# Module: RAG Engine / Context
# Used By: Context Builder
# Future Phase: Phase 2D Hybrid RAG
# --------------------------------------------------

from typing import List
from backend.app.rag.models import DocumentChunk


class ContextCompressor:
    """
    Context Compressor.

    Why it exists:
        Removes duplicate text passages across retrieved chunks to keep system prompt concise.
    """

    def compress_chunks(self, chunks: List[DocumentChunk]) -> List[DocumentChunk]:
        seen_texts = set()
        compressed: List[DocumentChunk] = []

        for c in chunks:
            text_snippet = c.text[:80].lower()
            if text_snippet not in seen_texts:
                seen_texts.add(text_snippet)
                compressed.append(c)

        return compressed


context_compressor = ContextCompressor()
