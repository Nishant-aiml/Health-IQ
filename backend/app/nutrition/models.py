# --------------------------------------------------
# File: models.py
# Purpose: Domain models for structured food database, nutrients, and dietary patterns.
# Module: Nutrition Knowledge Engine / Models
# Used By: Knowledge Base & Recommendation Engine
# Future Phase: Phase 3C Nutrition & Lifestyle Intelligence
# --------------------------------------------------

from typing import List, Optional, Dict, Any
from enum import Enum
from pydantic import BaseModel, Field


class FoodCategory(str, Enum):
    VEGETABLES = "Vegetables"
    FRUITS = "Fruits"
    WHOLE_GRAINS = "Whole Grains"
    LEAN_PROTEINS = "Lean Proteins"
    HEALTHY_FATS = "Healthy Fats"
    DAIRY_ALTERNATIVES = "Dairy & Alternatives"
    SEEDS_NUTS = "Seeds & Nuts"
    HERBS_SPICES = "Herbs & Spices"
    BEVERAGES = "Hydration & Teas"


class EvidenceLevel(str, Enum):
    HIGH = "High Clinical Evidence (WHO/ICMR/USDA)"
    MEDIUM = "Moderate Clinical Consensus"
    EMERGING = "Emerging Observational Evidence"


class NutrientProfile(BaseModel):
    name: str
    amount: float
    unit: str
    daily_value_pct: Optional[float] = None


class FoodItem(BaseModel):
    food_id: str
    name: str
    category: FoodCategory
    glycemic_index: Optional[int] = None
    nutrients: List[NutrientProfile] = Field(default_factory=list)
    health_benefits: List[str] = Field(default_factory=list)
    limitations: List[str] = Field(default_factory=list)
    food_drug_interactions: List[str] = Field(default_factory=list)
    evidence_level: EvidenceLevel = EvidenceLevel.HIGH
    evidence_source: str = "WHO & ICMR Dietary Guidelines"


class MicronutrientInfo(BaseModel):
    name: str
    biological_role: str
    dietary_sources: List[str]
    deficiency_signs: List[str]
    lab_markers_linked: List[str]


class MacronutrientRatio(BaseModel):
    carbohydrates_pct: float
    protein_pct: float
    fats_pct: float
    fiber_grams_daily: float
    guidance_note: str
