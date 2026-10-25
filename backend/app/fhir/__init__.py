# --------------------------------------------------
# File: __init__.py
# Purpose: FHIR Engine package index.
# Module: FHIR Engine
# Used By: Services & Application
# Future Phase: Phase 4 Clinical Collaboration & Digital Health Ecosystem
# --------------------------------------------------

from backend.app.fhir.models import FHIRResource, FHIRBundle
from backend.app.fhir.resources import FHIRResourceGenerator, fhir_resource_generator
from backend.app.fhir.mapper import FHIRMapper, fhir_mapper
from backend.app.fhir.registry import FHIRRegistry, fhir_registry

__all__ = [
    "FHIRResource",
    "FHIRBundle",
    "FHIRResourceGenerator",
    "fhir_resource_generator",
    "FHIRMapper",
    "fhir_mapper",
    "FHIRRegistry",
    "fhir_registry",
]
