# --------------------------------------------------
# File: models.py
# Purpose: Domain models for Care Team roles and viewer-only permissions.
# Module: Care Team Engine / Models
# Used By: Permissions & Care Service
# Future Phase: Phase 4 Clinical Collaboration & Digital Health Ecosystem
# --------------------------------------------------

from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, Field


class CareTeamRole(str, Enum):
    PRIMARY_DOCTOR = "Primary Doctor"
    SPECIALIST = "Specialist Physician"
    DIETITIAN = "Clinical Dietitian"
    CAREGIVER = "Caregiver"
    FAMILY = "Family Member"


class CareTeamMember(BaseModel):
    member_id: str
    name: str
    role: CareTeamRole
    email: Optional[str] = None
    phone: Optional[str] = None
    is_viewer_only: bool = True
    assigned_report_ids: List[int] = Field(default_factory=list)
