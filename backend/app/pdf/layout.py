# --------------------------------------------------
# File: layout.py
# Purpose: PDF SimpleDocTemplate layout builder with page margins.
# Module: PDF Engine
# Used By: PDF Renderer
# Future Phase: Phase 2E PDF Export
# --------------------------------------------------

from io import BytesIO
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import letter


def create_pdf_doc_template(buffer: BytesIO) -> SimpleDocTemplate:
    """Configures ReportLab SimpleDocTemplate with standard letter page dimensions."""
    return SimpleDocTemplate(
        buffer,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=36,
        bottomMargin=54,
    )
