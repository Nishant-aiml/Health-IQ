# --------------------------------------------------
# File: text_docx_provider.py
# Purpose: OCR/Text Extraction Provider for .txt files, copy-pasted text, and .docx Word documents.
# Module: OCR Engine / Providers
# Used By: TieredOCRPipeline
# Future Phase: Phase 2A Ingestion
# --------------------------------------------------

import time
import io
import zipfile
import xml.etree.ElementTree as ET
from typing import List
from backend.app.ocr.providers.base import BaseOCRProvider
from backend.app.ocr.models import OCRExtractionResult, OCRPage, OCRBlock
from backend.app.core.logging import logger


class TextDocxProvider(BaseOCRProvider):
    """
    Text & DOCX Extraction Provider.

    Why it exists:
        Extracts plain text directly from .txt files, copy-pasted text submissions,
        and Microsoft Word .docx documents (via OOXML zip parsing).
    """

    def __init__(self, timeout_seconds: float = 3.0):
        super().__init__(provider_name="TextDocxProvider", timeout_seconds=timeout_seconds)

    async def extract(self, file_bytes: bytes, filename: str) -> OCRExtractionResult:
        start_time = time.perf_counter()
        fn_lower = filename.lower()

        extracted_text = ""

        # Case 1: Plain Text (.txt) or Copy-Pasted Text Submission
        if fn_lower.endswith(".txt") or not ("." in filename):
            try:
                extracted_text = file_bytes.decode("utf-8")
            except UnicodeDecodeError:
                extracted_text = file_bytes.decode("latin-1", errors="ignore")

        # Case 2: Microsoft Word Document (.docx)
        elif fn_lower.endswith(".docx"):
            try:
                with zipfile.ZipFile(io.BytesIO(file_bytes)) as z:
                    xml_content = z.read("word/document.xml")
                    tree = ET.fromstring(xml_content)
                    paragraphs = []
                    for p in tree.iter("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p"):
                        texts = [
                            node.text
                            for node in p.iter("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t")
                            if node.text
                        ]
                        if texts:
                            paragraphs.append("".join(texts))
                    extracted_text = "\n".join(paragraphs)
            except Exception as exc:
                logger.error(f"DOCX extraction failed: {exc}")
                return OCRExtractionResult(
                    success=False,
                    provider_used=self.provider_name,
                    extracted_text="",
                    error_message=f"Failed to parse DOCX file: {exc}",
                )

        else:
            return OCRExtractionResult(
                success=False,
                provider_used=self.provider_name,
                extracted_text="",
                error_message="Non-TXT/DOCX file provided to TextDocxProvider",
            )

        extracted_text = extracted_text.strip()
        duration = round((time.perf_counter() - start_time) * 1000, 2)

        if not extracted_text:
            return OCRExtractionResult(
                success=False,
                provider_used=self.provider_name,
                extracted_text="",
                error_message="Empty text or docx content",
                execution_time_ms=duration,
            )

        ocr_block = OCRBlock(text=extracted_text, block_type="text", confidence=1.0)
        ocr_page = OCRPage(page_number=1, text_content=extracted_text, blocks=[ocr_block])

        return OCRExtractionResult(
            success=True,
            provider_used=self.provider_name,
            extracted_text=extracted_text,
            pages=[ocr_page],
            raw_blocks=[ocr_block],
            confidence=1.0,
            execution_time_ms=duration,
        )


text_docx_provider = TextDocxProvider()
