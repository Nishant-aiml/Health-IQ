from typing import Optional
from datetime import datetime, timezone
from sqlmodel import SQLModel, Field


class Recommendation(SQLModel, table=True):
    __tablename__ = "recommendations"

    id: Optional[int] = Field(default=None, primary_key=True)
    report_id: int = Field(foreign_key="reports.id", index=True, unique=True)
    explanation_json: Optional[str] = Field(default="{}")
    eli10_json: Optional[str] = Field(default="{}")
    diet_plan_json: Optional[str] = Field(default="{}")
    exercise_json: Optional[str] = Field(default="{}")
    evidence_sources: Optional[str] = Field(default="[]")
    limitations_json: Optional[str] = Field(default="[]")
    generated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
