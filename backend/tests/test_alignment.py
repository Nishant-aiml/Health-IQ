# --------------------------------------------------
# File: test_alignment.py
# Purpose: Unit tests for canonical biomarker alignment and unit harmonization.
# Module: Backend Test Suite / Biomarker Alignment
# Used By: Pytest Execution
# Future Phase: Phase 3B Validation
# --------------------------------------------------

from backend.app.history.alignment.normalizer import alignment_normalizer


def test_canonical_matching_aliases():
    res1 = alignment_normalizer.align_parameter("Hb", 13.5, "g/dL")
    assert res1.canonical_name == "Hemoglobin"

    res2 = alignment_normalizer.align_parameter("Fasting Glucose", 110, "mg/dL")
    assert res2.canonical_name == "Fasting Blood Sugar"


def test_unit_harmonization():
    # Fasting glucose: 6.0 mmol/L -> ~108.1 mg/dL
    res = alignment_normalizer.align_parameter("Fasting Blood Sugar", 6.0, "mmol/L")
    assert res.unit == "mg/dL"
    assert res.value > 100
    assert res.is_harmonized is True
