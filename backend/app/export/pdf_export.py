# --------------------------------------------------
# File: pdf_export.py
# Purpose: PDF Export Service wrapper delegating to ReportPDFGenerator.
# Module: Export Engine
# Used By: Export APIs
# Future Phase: Phase 2E Export System
# --------------------------------------------------

from typing import Dict, Any
from backend.app.pdf.generator import pdf_generator


class PDFExportService:
    """PDF Export Service Wrapper."""

    def generate_pdf_bytes(
        self,
        analysis: Dict[str, Any],
        recommendation_bundle: Dict[str, Any],
    ) -> bytes:
        return pdf_generator.generate_report_pdf(analysis, recommendation_bundle)


pdf_export_service = PDFExportService()
