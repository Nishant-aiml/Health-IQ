# --------------------------------------------------
# File: test_medicine_resolver.py
# Purpose: Unit tests for medicine resolution pipeline and fuzzy match fallbacks.
# Module: Backend Test Suite / Medicine Engine
# Used By: Pytest Execution
# Future Phase: Phase 3A Validation
# --------------------------------------------------

from backend.app.medicine.resolver import medicine_resolver


def test_brand_to_generic_resolution():
    info = medicine_resolver.resolve("Tab. Glycomet 500mg")
    assert info.generic_name == "Metformin"
    assert info.active_ingredient == "Metformin Hydrochloride"
    assert info.resolution_confidence >= 0.9


def test_unknown_medicine_resolution():
    info = medicine_resolver.resolve("Tab. UnknownDrugX 10mg")
    assert info.is_unknown is True
    assert info.resolution_confidence < 0.5
    assert isinstance(info.possible_matches, list)
