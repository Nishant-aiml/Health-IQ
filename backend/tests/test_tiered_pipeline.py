# --------------------------------------------------
# File: test_tiered_pipeline.py
# Purpose: Unit tests for Tiered OCR Pipeline escalation and provider fallback.
# Module: Backend Test Suite / OCR Engine
# Used By: Pytest Execution
# Future Phase: Phase 2A Validation
# --------------------------------------------------

import pytest
from backend.app.ocr import TieredOCRPipeline
from backend.app.ocr.providers import PyMuPDFProvider, VisionProvider


@pytest.mark.asyncio
async def test_tiered_pipeline_execution():
    pipeline = TieredOCRPipeline(providers=[PyMuPDFProvider(), VisionProvider()])
    
    # Non-PDF file will cause Tier 1 (PyMuPDF) to fail and escalate to Tier 4 (Vision)
    result = await pipeline.execute(file_bytes=b"sample_image_data", filename="scan.jpg")
    
    assert result.success is True
    assert result.provider_used == "GLM-4.6V Vision LLM"
    assert "Hemoglobin" in result.extracted_text
