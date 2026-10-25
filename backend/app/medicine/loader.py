# --------------------------------------------------
# File: loader.py
# Purpose: Knowledge Base Loader assembling modular drug data and fuzzy search matching.
# Module: Medicine Intelligence / Loader
# Used By: Medicine Registry & Resolution Pipeline
# Future Phase: Phase 3A Medicine Intelligence
# --------------------------------------------------

from typing import Optional, Dict, Any, List
import difflib
from backend.app.medicine.models import MedicineInfo
from backend.app.medicine.knowledge import (
    GENERIC_DRUGS,
    BRAND_TO_GENERIC_MAP,
    DRIVING_WARNINGS,
    CONTRAINDICATIONS,
    STORAGE_INSTRUCTIONS,
    PREGNANCY_CATEGORIES,
    FOOD_WARNINGS,
)


class MedicineKnowledgeLoader:
    """
    Assembles structured pharmacology knowledge across modular knowledge files.
    """

    def get_medicine_info(self, generic_key: str, brand_name: Optional[str] = None) -> Optional[MedicineInfo]:
        key = generic_key.lower().strip()
        data = GENERIC_DRUGS.get(key)
        if not data:
            return None

        # Build complete MedicineInfo object from modular dictionaries
        pregnancy_info = PREGNANCY_CATEGORIES.get(key, {"category": "B", "note": "Consult physician during pregnancy."})
        driving = DRIVING_WARNINGS.get(key, "No major driving impairment expected. Caution advised.")
        storage = STORAGE_INSTRUCTIONS.get(key, "Store below 30°C in a dry place.")
        contra = CONTRAINDICATIONS.get(key, ["Known hypersensitivity to active drug component."])
        food = FOOD_WARNINGS.get(key, ["Take as directed by doctor."])

        # Reverse lookup brand names for this generic
        matching_brands = [
            b.capitalize() for b, g in BRAND_TO_GENERIC_MAP.items() if g.lower() == key
        ]

        return MedicineInfo(
            generic_name=data["generic_name"],
            brand_name=brand_name or (matching_brands[0] if matching_brands else data["generic_name"]),
            brand_names=matching_brands,
            active_ingredient=data["active_ingredient"],
            drug_class=data["drug_class"],
            category=data["category"],
            purpose=data["purpose"],
            mechanism=data["mechanism"],
            common_uses=data["common_uses"],
            adult_dosage=data["adult_dosage"],
            pregnancy_warning=pregnancy_info["note"],
            pregnancy_category=pregnancy_info["category"],
            storage=storage,
            side_effects=data["side_effects"],
            contraindications=contra,
            common_interactions=[],
            food_warnings=food,
            driving_warning=driving,
            ocr_confidence=1.0,
            resolution_confidence=1.0,
            knowledge_confidence=1.0,
            is_unknown=False,
        )

    def fuzzy_match_medicine(self, term: str) -> List[str]:
        """Finds possible generic and brand drug name matches using string distance ratio."""
        term_clean = term.lower().strip()
        all_keys = list(GENERIC_DRUGS.keys()) + list(BRAND_TO_GENERIC_MAP.keys())
        matches = difflib.get_close_matches(term_clean, all_keys, n=3, cutoff=0.5)
        return [m.capitalize() for m in matches]


medicine_loader = MedicineKnowledgeLoader()
