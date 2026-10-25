# --------------------------------------------------
# File: report_service.py
# Purpose: Service orchestrator for fetching report analysis data and Health Score details.
# Module: Report Services
# Used By: Reports API Endpoint Controller
# Future Phase: Phase 2B Analysis
# --------------------------------------------------

import json
from typing import Dict, Any, List
from sqlmodel import Session, select
from backend.app.models.report import Report
from backend.app.models.extracted_value import ExtractedValue
from backend.app.models.risk_analysis import RiskAnalysis
from backend.app.repositories.report_repository import report_repository
from backend.app.analysis.critical_alerts import evaluate_critical_alerts
from backend.app.analysis.health_score import calculate_health_score
from backend.app.core.exceptions import NotFoundException


class ReportService:
    """
    Report Service Orchestrator.

    Why it exists:
        Retrieves analyzed report entities, parameter severity list, Health Score breakdown,
        critical alert objects, and detected clinical patterns for API and dashboard rendering.
    """

    def get_report_analysis(self, session: Session, report_id: int) -> Dict[str, Any]:
        report = report_repository.get_by_id(session, report_id)
        if not report:
            raise NotFoundException(f"Report #{report_id} not found.")

        # Fetch ExtractedValues
        values_stmt = select(ExtractedValue).where(ExtractedValue.report_id == report_id)
        extracted_values = session.exec(values_stmt).all()

        # Fetch RiskAnalysis
        risk_stmt = select(RiskAnalysis).where(RiskAnalysis.report_id == report_id)
        risk_analysis = session.exec(risk_stmt).first()

        parameters_list = [
            {
                "id": val.id,
                "canonical_name": val.parameter_canonical_name,
                "value": val.raw_value,
                "unit": val.unit,
                "normal_range_low": val.normal_range_low,
                "normal_range_high": val.normal_range_high,
                "severity": val.severity,
                "is_critical": val.is_critical,
            }
            for val in extracted_values
        ]

        critical_alerts = evaluate_critical_alerts([
            {"canonical_name": val.parameter_canonical_name, "value": val.raw_value, "unit": val.unit}
            for val in extracted_values
        ])

        health_score_details = calculate_health_score([
            {
                "canonical_name": val.parameter_canonical_name,
                "severity": val.severity,
                "is_critical": val.is_critical,
            }
            for val in extracted_values
        ])

        detected_patterns = []
        if risk_analysis and risk_analysis.detected_patterns:
            try:
                detected_patterns = json.loads(risk_analysis.detected_patterns)
            except Exception:
                detected_patterns = []

        return {
            "report_id": report.id,
            "source_filename": report.source_filename,
            "status": report.status,
            "extraction_method_used": report.extraction_method_used,
            "created_at": report.uploaded_at.isoformat() if getattr(report, "uploaded_at", None) else None,
            "health_score": risk_analysis.health_score if risk_analysis else health_score_details["score"],
            "health_score_details": health_score_details,
            "summary": risk_analysis.summary_text_en if risk_analysis else health_score_details["summary"],
            "parameters": parameters_list,
            "critical_alerts": critical_alerts,
            "detected_patterns": detected_patterns,
        }


report_service = ReportService()
