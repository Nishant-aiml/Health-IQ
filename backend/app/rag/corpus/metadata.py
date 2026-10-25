# --------------------------------------------------
# File: metadata.py
# Purpose: Metadata models and tags for medical guideline documents.
# Module: RAG Engine / Corpus
# Used By: Corpus Loader
# Future Phase: Phase 2D Hybrid RAG
# --------------------------------------------------

from typing import Dict, Any


def get_default_corpus_metadata(source: str, topic: str) -> Dict[str, Any]:
    return {
        "authority": source,
        "topic": topic,
        "verified": True,
        "license": "Public Healthcare Guidelines",
    }
