# --------------------------------------------------
# File: test_fhir_mapping.py
# Purpose: Unit tests for FHIR R4 Mapper converting report entities into standard HL7 JSON Bundle.
# Module: Backend Test Suite / FHIR Mapper
# Used By: Pytest Execution
# Future Phase: Phase 4 Validation
# --------------------------------------------------

from backend.app.fhir.mapper import fhir_mapper


def test_fhir_mapping_bundle():
    analysis = {
        "health_score": 85.0,
        "extracted_values": [
            {"parameter_name": "Hemoglobin", "value": 14.5, "unit": "g/dL"},
            {"parameter_name": "Fasting Blood Sugar", "value": 115.0, "unit": "mg/dL"},
        ],
    }

    bundle = fhir_mapper.map_report_to_fhir(report_id=1, analysis_data=analysis, user_id=1)

    assert bundle.resourceType == "Bundle"
    assert len(bundle.entry) == 4  # 1 Patient + 1 DiagnosticReport + 2 Observations
    res_types = [e["resource"]["resourceType"] for e in bundle.entry]
    assert "Patient" in res_types
    assert "DiagnosticReport" in res_types
    assert "Observation" in res_types
