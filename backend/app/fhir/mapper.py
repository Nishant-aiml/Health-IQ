# --------------------------------------------------
# File: mapper.py
# Purpose: Maps internal HealthLens report models to standard FHIR R4 JSON Bundle.
# Module: FHIR R4 Engine / Mapper
# Used By: Clinical Export & Service
# Future Phase: Phase 4 Clinical Collaboration & Digital Health Ecosystem
# --------------------------------------------------

from typing import Dict, Any
from backend.app.fhir.models import FHIRBundle
from backend.app.fhir.resources import fhir_resource_generator


class FHIRMapper:
    """Maps HealthLens AI analysis into FHIR R4 compliant collection bundle."""

    def map_report_to_fhir(self, report_id: int, analysis_data: Dict[str, Any], user_id: int = 1) -> FHIRBundle:
        entries = []

        # 1. Patient Resource
        entries.append({"resource": fhir_resource_generator.build_patient(user_id)})

        # 2. DiagnosticReport Resource
        entries.append({"resource": fhir_resource_generator.build_diagnostic_report(report_id, analysis_data.get("health_score", 85.0))})

        # 3. Observation Resources for parameters
        for val in analysis_data.get("extracted_values", []):
            param = val.get("parameter_name", "Biomarker")
            v = float(val.get("value", 0.0))
            u = val.get("unit", "units")
            entries.append({"resource": fhir_resource_generator.build_observation(param, v, u, report_id)})

        return FHIRBundle(entry=entries)


fhir_mapper = FHIRMapper()
