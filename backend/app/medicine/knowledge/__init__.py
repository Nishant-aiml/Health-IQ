# --------------------------------------------------
# File: __init__.py
# Purpose: Modular Knowledge Base package index.
# Module: Medicine Knowledge
# Used By: Medicine Loader & Registry
# Future Phase: Phase 3A Medicine Intelligence
# --------------------------------------------------

from backend.app.medicine.knowledge.generic import GENERIC_DRUGS
from backend.app.medicine.knowledge.brands import BRAND_TO_GENERIC_MAP
from backend.app.medicine.knowledge.categories import DRUG_CATEGORIES
from backend.app.medicine.knowledge.warnings import GENERAL_SAFETY_DISCLAIMER, DRIVING_WARNINGS
from backend.app.medicine.knowledge.contraindications import CONTRAINDICATIONS
from backend.app.medicine.knowledge.storage import STORAGE_INSTRUCTIONS
from backend.app.medicine.knowledge.pregnancy import PREGNANCY_CATEGORIES
from backend.app.medicine.knowledge.food import FOOD_WARNINGS

__all__ = [
    "GENERIC_DRUGS",
    "BRAND_TO_GENERIC_MAP",
    "DRUG_CATEGORIES",
    "GENERAL_SAFETY_DISCLAIMER",
    "DRIVING_WARNINGS",
    "CONTRAINDICATIONS",
    "STORAGE_INSTRUCTIONS",
    "PREGNANCY_CATEGORIES",
    "FOOD_WARNINGS",
]
