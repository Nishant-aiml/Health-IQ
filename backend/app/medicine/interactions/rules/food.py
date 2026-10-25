# --------------------------------------------------
# File: food.py
# Purpose: Food-drug interaction rule definitions.
# Module: Medicine Interaction Engine / Rules
# Used By: Interaction Checker
# Future Phase: Phase 3A Medicine Intelligence
# --------------------------------------------------

from typing import List
from backend.app.medicine.interactions.models import DrugInteractionItem
from backend.app.medicine.knowledge import FOOD_WARNINGS


def check_food_interactions(generic_names: List[str]) -> List[DrugInteractionItem]:
    results: List[DrugInteractionItem] = []
    for g_name in generic_names:
        key = g_name.lower()
        warnings = FOOD_WARNINGS.get(key, [])
        for w in warnings:
            results.append(
                DrugInteractionItem(
                    drug_a=g_name.capitalize(),
                    severity="LOW",
                    interaction_type="food",
                    title=f"Food & Timing Guidance: {g_name.capitalize()}",
                    description=w,
                    recommendation="Follow specific food timing instructions for optimal drug absorption.",
                    evidence_source="Clinical Dietary Guidance",
                )
            )
    return results
