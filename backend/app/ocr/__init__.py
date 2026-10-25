# --------------------------------------------------
# File: __init__.py
# Purpose: OCR package index.
# Module: OCR Engine
# Used By: Worker Queue, Ingestion Service
# Future Phase: Phase 2A
# --------------------------------------------------

from backend.app.ocr.models import OCRExtractionResult, OCRPage, OCRBlock
from backend.app.ocr.tiered_pipeline import TieredOCRPipeline, tiered_ocr_pipeline

__all__ = [
    "OCRExtractionResult",
    "OCRPage",
    "OCRBlock",
    "TieredOCRPipeline",
    "tiered_ocr_pipeline",
]
