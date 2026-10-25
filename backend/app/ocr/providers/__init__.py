# --------------------------------------------------
# File: __init__.py
# Purpose: OCR Providers package index.
# Module: OCR Engine / Providers
# Used By: TieredOCRPipeline
# Future Phase: Phase 2A Ingestion
# --------------------------------------------------

from backend.app.ocr.providers.base import BaseOCRProvider
from backend.app.ocr.providers.pymupdf_provider import PyMuPDFProvider
from backend.app.ocr.providers.docling_provider import DoclingProvider
from backend.app.ocr.providers.sarvam_provider import SarvamProvider
from backend.app.ocr.providers.vision_provider import VisionProvider
from backend.app.ocr.providers.text_docx_provider import TextDocxProvider, text_docx_provider

__all__ = [
    "BaseOCRProvider",
    "PyMuPDFProvider",
    "DoclingProvider",
    "SarvamProvider",
    "VisionProvider",
    "TextDocxProvider",
    "text_docx_provider",
]
