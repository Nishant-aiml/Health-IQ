# --------------------------------------------------
# File: weights.py
# Purpose: Transparent weighting formula for composite Overall Wellness Score.
# Module: Wellness Score Engine / Weights
# Used By: Wellness Calculator
# Future Phase: Phase 3C Nutrition & Lifestyle Intelligence
# --------------------------------------------------

# Weights sum up to 1.00 (100%)
WEIGHT_HEALTH_SCORE = 0.40      # Reused Phase 2B Health Score
WEIGHT_NUTRITION_SCORE = 0.25   # Nutrition Quality
WEIGHT_LIFESTYLE_SCORE = 0.15   # Activity & Movement
WEIGHT_HYDRATION_SCORE = 0.10   # Hydration Target
WEIGHT_SLEEP_SCORE = 0.10       # Sleep Hygiene


def compute_composite_wellness_score(
    health_score: float,
    nutrition_score: float,
    lifestyle_score: float,
    hydration_score: float,
    sleep_score: float,
) -> float:
    """Computes overall wellness score using transparent weighted formula."""
    weighted = (
        (health_score * WEIGHT_HEALTH_SCORE)
        + (nutrition_score * WEIGHT_NUTRITION_SCORE)
        + (lifestyle_score * WEIGHT_LIFESTYLE_SCORE)
        + (hydration_score * WEIGHT_HYDRATION_SCORE)
        + (sleep_score * WEIGHT_SLEEP_SCORE)
    )
    return round(max(0.0, min(100.0, weighted)), 1)
