# --------------------------------------------------
# File: test_food_interactions.py
# Purpose: Unit tests for Food-Medicine Interaction Engine rules and drug checker.
# Module: Backend Test Suite / Food Interactions
# Used By: Pytest Execution
# Future Phase: Phase 3C Validation
# --------------------------------------------------

from backend.app.nutrition.interactions.checker import food_medicine_interaction_checker
from backend.app.nutrition.interactions.models import InteractionSeverity


def test_food_drug_interaction_checker():
    drugs = ["Warfarin", "Levothyroxine 50mcg", "Atorvastatin"]

    flagged = food_medicine_interaction_checker.check_interactions(drugs)

    assert len(flagged) == 3
    drug_names = [f.drug_name for f in flagged]
    assert "Warfarin" in drug_names
    assert "Levothyroxine" in drug_names
    assert "Atorvastatin" in drug_names

    # Check high severity
    severities = [f.severity for f in flagged]
    assert InteractionSeverity.HIGH in severities
