# --------------------------------------------------
# File: report.py
# Purpose: Pydantic schemas for report upload and status responses.
# Module: API Schemas / Report
# Used By: Documents & Reports Endpoint Controllers
# Future Phase: Phase 2A Ingestion
# --------------------------------------------------

from typing import List, Optional
from pydantic import BaseModel


class ReportUploadResponse(BaseModel):
    batch_id: str
    job_ids: List[int]
    message: str


class ReportStatusResponse(BaseModel):
    job_id: Optional[int] = None
    report_id: int
    filename: Optional[str] = None
    status: str
    stage: str
    error_reason: Optional[str] = None
