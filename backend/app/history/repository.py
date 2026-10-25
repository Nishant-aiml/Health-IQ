# --------------------------------------------------
# File: repository.py
# Purpose: Historical report database repository managing CRUD operations for historical parameters & reports.
# Module: History Intelligence / Repository
# Used By: History Service & Endpoints
# --------------------------------------------------

from typing import List, Optional
from sqlmodel import Session, select
from backend.app.models.historical_report import HistoricalReport
from backend.app.models.historical_parameter import HistoricalParameter
from backend.app.models.timeline_event import TimelineEvent
from backend.app.history.models import HistoricalParameterReading
from backend.app.history.loader import historical_loader
from backend.app.core.logging import logger


class HistoryRepository:
    """Database interface for longitudinal report parameters and timeline events."""

    def add_historical_report(self, session: Session, report: HistoricalReport) -> HistoricalReport:
        session.add(report)
        session.commit()
        session.refresh(report)
        return report

    def add_historical_parameters(self, session: Session, parameters: List[HistoricalParameter]) -> None:
        for p in parameters:
            session.add(p)
        session.commit()

    def add_timeline_event(self, session: Session, event: TimelineEvent) -> TimelineEvent:
        session.add(event)
        session.commit()
        session.refresh(event)
        return event

    def get_user_historical_reports(self, session: Session, user_id: int) -> List[HistoricalReport]:
        stmt = select(HistoricalReport).where(HistoricalReport.user_id == user_id).order_by(HistoricalReport.collection_date.asc())
        reports = list(session.exec(stmt).all())
        if not reports:
            # Fallback to all reports if single-user mode
            stmt_all = select(HistoricalReport).order_by(HistoricalReport.collection_date.asc())
            reports = list(session.exec(stmt_all).all())
        return reports

    def get_user_parameter_readings(self, session: Session, user_id: int, canonical_name: str) -> List[HistoricalParameterReading]:
        stmt = (
            select(HistoricalParameter)
            .where(HistoricalParameter.canonical_name == canonical_name)
            .order_by(HistoricalParameter.collection_date.asc())
        )
        entities = session.exec(stmt).all()

        readings = [
            HistoricalParameterReading(
                report_id=e.report_id,
                collection_date=e.collection_date,
                raw_name=e.raw_name,
                canonical_name=e.canonical_name,
                value=e.value,
                unit=e.unit,
                lab_name=e.lab_name or "Standard Lab",
                reference_range_low=e.reference_range_low,
                reference_range_high=e.reference_range_high,
                range_version=e.range_version or "v1.0",
                severity=e.severity,
            )
            for e in entities
        ]
        return readings

    def get_all_user_canonical_names(self, session: Session, user_id: int) -> List[str]:
        stmt = select(HistoricalParameter.canonical_name).distinct()
        return list(session.exec(stmt).all())

    def get_user_timeline_events(self, session: Session, user_id: int) -> List[TimelineEvent]:
        stmt = select(TimelineEvent).order_by(TimelineEvent.event_date.asc())
        return list(session.exec(stmt).all())


history_repository = HistoryRepository()
