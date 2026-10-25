# --------------------------------------------------
# File: models.py
# Purpose: PDF Report generation metadata and configuration domain models.
# Module: PDF Engine
# Used By: PDF Generator & Renderer
# Future Phase: Phase 2E PDF Export
# --------------------------------------------------

from typing import Dict, Any, Optional
from pydantic import BaseModel, Field


class PDFMetadata(BaseModel):
    """
    Metadata embedded inside exported PDF documents.
    """

    report_id: int
    sha256_hash: str
    generated_at: str
    application_name: str = "HealthLens AI"
    application_version: str = "2.5.0"
    schema_version: str = "1.0"
