# --------------------------------------------------
# File: driving.py
# Purpose: Driving and drowsiness warning rules.
# Module: Medicine Interaction Engine / Rules
# Used By: Interaction Checker
# Future Phase: Phase 3A Medicine Intelligence
# --------------------------------------------------

from typing import List
from backend.app.medicine.interactions.models import DrugInteractionItem
from backend.app.medicine.knowledge import DRIVING_WARNINGS


def check_driving_warnings(generic_names: List[str]) -> List[DrugInteractionItem]:
    results: List[DrugInteractionItem] = []
    for g_name in generic_names:
        key = g_name.lower()
        if key in DRIVING_WARNINGS:
            results.append(
                DrugInteractionItem(
                    drug_a=g_name.capitalize(),
                    severity="LOW",
                    interaction_type="driving",
                    title=f"Driving Caution: {g_name.capitalize()}",
                    description=DRIVING_WARNINGS[key],
                    recommendation="Observe individual tolerance before driving or operating heavy machinery.",
                    evidence_source="Pharmacovigilance Driving Safety Guidelines",
                )
            )
    return results
