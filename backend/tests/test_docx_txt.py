# --------------------------------------------------
# File: test_docx_txt.py
# Purpose: Unit tests for .txt, .docx, and copy-pasted text extraction provider.
# Module: Backend Test Suite / OCR Engine
# Used By: Pytest Execution
# Future Phase: Phase 2A Validation
# --------------------------------------------------

import asyncio
import io
import zipfile
from backend.app.ocr.providers import text_docx_provider


def test_txt_and_pasted_text_extraction():
    raw_text = "Hemoglobin 11.5 g/dL\nFasting Blood Sugar 110 mg/dL"
    text_bytes = raw_text.encode("utf-8")

    result = asyncio.run(text_docx_provider.extract(text_bytes, "pasted_report.txt"))

    assert result.success is True
    assert "Hemoglobin 11.5" in result.extracted_text
    assert result.provider_used == "TextDocxProvider"


def test_docx_text_extraction():
    xml_content = b"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
        <w:body>
            <w:p><w:r><w:t>Total Cholesterol 220 mg/dL</w:t></w:r></w:p>
        </w:body>
    </w:document>
    """
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w") as z:
        z.writestr("word/document.xml", xml_content)

    docx_bytes = buffer.getvalue()
    result = asyncio.run(text_docx_provider.extract(docx_bytes, "report.docx"))

    assert result.success is True
    assert "Total Cholesterol 220" in result.extracted_text
