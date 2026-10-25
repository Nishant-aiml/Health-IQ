from typing import Optional
from datetime import datetime, timezone
from sqlmodel import SQLModel, Field


class DoctorQuestion(SQLModel, table=True):
    __tablename__ = "doctor_questions"

    id: Optional[int] = Field(default=None, primary_key=True)
    report_id: int = Field(foreign_key="reports.id", index=True)
    questions_json: str = Field(default="[]")
    generated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
