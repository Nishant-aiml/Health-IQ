from typing import List
from sqlmodel import Session, select
from backend.app.models.report import Report
from backend.app.repositories.base import BaseRepository


class ReportRepository(BaseRepository[Report]):
    def __init__(self):
        super().__init__(Report)

    def get_all_by_user(self, session: Session, user_id: int) -> List[Report]:
        statement = select(Report).where(Report.user_id == user_id).order_by(Report.uploaded_at.desc())
        return session.exec(statement).all()

    def update_status(self, session: Session, report_id: int, status: str) -> bool:
        report = self.get_by_id(session, report_id)
        if report:
            report.status = status
            session.add(report)
            session.commit()
            session.refresh(report)
            return True
        return False


report_repository = ReportRepository()
