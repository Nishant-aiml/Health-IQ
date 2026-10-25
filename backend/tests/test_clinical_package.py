# --------------------------------------------------
# File: test_clinical_package.py
# Purpose: Unit tests for Clinical Case Package Builder, SHA-256 integrity hash, and audience formatting.
# Module: Backend Test Suite / Clinical Package
# Used By: Pytest Execution
# Future Phase: Phase 4 Validation
# --------------------------------------------------

from backend.app.clinical.builder import clinical_package_builder
from backend.app.clinical.formatter import clinical_package_formatter
from backend.app.clinical.models import AudienceTarget, ClinicalPackageStatus


def test_clinical_package_builder_and_sha256():
    pkg = clinical_package_builder.build_package(
        report_id=1,
        user_id=1,
        analysis_data={"health_score": 88.0},
        prescription_data={"medicines": []},
        history_data={"reports": []},
        nutrition_data={"overall_dietary_focus": "Wellness"},
        wellness_data={"overall_wellness_score": 90.0},
        audience=AudienceTarget.DOCTOR,
    )

    assert pkg.report_id == 1
    assert pkg.status == ClinicalPackageStatus.AI_GENERATED
    assert pkg.sha256_integrity_hash is not None
    assert len(pkg.sha256_integrity_hash) == 64
    assert len(pkg.evidence_graph) == 5
    assert len(pkg.questions_for_physician) > 0


def test_clinical_package_audience_formatter():
    pkg = clinical_package_builder.build_package(
        report_id=1,
        user_id=1,
        analysis_data={"health_score": 85.0},
        prescription_data={},
        history_data={},
        nutrition_data={},
        wellness_data={},
        audience=AudienceTarget.DOCTOR,
    )

    formatted_doc = clinical_package_formatter.format_package_for_audience(pkg, AudienceTarget.DOCTOR)
    assert formatted_doc["header_title"] == "Physician Clinical Case Brief"

    formatted_fam = clinical_package_formatter.format_package_for_audience(pkg, AudienceTarget.FAMILY)
    assert "Family Care" in formatted_fam["active_summary"]
