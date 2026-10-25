# --------------------------------------------------
# File: history_service.py
# Purpose: History Service orchestrator for longitudinal health tracking, biomarker trends, and report comparisons.
# Module: History Services
# Used By: History API Controllers
# --------------------------------------------------

from typing import Dict, Any, List, Optional
from datetime import datetime
from sqlmodel import Session, select
from backend.app.models.user import User
from backend.app.models.report import Report
from backend.app.models.historical_report import HistoricalReport
from backend.app.models.historical_parameter import HistoricalParameter
from backend.app.models.timeline_event import TimelineEvent, TimelineEventType
from backend.app.models.trend import TrendSnapshot
from backend.app.history.repository import history_repository
from backend.app.history.alignment.normalizer import alignment_normalizer
from backend.app.history.analytics.statistics import time_series_statistics_engine
from backend.app.history.trends.analyzer import trend_analyzer
from backend.app.history.change.analyzer import change_analyzer
from backend.app.history.change.models import ComparisonMode
from backend.app.history.timeline.builder import timeline_builder
from backend.app.history.summary.generator import longitudinal_summary_generator
from backend.app.history.recommendations.generator import trend_recommendation_generator
from backend.app.repositories.user_repository import user_repository
from backend.app.core.exceptions import NotFoundException
from backend.app.core.logging import logger


class HistoryService:
    """Orchestrates longitudinal health intelligence, trends, comparisons, and patient journey timeline."""

    def sync_report_to_history(self, session: Session, report_id: int, analysis_data: Dict[str, Any]) -> HistoricalReport:
        report = session.get(Report, report_id)
        if not report:
            raise NotFoundException(f"Report #{report_id} not found.")

        # Create HistoricalReport record
        hist_report = HistoricalReport(
            report_id=report.id,
            user_id=report.user_id,
            source_filename=report.source_filename or "report.pdf",
            doc_type=report.doc_type,
            collection_date=report.uploaded_at,
            health_score=analysis_data.get("health_score", 100.0),
            total_parameters=len(analysis_data.get("extracted_values", [])),
            abnormal_parameters_count=len(analysis_data.get("abnormal_parameters", [])),
            critical_alerts_count=len(analysis_data.get("critical_alerts", [])),
        )
        session.add(hist_report)
        session.commit()
        session.refresh(hist_report)

        # Create HistoricalParameter records with unit harmonization and canonical alignment
        hist_params = []
        for val in analysis_data.get("extracted_values", []):
            raw_name = val.get("raw_name") or val.get("canonical_name", "Unknown")
            value = float(val.get("value", 0.0))
            unit = str(val.get("unit", ""))

            aligned = alignment_normalizer.align_parameter(raw_name, value, unit)

            hp = HistoricalParameter(
                report_id=report.id,
                user_id=report.user_id,
                canonical_name=aligned.canonical_name,
                raw_name=raw_name,
                value=aligned.value,
                unit=aligned.unit,
                lab_name="Standard Clinical Lab",
                reference_range_low=val.get("normal_range_low"),
                reference_range_high=val.get("normal_range_high"),
                range_version="v1.0",
                severity=val.get("severity", "NORMAL"),
                collection_date=report.uploaded_at,
            )
            hist_params.append(hp)

        history_repository.add_historical_parameters(session, hist_params)

        # Add Timeline Event
        ev = TimelineEvent(
            user_id=report.user_id,
            report_id=report.id,
            event_type=TimelineEventType.UPLOAD,
            title=f"Lab Report Uploaded ({report.source_filename})",
            description=f"Recorded {len(hist_params)} biomarkers with Health Score {hist_report.health_score}/100.",
            event_date=report.uploaded_at,
            severity_level="INFO",
            icon_hint="file-text",
        )
        history_repository.add_timeline_event(session, ev)

        logger.info(f"Report #{report_id} synced to historical database with {len(hist_params)} parameters.")
        return hist_report

    def get_patient_history(self, session: Session, user_id: int) -> Dict[str, Any]:
        reports = history_repository.get_user_historical_reports(session, user_id)
        canonical_names = history_repository.get_all_user_canonical_names(session, user_id)
        
        trend_data = {}
        for c_name in canonical_names:
            readings = history_repository.get_user_parameter_readings(session, user_id, c_name)
            if readings:
                trend_data[c_name] = [
                    {
                        "parameter_name": r.canonical_name,
                        "value": r.value,
                        "unit": r.unit,
                        "recorded_at": r.collection_date.isoformat() if hasattr(r.collection_date, 'isoformat') else str(r.collection_date),
                        "status": r.severity
                    }
                    for r in readings
                ]

        summary_info = longitudinal_summary_generator.generate_summary(
            report_count=len(reports),
            initial_score=reports[0].health_score if reports else 100.0,
            latest_score=reports[-1].health_score if reports else 100.0,
            trend_results=[trend_analyzer.analyze_series(c, history_repository.get_user_parameter_readings(session, user_id, c)) for c in canonical_names] if canonical_names else [],
        )

        return {
            "user_id": user_id,
            "total_reports": len(reports),
            "reports": [r.model_dump() for r in reports],
            "trend_data": trend_data,
            "insights": summary_info.get("highlights", []) if isinstance(summary_info, dict) else [],
            "summary": summary_info,
        }

    def get_patient_timeline(self, session: Session, user_id: int) -> Dict[str, Any]:
        events = history_repository.get_user_timeline_events(session, user_id)
        timeline = timeline_builder.build_timeline(user_id, events)
        return timeline.model_dump()


history_service = HistoryService()
