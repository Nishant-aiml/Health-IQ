# --------------------------------------------------
# File: registry.py
# Purpose: Central Medicine Knowledge & Resolution Registry.
# Module: Medicine Intelligence
# Used By: Services and Controllers
# Future Phase: Phase 3A Medicine Intelligence
# --------------------------------------------------

from backend.app.medicine.models import MedicineInfo
from backend.app.medicine.resolver import medicine_resolver, MedicineResolver
from backend.app.medicine.loader import medicine_loader, MedicineKnowledgeLoader


class MedicineRegistry:
    """Central access point for medicine resolution and knowledge base lookups."""

    def resolve_medicine(self, raw_name: str, ocr_confidence: float = 1.0) -> MedicineInfo:
        return medicine_resolver.resolve(raw_name, ocr_confidence=ocr_confidence)


medicine_registry = MedicineRegistry()
