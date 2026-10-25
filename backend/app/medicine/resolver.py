# --------------------------------------------------
# File: resolver.py
# Purpose: Dedicated Medicine Resolution Pipeline (Brand -> Generic -> Active Ingredient -> Knowledge Base).
# Module: Medicine Intelligence / Resolution
# Used By: Prescription Extractor & Medicine Service
# Future Phase: Phase 3A Medicine Intelligence
# --------------------------------------------------

import re
from typing import Optional, Tuple
from backend.app.medicine.models import MedicineInfo
from backend.app.medicine.loader import medicine_loader
from backend.app.medicine.knowledge import BRAND_TO_GENERIC_MAP, GENERIC_DRUGS
from backend.app.core.logging import logger


class MedicineResolver:
    """
    Dedicated Medicine Resolution Pipeline.

    Pipeline stages:
        1. Clean OCR raw term (strip prefixes like Tab, Cap, Syr, Inj).
        2. Check if clean term is direct Brand Name -> resolve to Generic.
        3. Check if clean term is Generic Name.
        4. Check Active Ingredient lookup.
        5. Fallback: Fuzzy search & mark unknown with candidate recommendations.
    """

    PREFIXES = [
        r"^tab\.?\s*",
        r"^tablet\.?\s*",
        r"^cap\.?\s*",
        r"^capsule\.?\s*",
        r"^syr\.?\s*",
        r"^syrup\.?\s*",
        r"^inj\.?\s*",
        r"^injection\.?\s*",
        r"^ointment\.?\s*",
        r"^cream\.?\s*",
    ]

    def clean_medicine_name(self, raw_name: str) -> str:
        name = raw_name.strip()
        for prefix in self.PREFIXES:
            name = re.sub(prefix, "", name, flags=re.IGNORECASE)
        # Remove trailing dosage like 500mg, 10mg, 5ml
        name = re.sub(r"\s+\d+\s*(mg|g|ml|mcg|iu)\b.*$", "", name, flags=re.IGNORECASE)
        return name.strip()

    def resolve(self, raw_name: str, ocr_confidence: float = 1.0) -> MedicineInfo:
        clean_name = self.clean_medicine_name(raw_name)
        clean_key = clean_name.lower()

        logger.info(f"Resolving medicine raw_name='{raw_name}' -> clean_name='{clean_name}'")

        # Stage 1: Brand Name Lookup
        if clean_key in BRAND_TO_GENERIC_MAP:
            generic_key = BRAND_TO_GENERIC_MAP[clean_key]
            info = medicine_loader.get_medicine_info(generic_key, brand_name=clean_name.capitalize())
            if info:
                info.ocr_confidence = ocr_confidence
                info.resolution_confidence = 0.95
                info.knowledge_confidence = 1.0
                return info

        # Stage 2: Generic Name Lookup
        if clean_key in GENERIC_DRUGS:
            info = medicine_loader.get_medicine_info(clean_key, brand_name=clean_name.capitalize())
            if info:
                info.ocr_confidence = ocr_confidence
                info.resolution_confidence = 1.0
                info.knowledge_confidence = 1.0
                return info

        # Stage 3: Partial / Token Match Lookup
        for g_key, g_data in GENERIC_DRUGS.items():
            if g_key in clean_key or clean_key in g_key:
                info = medicine_loader.get_medicine_info(g_key, brand_name=clean_name.capitalize())
                if info:
                    info.ocr_confidence = ocr_confidence
                    info.resolution_confidence = 0.85
                    info.knowledge_confidence = 0.9
                    return info

        # Stage 4: Unknown Medicine Fallback with Fuzzy Matching
        possible_matches = medicine_loader.fuzzy_match_medicine(clean_name)
        logger.warning(f"Unknown medicine '{clean_name}'. Suggested matches: {possible_matches}")

        return MedicineInfo(
            generic_name=clean_name.capitalize(),
            brand_name=clean_name.capitalize(),
            brand_names=[],
            active_ingredient=clean_name.capitalize(),
            drug_class="Prescribed Pharmacological Agent",
            category="General Medicine",
            purpose=f"Prescribed treatment: {clean_name.capitalize()}.",
            mechanism="Consult healthcare provider or physician for detailed mechanism of action.",
            common_uses=[clean_name.capitalize()],
            adult_dosage="As prescribed by physician",
            pregnancy_warning="Consult prescribing physician before use during pregnancy.",
            storage="Store below 30°C in a cool, dry place.",
            side_effects=["Consult doctor if adverse symptoms occur."],
            contraindications=["Known hypersensitivity."],
            common_interactions=[],
            food_warnings=["Take as directed by doctor."],
            driving_warning="Exercise general caution when starting new medications.",
            ocr_confidence=ocr_confidence,
            resolution_confidence=0.4,
            knowledge_confidence=0.5,
            is_unknown=True,
            possible_matches=possible_matches,
        )


medicine_resolver = MedicineResolver()
