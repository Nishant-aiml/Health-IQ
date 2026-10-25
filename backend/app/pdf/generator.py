# --------------------------------------------------
# File: generator.py
# Purpose: PDF Generator orchestrator computing SHA-256 report hash and building complete PDF.
# Module: PDF Engine
# Used By: PDF Export Service
# Future Phase: Phase 2E, Phase 3B & Phase 3C PDF Export
# --------------------------------------------------

import json
import hashlib
from typing import Dict, Any, Optional
from backend.app.pdf.sections import assemble_all_report_sections
from backend.app.pdf.renderer import render_pdf_to_bytes
from backend.app.core.logging import logger


class ReportPDFGenerator:
    """
    ReportLab Professional Medical PDF Generator.

    Generates hospital-quality, multi-page medical report PDFs containing Cover Summary,
    Health Score, Extracted Parameters Table, Action Recommendations, Doctor Questions, ELI10,
    Disclaimers, optional Longitudinal Health Trends, Nutrition, Lifestyle & Wellness scores, and embedded SHA-256 integrity hash.
    """

    def generate_report_pdf(
        self,
        analysis: Dict[str, Any],
        recommendation_bundle: Dict[str, Any],
        trend_data: Optional[Dict[str, Any]] = None,
        nutrition_data: Optional[Dict[str, Any]] = None,
        lifestyle_data: Optional[Dict[str, Any]] = None,
        wellness_data: Optional[Dict[str, Any]] = None,
    ) -> bytes:
        # Compute SHA-256 Report Integrity Hash
        raw_str = json.dumps(analysis, sort_keys=True, default=str)
        sha256_hash = hashlib.sha256(raw_str.encode("utf-8")).hexdigest()

        # Assemble Story Elements
        story = assemble_all_report_sections(
            analysis,
            recommendation_bundle,
            trend_data=trend_data,
            nutrition_data=nutrition_data,
            lifestyle_data=lifestyle_data,
            wellness_data=wellness_data,
        )

        # Render PDF to Bytes
        pdf_bytes = render_pdf_to_bytes(story, sha256_hash)
        logger.info(f"Report PDF generated for report #{analysis.get('report_id')} ({len(pdf_bytes)} bytes).")
        return pdf_bytes


pdf_generator = ReportPDFGenerator()
