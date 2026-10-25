# --------------------------------------------------
# File: registry.py
# Purpose: Registry wrapper for FHIR R4 Mapping Engine.
# Module: FHIR R4 Engine / Registry
# Used By: Services & Endpoints
# Future Phase: Phase 4 Clinical Collaboration & Digital Health Ecosystem
# --------------------------------------------------

from backend.app.fhir.mapper import fhir_mapper, FHIRMapper
from backend.app.fhir.resources import fhir_resource_generator, FHIRResourceGenerator


class FHIRRegistry:
    def get_mapper(self) -> FHIRMapper:
        return fhir_mapper

    def get_generator(self) -> FHIRResourceGenerator:
        return fhir_resource_generator


fhir_registry = FHIRRegistry()
