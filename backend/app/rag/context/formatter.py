# --------------------------------------------------
# File: formatter.py
# Purpose: Formats context strings for prompt insertion.
# Module: RAG Engine / Context
# Used By: Context Builder
# Future Phase: Phase 2D Hybrid RAG
# --------------------------------------------------

def format_context_for_prompt(context_str: str) -> str:
    """Formats context block with clear boundary demarcations."""
    return f"\n<medical_context>\n{context_str}\n</medical_context>\n"
