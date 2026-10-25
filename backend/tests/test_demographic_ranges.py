# --------------------------------------------------
# File: test_demographic_ranges.py
# Purpose: Unit tests for demographic-adjusted normal reference range calculations.
# Module: Backend Test Suite / Analysis Engine
# Used By: Pytest Execution
# Future Phase: Phase 2A Validation
# --------------------------------------------------

from backend.app.analysis import get_demographic_normal_range


def test_hemoglobin_demographic_ranges():
    # Male baseline
    low_m, high_m = get_demographic_normal_range("Hemoglobin", age=30, gender="male", pregnant=False)
    assert low_m == 13.8
    assert high_m == 17.2

    # Female non-pregnant baseline
    low_f, high_f = get_demographic_normal_range("Hemoglobin", age=30, gender="female", pregnant=False)
    assert low_f == 12.0
    assert high_f == 15.5

    # Pregnant baseline
    low_p, high_p = get_demographic_normal_range("Hemoglobin", age=28, gender="female", pregnant=True)
    assert low_p == 11.0
    assert high_p == 14.0
