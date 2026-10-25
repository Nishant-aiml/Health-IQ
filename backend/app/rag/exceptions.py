# --------------------------------------------------
# File: exceptions.py
# Purpose: RAG-specific exception classes.
# Module: RAG Engine
# Used By: Hybrid Retriever, Security Filter
# Future Phase: Phase 2D Hybrid RAG
# --------------------------------------------------

from backend.app.core.exceptions import AppException


class RAGException(AppException):
    def __init__(self, message: str):
        super().__init__(message=message, status_code=400, error_code="RAG_ERROR")


class PromptInjectionException(AppException):
    def __init__(self, message: str = "Query rejected due to security policy violation."):
        super().__init__(message=message, status_code=422, error_code="PROMPT_INJECTION_DETECTED")
