# --------------------------------------------------
# File: models.py
# Purpose: Domain schemas for FHIR R4 JSON resources (Patient, Observation, DiagnosticReport, etc.).
# Module: FHIR R4 Engine / Models
# Used By: FHIR Mapper & Resources Builder
# Future Phase: Phase 4 Clinical Collaboration & Digital Health Ecosystem
# --------------------------------------------------

from typing import Dict, Any, List, Optional
from pydantic import BaseModel, Field


class FHIRResource(BaseModel):
    resourceType: str
    id: str
    meta: Dict[str, Any] = Field(default_factory=lambda: {"profile": ["http://hl7.org/fhir/StructureDefinition/domain-resource"]})


class FHIRBundle(BaseModel):
    resourceType: str = "Bundle"
    type: str = "collection"
    entry: List[Dict[str, Any]] = Field(default_factory=list)
