# --------------------------------------------------
# File: models.py
# Purpose: Export payload domain models.
# Module: Export Engine
# Used By: JSON Export, CSV Export, PDF Export Services
# Future Phase: Phase 2E Export System
# --------------------------------------------------

from typing import Dict, Any
from pydantic import BaseModel, Field


class VersionedJSONExport(BaseModel):
    """
    Versioned JSON export schema.
    """

    schema_version: str = "1.0"
    application_name: str = "HealthLens AI"
    application_version: str = "2.5.0"
    generated_at: str
    report_id: int
    analysis: Dict[str, Any]
    recommendations: Dict[str, Any]
