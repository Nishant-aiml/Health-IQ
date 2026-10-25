# --------------------------------------------------
# File: normalizer.py
# Purpose: Normalizes raw user chat queries (whitespace, punctuation, lowercasing).
# Module: RAG Engine / Query
# Used By: Query Rewriter & Hybrid Retriever
# Future Phase: Phase 2D Hybrid RAG
# --------------------------------------------------

import re


def normalize_query_text(raw_query: str) -> str:
    """
    Cleans and normalizes user chat query strings.

    Inputs:
        raw_query: Raw user input text.

    Returns:
        Cleaned normalized query string.
    """
    cleaned = raw_query.strip().lower()
    cleaned = re.sub(r"[^\w\s\-\%]", "", cleaned)
    cleaned = re.sub(r"\s+", " ", cleaned)
    return cleaned
