# --------------------------------------------------
# File: models.py
# Purpose: Domain models for biomarker canonical matching and unit harmonization.
# Module: Biomarker Alignment Engine / Models
# Used By: Alignment Engine
# Future Phase: Phase 3B Longitudinal Health Intelligence
# --------------------------------------------------

from typing import Optional
from pydantic import BaseModel


class AlignedBiomarker(BaseModel):
    """Canonicalized and unit-harmonized biomarker snapshot."""

    raw_name: str
    canonical_name: str
    value: float
    unit: str
    original_value: float
    original_unit: str
    is_harmonized: bool = False
