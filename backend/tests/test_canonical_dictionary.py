# --------------------------------------------------
# File: test_canonical_dictionary.py
# Purpose: Unit tests for canonical lab parameter alias mapping and unit normalization.
# Module: Backend Test Suite / Analysis Engine
# Used By: Pytest Execution
# Future Phase: Phase 2A Validation
# --------------------------------------------------

from backend.app.analysis import (
    resolve_canonical_name,
    normalize_unit,
    is_physiologically_plausible,
)


def test_alias_resolution():
    assert resolve_canonical_name("Hb") == "Hemoglobin"
    assert resolve_canonical_name("HGB") == "Hemoglobin"
    assert resolve_canonical_name("FBS") == "Fasting Blood Sugar"
    assert resolve_canonical_name("glycated hemoglobin") == "HbA1c"
    assert resolve_canonical_name("unknown_xyz_param") is None


def test_unit_normalization():
    # Fasting Blood Sugar: mmol/L to mg/dL
    val, unit = normalize_unit("Fasting Blood Sugar", 10.0, "mmol/L")
    assert unit == "mg/dL"
    assert val == 180.2

    # Serum Creatinine: umol/L to mg/dL
    val, unit = normalize_unit("Serum Creatinine", 88.4, "umol/L")
    assert unit == "mg/dL"
    assert val == 1.0


def test_physiological_plausibility():
    assert is_physiologically_plausible("Hemoglobin", 14.5) is True
    assert is_physiologically_plausible("Hemoglobin", -5.0) is False
    assert is_physiologically_plausible("Hemoglobin", 500.0) is False
