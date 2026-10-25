# --------------------------------------------------
# File: __init__.py
# Purpose: Medicine Explanation Engine package index.
# Module: Medicine Explanation Engine
# Used By: Medicine Services
# Future Phase: Phase 3A Medicine Intelligence
# --------------------------------------------------

from backend.app.medicine.explainer.engine import MedicineExplainerEngine, medicine_explainer_engine
from backend.app.medicine.explainer.eli10 import generate_eli10_explanation

__all__ = [
    "MedicineExplainerEngine",
    "medicine_explainer_engine",
    "generate_eli10_explanation",
]
