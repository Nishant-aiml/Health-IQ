# --------------------------------------------------
# File: test_interactions.py
# Purpose: Unit tests for modular drug-drug interaction rules and duplicate therapy detection.
# Module: Backend Test Suite / Interaction Engine
# Used By: Pytest Execution
# Future Phase: Phase 3A Validation
# --------------------------------------------------

from backend.app.medicine.interactions.checker import interaction_checker


def test_drug_drug_interaction_detection():
    # Aspirin + Ibuprofen -> HIGH severity interaction
    safety = interaction_checker.evaluate_safety(["Aspirin", "Ibuprofen"])
    assert len(safety.interactions) >= 1
    assert safety.has_high_risk is True
    assert any(i.severity == "HIGH" for i in safety.interactions)


def test_duplicate_therapy_detection():
    # Pantoprazole + Omeprazole -> Duplicate PPI therapy
    safety = interaction_checker.evaluate_safety(["Pantoprazole", "Omeprazole"])
    assert len(safety.duplicate_therapies) >= 1
