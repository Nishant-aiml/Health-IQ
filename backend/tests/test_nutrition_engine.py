# --------------------------------------------------
# File: test_nutrition_engine.py
# Purpose: Unit tests for Nutrition Knowledge Engine foods, nutrients, rules, and meal patterns.
# Module: Backend Test Suite / Nutrition Engine
# Used By: Pytest Execution
# Future Phase: Phase 3C Validation
# --------------------------------------------------

from backend.app.nutrition.knowledge import nutrition_knowledge_base
from backend.app.nutrition.recommendations.rules import evaluate_nutrition_rules
from backend.app.nutrition.recommendations.models import NutritionActionType


def test_food_database_lookup():
    spinach = nutrition_knowledge_base.get_food("spinach")
    assert spinach is not None
    assert spinach.name == "Spinach & Dark Leafy Greens"
    assert len(spinach.nutrients) > 0


def test_nutrition_recommendation_rules():
    extracted = [
        {"canonical_name": "Fasting Blood Sugar", "value": 130.0, "unit": "mg/dL", "severity": "HIGH"},
        {"canonical_name": "Hemoglobin", "value": 11.0, "unit": "g/dL", "severity": "LOW"},
    ]

    recs = evaluate_nutrition_rules(extracted, [], [])

    # Should have INCREASE soluble fiber and REDUCE refined carbs, INCREASE iron
    actions = [r.action for r in recs]
    assert NutritionActionType.INCREASE in actions
    assert NutritionActionType.REDUCE in actions
