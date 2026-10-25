# --------------------------------------------------
# File: rewriter.py
# Purpose: Query Expansion Rewriter transforming casual user questions into clinical terminology.
# Module: RAG Engine / Query
# Used By: Hybrid Retriever
# Future Phase: Phase 2D Hybrid RAG
# --------------------------------------------------

from typing import Dict, List
from backend.app.rag.query.normalizer import normalize_query_text


QUERY_EXPANSION_DICTIONARY: Dict[str, List[str]] = {
    "sugar": ["Fasting Blood Sugar", "Glucose", "Hyperglycemia", "Glycemic Control"],
    "hb": ["Hemoglobin", "Anemia", "Red Blood Cell", "Oxygen Transport"],
    "blood": ["Complete Blood Count", "Hemoglobin", "WBC", "Platelet"],
    "kidney": ["Serum Creatinine", "Blood Urea Nitrogen", "eGFR", "Renal Stress"],
    "creatinine": ["Serum Creatinine", "Glomerular Filtration", "Renal Clearance"],
    "cholesterol": ["Total Cholesterol", "Triglycerides", "HDL", "LDL", "Lipid Profile"],
    "thyroid": ["Thyroid Stimulating Hormone", "TSH", "Hypothyroidism"],
}


class QueryRewriter:
    """
    Query Expansion Rewriter.

    Why it exists:
        Non-medical users ask questions in casual language ("Why is my sugar high?").
        This rewriter expands casual terms into formal medical vocabulary before retrieval,
        significantly boosting FAISS & BM25 recall accuracy.
    """

    def rewrite_query(self, raw_query: str) -> str:
        norm_q = normalize_query_text(raw_query)
        expanded_terms: List[str] = [norm_q]

        for token in norm_q.split():
            if token in QUERY_EXPANSION_DICTIONARY:
                expanded_terms.extend(QUERY_EXPANSION_DICTIONARY[token])

        # Remove duplicates while preserving order
        unique_terms = []
        for term in expanded_terms:
            if term not in unique_terms:
                unique_terms.append(term)

        return " ".join(unique_terms)


query_rewriter = QueryRewriter()
