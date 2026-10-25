# --------------------------------------------------
# File: models.py
# Purpose: Domain models for Clinical Case Packages, SHA-256 integrity hashing, and lifecycle states.
# Module: Clinical Collaboration Engine / Models
# Used By: Package Builder, Formatter & Service
# Future Phase: Phase 4 Clinical Collaboration & Digital Health Ecosystem
# --------------------------------------------------

import hashlib
import json
from datetime import datetime
from typing import List, Dict, Any, Optional
from enum import Enum
from pydantic import BaseModel, Field


class ClinicalPackageStatus(str, Enum):
    DRAFT = "Draft"
    AI_GENERATED = "AI Generated"
    REVIEWED = "Reviewed"
    SHARED = "Shared"
    ARCHIVED = "Archived"


class AudienceTarget(str, Enum):
    DOCTOR = "Doctor-Friendly"
    PATIENT = "Patient-Friendly"
    FAMILY = "Family-Friendly"

    @classmethod
    def _missing_(cls, value: Any):
        val = str(value).lower()
        if "doc" in val:
            return cls.DOCTOR
        if "pat" in val:
            return cls.PATIENT
        if "fam" in val:
            return cls.FAMILY
        return None


class EvidenceNode(BaseModel):
    source_type: str = Field(..., description="lab_result | trend | recommendation | nutrition | clinical_summary")
    node_id: str
    title: str
    description: str
    connected_to: List[str] = Field(default_factory=list, description="IDs of connected downstream evidence nodes")
    confidence_score: float = 1.0


class ClinicalCasePackage(BaseModel):
    package_id: str
    report_id: int
    user_id: int
    created_at: str = Field(default_factory=lambda: datetime.utcnow().isoformat())
    package_version: str = "1.0.0"
    ai_engine_version: str = "3.4.0"
    status: ClinicalPackageStatus = ClinicalPackageStatus.AI_GENERATED
    audience: AudienceTarget = AudienceTarget.DOCTOR
    
    # Core Reused Summaries (Zero Recomputation)
    doctor_summary: str
    patient_summary: str
    timeline_summary: str
    medication_summary: str
    nutrition_summary: str
    historical_summary: str
    
    questions_for_physician: List[Dict[str, str]] = Field(default_factory=list)
    evidence_graph: List[EvidenceNode] = Field(default_factory=list)
    
    # SHA-256 Traceability Hash
    sha256_integrity_hash: Optional[str] = None

    def compute_sha256(self) -> str:
        payload = {
            "package_id": self.package_id,
            "report_id": self.report_id,
            "doctor_summary": self.doctor_summary,
            "package_version": self.package_version,
            "created_at": self.created_at,
        }
        raw_bytes = json.dumps(payload, sort_keys=True).encode("utf-8")
        return hashlib.sha256(raw_bytes).hexdigest()
