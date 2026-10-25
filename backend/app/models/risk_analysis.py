from typing import Optional
from sqlmodel import SQLModel, Field


class RiskAnalysis(SQLModel, table=True):
    __tablename__ = "risk_analysis"

    id: Optional[int] = Field(default=None, primary_key=True)
    report_id: int = Field(foreign_key="reports.id", index=True, unique=True)
    health_score: int = Field(default=100, description="Health score 0-100")
    detected_patterns: Optional[str] = Field(default="[]", description="JSON serialized array of detected patterns")
    summary_text_en: Optional[str] = Field(default=None)
    summary_text_hi: Optional[str] = Field(default=None)
