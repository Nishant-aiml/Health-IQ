from typing import Optional
from datetime import datetime, timezone
from sqlmodel import SQLModel, Field


class Report(SQLModel, table=True):
    __tablename__ = "reports"

    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id", index=True)
    doc_type: str = Field(description="lab_report or prescription")
    uploaded_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    source_filename: str
    extraction_method_used: Optional[str] = Field(default=None)
    status: str = Field(default="queued", description="queued, extracting, parsing, completed, failed")
