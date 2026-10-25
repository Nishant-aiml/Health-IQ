# --------------------------------------------------
# File: checker.py
# Purpose: Evaluates prescribed medicines through modular rule modules and compiles a unified SafetyResult.
# Module: Medicine Interaction Engine / Checker
# Used By: Medicine Service & Prescription Service
# Future Phase: Phase 3A Medicine Intelligence
# --------------------------------------------------

from typing import List
from backend.app.medicine.interactions.models import SafetyResult
from backend.app.medicine.interactions.rules import (
    check_drug_drug_interactions,
    check_duplicate_therapies,
    check_food_interactions,
    check_pregnancy_warnings,
    check_alcohol_warnings,
    check_driving_warnings,
)


class InteractionChecker:
    """Evaluates list of prescribed medicines through modular rule engines."""

    def evaluate_safety(self, generic_names: List[str], is_pregnant: bool = False) -> SafetyResult:
        dd_interactions = check_drug_drug_interactions(generic_names)
        duplicates = check_duplicate_therapies(generic_names)
        food = check_food_interactions(generic_names)
        pregnancy = check_pregnancy_warnings(generic_names, is_pregnant=is_pregnant)
        alcohol = check_alcohol_warnings(generic_names)
        driving = check_driving_warnings(generic_names)

        all_items = dd_interactions + duplicates + food + pregnancy + alcohol + driving
        has_high_risk = any(item.severity == "HIGH" for item in all_items)

        monitoring_notes = [
            "Maintain scheduled follow-up visits with your prescribing doctor.",
            "Report any unusual side effects or symptoms immediately.",
        ]
        if has_high_risk:
            monitoring_notes.insert(0, "CRITICAL: High-risk medication interaction or safety warning detected. Consult physician.")

        return SafetyResult(
            interactions=dd_interactions,
            duplicate_therapies=duplicates,
            food_warnings=food,
            pregnancy_warnings=pregnancy,
            alcohol_warnings=alcohol,
            driving_warnings=driving,
            monitoring_notes=monitoring_notes,
            has_high_risk=has_high_risk,
        )


interaction_checker = InteractionChecker()
