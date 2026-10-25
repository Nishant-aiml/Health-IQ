# --------------------------------------------------
# File: pymupdf_provider.py
# Purpose: Tier 1 OCR Provider using PyMuPDF for digital PDF text extraction.
# Module: OCR Engine / Providers
# Used By: TieredOCRPipeline
# Future Phase: Phase 2A Ingestion
# --------------------------------------------------

import time
import io
from typing import List
from backend.app.ocr.providers.base import BaseOCRProvider
from backend.app.ocr.models import OCRExtractionResult, OCRPage, OCRBlock
from backend.app.core.logging import logger

try:
    import fitz  # PyMuPDF
    PYMUPDF_AVAILABLE = True
except ImportError:
    PYMUPDF_AVAILABLE = False


class PyMuPDFProvider(BaseOCRProvider):
    """
    Tier 1 OCR Provider: Digital PDF Text Extraction.

    Why it exists:
        Born-digital PDFs (exported directly by labs) contain clean embedded text streams.
        PyMuPDF extracts them instantly without needing cloud vision APIs.
    """

    def __init__(self, timeout_seconds: float = 5.0):
        super().__init__(provider_name="PyMuPDF", timeout_seconds=timeout_seconds)

    async def extract(self, file_bytes: bytes, filename: str) -> OCRExtractionResult:
        start_time = time.perf_counter()
        
        # Check if PyMuPDF library is available
        if not PYMUPDF_AVAILABLE:
            logger.warning("PyMuPDF (fitz) not installed. Tier 1 fallback triggered.")
            return OCRExtractionResult(
                success=False,
                provider_used=self.provider_name,
                extracted_text="",
                error_message="PyMuPDF library unavailable",
            )

        if not filename.lower().endswith(".pdf"):
            return OCRExtractionResult(
                success=False,
                provider_used=self.provider_name,
                extracted_text="",
                error_message="Non-PDF document provided to PyMuPDF provider",
            )

        try:
            doc = fitz.open(stream=file_bytes, filetype="pdf")
            extracted_pages: List[OCRPage] = []
            all_blocks: List[OCRBlock] = []
            full_text_list: List[str] = []

            for page_num, page in enumerate(doc):
                text = page.get_text("text")
                full_text_list.append(text)
                
                blocks = page.get_text("blocks")
                page_blocks: List[OCRBlock] = []
                for b in blocks:
                    block_text = b[4].strip()
                    if block_text:
                        ocr_block = OCRBlock(text=block_text, block_type="text", confidence=1.0)
                        page_blocks.append(ocr_block)
                        all_blocks.append(ocr_block)

                extracted_pages.append(OCRPage(page_number=page_num + 1, text_content=text, blocks=page_blocks))

            doc.close()
            combined_text = "\n".join(full_text_list).strip()
            duration = round((time.perf_counter() - start_time) * 1000, 2)

            # Require minimum text threshold to consider digital PDF extraction successful
            if len(combined_text) < 20:
                return OCRExtractionResult(
                    success=False,
                    provider_used=self.provider_name,
                    extracted_text="",
                    error_message="Scanned PDF detected (insufficient embedded text)",
                    execution_time_ms=duration,
                )

            return OCRExtractionResult(
                success=True,
                provider_used=self.provider_name,
                extracted_text=combined_text,
                pages=extracted_pages,
                raw_blocks=all_blocks,
                confidence=1.0,
                execution_time_ms=duration,
            )
        except Exception as e:
            logger.error(f"PyMuPDF Extraction failed: {e}")
            return OCRExtractionResult(
                success=False,
                provider_used=self.provider_name,
                extracted_text="",
                error_message=str(e),
            )
