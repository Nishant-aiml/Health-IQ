from typing import Optional
from sqlmodel import SQLModel, Field


class ExtractedValue(SQLModel, table=True):
    __tablename__ = "extracted_values"

    id: Optional[int] = Field(default=None, primary_key=True)
    report_id: int = Field(foreign_key="reports.id", index=True)
    parameter_canonical_name: str = Field(index=True)
    raw_value: float
    unit: str
    normal_range_low: Optional[float] = Field(default=None)
    normal_range_high: Optional[float] = Field(default=None)
    severity: str = Field(default="normal", description="normal, mild, moderate, severe")
    is_critical: bool = Field(default=False)
