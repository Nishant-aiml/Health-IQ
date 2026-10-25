# --------------------------------------------------
# File: renderer.py
# Purpose: PDF document renderer orchestrating layout and canvas generation.
# Module: PDF Engine
# Used By: PDF Generator
# Future Phase: Phase 2E PDF Export
# --------------------------------------------------

from io import BytesIO
from typing import List, Any
from backend.app.pdf.layout import create_pdf_doc_template
from backend.app.pdf.components.footer import NumberedCanvas


def render_pdf_to_bytes(story: List[Any], sha256_hash: str) -> bytes:
    """Renders ReportLab story to bytes buffer using NumberedCanvas."""
    buffer = BytesIO()
    doc = create_pdf_doc_template(buffer)

    def canvas_maker(*args, **kwargs):
        kwargs["sha256_hash"] = sha256_hash
        return NumberedCanvas(*args, **kwargs)

    doc.build(story, canvasmaker=canvas_maker)
    buffer.seek(0)
    return buffer.getvalue()
