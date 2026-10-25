# --------------------------------------------------
# File: extractor.py
# Purpose: Prescription Extraction Orchestrator delegating to TieredOCRPipeline and PrescriptionParser.
# Module: Prescription OCR & Parsing / Extractor
# Used By: Prescription Service
# Future Phase: Phase 3A Medicine Intelligence
# --------------------------------------------------

from backend.app.ocr.tiered_pipeline import tiered_ocr_pipeline
from backend.app.prescription.models import PrescriptionParseResult
from backend.app.prescription.parser import prescription_parser
from backend.app.core.logging import logger


class PrescriptionExtractor:
    """Orchestrates tiered OCR and prescription medicine parsing."""

    async def extract_prescription(self, file_bytes: bytes, filename: str) -> PrescriptionParseResult:
        logger.info(f"Starting Prescription Extraction for file '{filename}'")
        ocr_result = await tiered_ocr_pipeline.execute(file_bytes, filename)

        if not ocr_result.success or not ocr_result.extracted_text:
            return PrescriptionParseResult(
                success=False,
                source_filename=filename,
                extraction_method=ocr_result.provider_used,
                items=[],
                raw_ocr_text="",
                error_message=ocr_result.error_message or "Failed to extract text from prescription file.",
            )

        items = prescription_parser.parse_text(ocr_result.extracted_text)

        return PrescriptionParseResult(
            success=True,
            source_filename=filename,
            extraction_method=ocr_result.provider_used,
            items=items,
            raw_ocr_text=ocr_result.extracted_text,
        )


prescription_extractor = PrescriptionExtractor()
