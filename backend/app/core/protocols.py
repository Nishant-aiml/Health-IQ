# --------------------------------------------------
# File: protocols.py
# Purpose: Core protocol contracts and abstract interfaces for OCR, Analysis, RAG, and LLM Providers.
# Module: Core Infrastructure
# Used By: OCR Pipeline, Ingestion Engine, AI Chat Engines
# Future Phase: Phase 2A, 2B, 2C, 2D
# --------------------------------------------------

from typing import Protocol, List, Dict, Any, Optional, runtime_checkable


@runtime_checkable
class OCRProviderProtocol(Protocol):
    """
    Abstract Protocol for OCR Provider engines.

    Why it exists:
        Decouples the Tiered OCR Pipeline from concrete OCR provider implementations
        (PyMuPDF, Docling, Sarvam Vision, Vision LLM).
    """

    provider_name: str

    async def extract(self, file_bytes: bytes, filename: str) -> Dict[str, Any]:
        ...


@runtime_checkable
class LLMProviderProtocol(Protocol):
    """
    Abstract Protocol for LLM Chat Completion Providers.

    Why it exists:
        Decouples downstream AI features (Phase 2C Recommendations, Phase 2D Grounded Chat)
        from specific LLM backends (Sarvam Chat API, GLM, OpenAI).
    """

    provider_name: str

    async def generate_chat_completion(
        self,
        messages: List[Dict[str, str]],
        temperature: float = 0.2,
        max_tokens: int = 1000,
    ) -> Dict[str, Any]:
        """
        Generates a chat completion response from the underlying LLM provider.

        Inputs:
            messages: List of message objects `[{"role": "user"|"system", "content": "..."}]`.
            temperature: Sampling temperature for output variability.
            max_tokens: Maximum tokens in generated completion.

        Returns:
            Dict containing `content`, `tokens_used`, and `provider_name`.
        """
        ...


@runtime_checkable
class AnalysisEngineProtocol(Protocol):
    """
    Abstract Protocol for Lab Parameter Analysis Engines.
    """

    def parse_and_canonicalize(self, raw_extracted_data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        ...


@runtime_checkable
class RetrieverProtocol(Protocol):
    """
    Abstract Protocol for Hybrid RAG Retrieval Engines.
    """

    async def retrieve(self, query: str, top_k: int = 5) -> List[Dict[str, Any]]:
        ...
