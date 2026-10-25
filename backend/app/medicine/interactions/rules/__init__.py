# --------------------------------------------------
# File: __init__.py
# Purpose: Modular Interaction Rules package index.
# Module: Medicine Interaction Engine / Rules
# Used By: Interaction Checker & Registry
# Future Phase: Phase 3A Medicine Intelligence
# --------------------------------------------------

from backend.app.medicine.interactions.rules.drug_drug import check_drug_drug_interactions
from backend.app.medicine.interactions.rules.duplicate import check_duplicate_therapies
from backend.app.medicine.interactions.rules.food import check_food_interactions
from backend.app.medicine.interactions.rules.pregnancy import check_pregnancy_warnings
from backend.app.medicine.interactions.rules.alcohol import check_alcohol_warnings
from backend.app.medicine.interactions.rules.driving import check_driving_warnings

__all__ = [
    "check_drug_drug_interactions",
    "check_duplicate_therapies",
    "check_food_interactions",
    "check_pregnancy_warnings",
    "check_alcohol_warnings",
    "check_driving_warnings",
]
