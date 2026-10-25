from typing import Optional
from datetime import datetime, timezone
from sqlmodel import SQLModel, Field


class Job(SQLModel, table=True):
    __tablename__ = "jobs"

    id: Optional[int] = Field(default=None, primary_key=True)
    report_id: int = Field(foreign_key="reports.id", index=True)
    stage: str = Field(default="queued", description="queued, extracting, parsing, analyzed, completed")
    status: str = Field(default="pending", description="pending, in_progress, completed, failed")
    error_reason: Optional[str] = Field(default=None)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
