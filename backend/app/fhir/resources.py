# --------------------------------------------------
# File: resources.py
# Purpose: Resource generators creating standard HL7 FHIR R4 JSON structures.
# Module: FHIR R4 Engine / Resources
# Used By: FHIR Mapper
# Future Phase: Phase 4 Clinical Collaboration & Digital Health Ecosystem
# --------------------------------------------------

from typing import Dict, Any


class FHIRResourceGenerator:
    """Generates standard HL7 FHIR R4 resources."""

    def build_patient(self, user_id: int) -> Dict[str, Any]:
        return {
            "resourceType": "Patient",
            "id": f"pat_{user_id}",
            "gender": "male",
            "active": True,
        }

    def build_observation(self, param_name: str, value: float, unit: str, report_id: int) -> Dict[str, Any]:
        return {
            "resourceType": "Observation",
            "id": f"obs_{report_id}_{param_name.replace(' ', '_')}",
            "status": "final",
            "code": {"text": param_name},
            "valueQuantity": {"value": value, "unit": unit},
        }

    def build_diagnostic_report(self, report_id: int, score: float) -> Dict[str, Any]:
        return {
            "resourceType": "DiagnosticReport",
            "id": f"report_{report_id}",
            "status": "final",
            "code": {"text": "Laboratory Biomarker Analysis"},
            "conclusion": f"Health Lens Composite Score: {score}/100",
        }


fhir_resource_generator = FHIRResourceGenerator()
