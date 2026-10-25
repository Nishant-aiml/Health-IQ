# --------------------------------------------------
# File: security.py
# Purpose: Security validator for prompt injection and out-of-scope query rejection.
# Module: RAG Engine / Security
# Used By: Grounded Chat Engine
# Future Phase: Phase 2D Hybrid RAG
# --------------------------------------------------

import re
from backend.app.rag.exceptions import PromptInjectionException
from backend.app.core.logging import logger

INJECTION_PATTERNS = [
    r"ignore\s+(previous|above)\s+instructions",
    r"forget\s+(the|your)\s+system\s+prompt",
    r"reveal\s+(the|your)\s+system\s+prompt",
    r"act\s+as\s+a\s+doctor",
    r"roleplay",
    r"system\s+override",
    r"bypass\s+safety",
]


class SecurityFilter:
    """
    Prompt Injection Protection Filter.

    Why it exists:
        Prevents prompt injection attacks, jailbreaks, system prompt leakage, and roleplay attempts.
    """

    def validate_query_safety(self, query: str):
        q_lower = query.lower()

        for pattern in INJECTION_PATTERNS:
            if re.search(pattern, q_lower):
                logger.warning(f"Prompt injection attempt blocked for pattern '{pattern}' in query: '{query}'")
                raise PromptInjectionException("Security Policy: Prompt injection or system bypass attempt rejected.")


security_filter = SecurityFilter()
