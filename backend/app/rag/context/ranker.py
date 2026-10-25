# --------------------------------------------------
# File: ranker.py
# Purpose: Context Ranker prioritizing retrieved chunks by clinical relevance.
# Module: RAG Engine / Context
# Used By: Context Builder
# Future Phase: Phase 2D Hybrid RAG
# --------------------------------------------------

from typing import List
from backend.app.rag.models import DocumentChunk


class ContextRanker:
    """
    Context Ranker.

    Why it exists:
        Ranks retrieved chunks by clinical authority (WHO > ICMR > CDC > NIH)
        and score prior to prompt compression.
    """

    AUTHORITY_WEIGHTS = {"WHO": 4, "ICMR": 3, "CDC": 2, "NIH": 1}

    def rank_context_chunks(self, chunks: List[DocumentChunk]) -> List[DocumentChunk]:
        return sorted(
            chunks,
            key=lambda c: (self.AUTHORITY_WEIGHTS.get(c.source, 0), c.score),
            reverse=True,
        )


context_ranker = ContextRanker()
