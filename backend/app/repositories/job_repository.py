from typing import List, Optional
from datetime import datetime, timezone
from sqlmodel import Session, select
from backend.app.models.job import Job
from backend.app.repositories.base import BaseRepository


class JobRepository(BaseRepository[Job]):
    def __init__(self):
        super().__init__(Job)

    def get_by_report_id(self, session: Session, report_id: int) -> List[Job]:
        statement = select(Job).where(Job.report_id == report_id)
        return session.exec(statement).all()

    def update_stage_and_status(
        self, session: Session, job_id: int, stage: str, status: str, error_reason: Optional[str] = None
    ) -> bool:
        job = self.get_by_id(session, job_id)
        if job:
            job.stage = stage
            job.status = status
            job.error_reason = error_reason
            job.updated_at = datetime.now(timezone.utc)
            session.add(job)
            session.commit()
            session.refresh(job)
            return True
        return False


job_repository = JobRepository()
