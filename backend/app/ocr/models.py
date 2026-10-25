# --------------------------------------------------
# File: models.py
# Purpose: Domain Pydantic models for OCR extraction data structures.
# Module: OCR Engine
# Used By: All OCR Providers, Tiered Pipeline, Report Parser
# Future Phase: Phase 2A Ingestion Pipeline
# --------------------------------------------------

from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field


class OCRBlock(BaseModel):
    """
    Represents a discrete text line or table row block extracted from a document.
    """

    text: str
    block_type: str = Field(default="text", description="text, table_row, or title")
    confidence: float = Field(default=1.0, description="Confidence score 0.0 to 1.0")
    bounding_box: Optional[List[float]] = Field(default=None, description="[x0, y0, x1, y1]")


class OCRPage(BaseModel):
    """
    Represents a single page within an extracted document.
    """

    page_number: int
    text_content: str
    blocks: List[OCRBlock] = Field(default_factory=list)


class OCRExtractionResult(BaseModel):
    """
    Standardized result payload returned by any OCRProvider implementation.

    Why it exists:
        Provides a unified schema so downstream parsers never depend on
        vendor-specific API response structures.
    """

    success: bool
    provider_used: str
    extracted_text: str
    pages: List[OCRPage] = Field(default_factory=list)
    raw_blocks: List[OCRBlock] = Field(default_factory=list)
    confidence: float = Field(default=1.0)
    error_message: Optional[str] = None
    execution_time_ms: float = Field(default=0.0)
