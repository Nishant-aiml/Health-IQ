# --------------------------------------------------
# File: planner.py
# Purpose: Adaptive Retrieval Planner adjusting Dense vs Sparse weights based on query intent.
# Module: RAG Engine / Retrieval
# Used By: Hybrid Retriever Orchestrator
# Future Phase: Phase 2D Hybrid RAG
# --------------------------------------------------

from typing import Tuple
from backend.app.core.config.rag import rag_settings


class RetrievalPlanner:
    """
    Adaptive Retrieval Planner.

    Why it exists:
        Dynamically adjusts dense (FAISS semantic) vs sparse (BM25 keyword) weights
        based on user query intent.
        - Exact medical term queries (e.g. "HbA1c", "Creatinine") -> Boost Sparse (BM25)
        - Conceptual explanation queries ("How does blood carry oxygen?") -> Boost Dense (FAISS)
    """

    def plan_weights(self, query: str) -> Tuple[float, float]:
        q_lower = query.lower()

        # Keywords indicating exact terminology search
        exact_terms = ["mg/dl", "g/dl", "hba1c", "tsh", "alt", "sgpt", "mcv", "mchc"]
        if any(term in q_lower for term in exact_terms):
            return 0.3, 0.7  # (dense_weight, sparse_weight)

        # Conceptual questions
        if "how" in q_lower or "why" in q_lower or "explain" in q_lower:
            return 0.7, 0.3  # (dense_weight, sparse_weight)

        # Default balanced weights
        return rag_settings.DENSE_WEIGHT, rag_settings.SPARSE_WEIGHT


retrieval_planner = RetrievalPlanner()
