# --------------------------------------------------
# File: nutrition_context.py
# Purpose: Nutrition & Lifestyle context builder injecting guidance, food-drug warnings, and hydration targets into Grounded Chat.
# Module: RAG Engine / Context Injector
# Used By: Grounded Chat Service
# Future Phase: Phase 3C Nutrition & Lifestyle Intelligence
# --------------------------------------------------

from typing import List, Dict, Any, Optional


def build_nutrition_rag_context(
    nutrition_bundle: Dict[str, Any],
    food_interactions: List[Dict[str, Any]],
    lifestyle_bundle: Dict[str, Any],
    wellness_scores: Dict[str, Any],
) -> str:
    """Builds structured nutrition and lifestyle context string for RAG Chat prompt injection."""
    lines = ["Personalized Nutrition & Lifestyle Context:"]

    # Wellness score summary
    if wellness_scores:
        lines.append(
            f"- Overall Wellness Score: {wellness_scores.get('overall_wellness_score')}/100 "
            f"(Nutrition: {wellness_scores.get('nutrition_score')}, Lifestyle: {wellness_scores.get('lifestyle_score')}, Hydration: {wellness_scores.get('hydration_score')}, Sleep: {wellness_scores.get('sleep_score')})"
        )

    # Food-Drug Interactions
    if food_interactions:
        lines.append("- Critical Food-Drug Interactions Flagged:")
        for inter in food_interactions:
            lines.append(
                f"  * Drug '{inter.get('drug_name')}': Avoid/Monitor '{inter.get('interacting_food_or_substance')}'. Timing: {inter.get('actionable_timing_guidance')}"
            )

    # Nutrition Recommendations
    recs = nutrition_bundle.get("recommendations", [])
    if recs:
        lines.append("- Personalized Dietary Guidance:")
        for r in recs:
            lines.append(f"  * [{r.get('action')}] {r.get('target_food_or_group')}: {r.get('reasoning')}")

    # Hydration Target
    hy = lifestyle_bundle.get("hydration", {})
    if hy:
        lines.append(
            f"- Hydration Target: {hy.get('daily_volume_liters')} Liters ({hy.get('daily_glasses_count')} glasses/day). Pacing: {hy.get('pacing_guideline')}"
        )

    # Exercise Plan
    ex_list = lifestyle_bundle.get("exercise", [])
    if ex_list:
        lines.append("- Physical Activity Plan:")
        for ex in ex_list:
            lines.append(f"  * {ex.get('activity_name')} ({ex.get('frequency_weekly')}, {ex.get('duration_minutes_per_session')} mins): {ex.get('physiological_rationale')}")

    return "\n".join(lines)
