# --------------------------------------------------
# File: tiered_pipeline.py
# Purpose: Tiered OCR & Text Extraction Pipeline Orchestrator with timeout escalation.
# Module: OCR Engine
# Used By: Worker Queue Jobs
# Future Phase: Phase 2A Ingestion Pipeline
# --------------------------------------------------

import asyncio
from typing import List
from backend.app.ocr.providers import (
    BaseOCRProvider,
    TextDocxProvider,
    PyMuPDFProvider,
    DoclingProvider,
    SarvamProvider,
    VisionProvider,
)
from backend.app.ocr.models import OCRExtractionResult
from backend.app.core.logging import logger


class TieredOCRPipeline:
    """
    Tiered OCR & Text Extraction Pipeline Orchestrator.

    Why it exists:
        Ensures robust document text extraction across all formats:
        - Plain Text (.txt) / Copy-Pasted Text -> TextDocxProvider
        - Microsoft Word (.docx) -> TextDocxProvider
        - Born-Digital PDFs -> PyMuPDFProvider
        - Structured Documents -> DoclingProvider
        - Indian Regional / Sarvam Document Intelligence -> SarvamProvider
        - Complex Multimodal Scans -> VisionProvider
    """

    def __init__(self, providers: List[BaseOCRProvider] = None):
        self.providers = providers or [
            TextDocxProvider(),
            PyMuPDFProvider(),
            DoclingProvider(),
            SarvamProvider(),
            VisionProvider(),
        ]

    async def execute(self, file_bytes: bytes, filename: str) -> OCRExtractionResult:
        logger.info(f"Starting Tiered OCR Pipeline for file '{filename}' across {len(self.providers)} providers.")

        for index, provider in enumerate(self.providers, start=1):
            logger.info(f"Attempting Tier {index} Provider: {provider.provider_name} (Timeout: {provider.timeout_seconds}s)")
            try:
                result = await asyncio.wait_for(
                    provider.extract(file_bytes, filename),
                    timeout=provider.timeout_seconds,
                )
                if result.success:
                    logger.info(f"Tier {index} ({provider.provider_name}) SUCCEEDED in {result.execution_time_ms}ms.")
                    return result
                else:
                    logger.warning(f"Tier {index} ({provider.provider_name}) returned un-successful result: {result.error_message}. Escalating...")
            except asyncio.TimeoutError:
                logger.warning(f"Tier {index} ({provider.provider_name}) TIMED OUT after {provider.timeout_seconds}s. Escalating to next provider...")
            except Exception as exc:
                logger.error(f"Tier {index} ({provider.provider_name}) failed with exception: {exc}. Escalating...")

        logger.error(f"All {len(self.providers)} provider tiers exhausted for file '{filename}'.")
        return OCRExtractionResult(
            success=False,
            provider_used="None",
            extracted_text="",
            error_message="All OCR provider tiers failed or timed out",
        )


tiered_ocr_pipeline = TieredOCRPipeline()
