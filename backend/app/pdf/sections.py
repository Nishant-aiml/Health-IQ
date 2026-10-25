# --------------------------------------------------
# File: sections.py
# Purpose: Assembles all PDF document sections including optional longitudinal trends, nutrition, and lifestyle sections.
# Module: PDF Engine
# Used By: PDF Layout & Builder
# Future Phase: Phase 2E, Phase 3B & Phase 3C PDF Export
# --------------------------------------------------

from typing import Dict, Any, List, Optional
from reportlab.platypus import Spacer, Paragraph
from backend.app.pdf.styles import medical_pdf_styles
from backend.app.pdf.components import (
    build_cover_header,
    build_health_score_section,
    build_parameters_table,
    build_recommendations_section,
)


def build_longitudinal_trend_pdf_section(trend_data: Dict[str, Any]) -> List[Any]:
    story = []
    story.append(Paragraph("Longitudinal Health Trends", medical_pdf_styles.h2_style))
    story.append(Spacer(1, 6))

    trends = trend_data.get("trends", [])
    for t in trends:
        text = f"<b>{t.get('canonical_name')}:</b> {str(t.get('direction', '')).upper()} ({t.get('percentage_change', 0)}%) — {t.get('clinical_summary', '')}"
        story.append(Paragraph(text, medical_pdf_styles.body_style))
        story.append(Spacer(1, 4))

    return story


def build_nutrition_lifestyle_pdf_section(nutrition_data: Dict[str, Any], lifestyle_data: Dict[str, Any], wellness_data: Dict[str, Any]) -> List[Any]:
    story = []
    story.append(Paragraph("Nutrition & Lifestyle Guidance", medical_pdf_styles.h2_style))
    story.append(Spacer(1, 6))

    if wellness_data:
        w_text = f"<b>Overall Wellness Score:</b> {wellness_data.get('overall_wellness_score')}/100 (Nutrition: {wellness_data.get('nutrition_score')}, Lifestyle: {wellness_data.get('lifestyle_score')}, Hydration: {wellness_data.get('hydration_score')}, Sleep: {wellness_data.get('sleep_score')})"
        story.append(Paragraph(w_text, medical_pdf_styles.body_style))
        story.append(Spacer(1, 4))

    if nutrition_data and nutrition_data.get("recommendations"):
        story.append(Paragraph("<b>Dietary Recommendations:</b>", medical_pdf_styles.body_style))
        for r in nutrition_data.get("recommendations", []):
            text = f"• [{r.get('action')}] <b>{r.get('target_food_or_group')}:</b> {r.get('reasoning')}"
            story.append(Paragraph(text, medical_pdf_styles.body_style))
            story.append(Spacer(1, 2))
        story.append(Spacer(1, 4))

    if nutrition_data and nutrition_data.get("food_interactions"):
        story.append(Paragraph("<b>Food-Medicine Interaction Warnings:</b>", medical_pdf_styles.body_style))
        for inter in nutrition_data.get("food_interactions", []):
            text = f"• <b>{inter.get('drug_name')} ↔ {inter.get('interacting_food_or_substance')}:</b> {inter.get('actionable_timing_guidance')}"
            story.append(Paragraph(text, medical_pdf_styles.body_style))
            story.append(Spacer(1, 2))
        story.append(Spacer(1, 4))

    if lifestyle_data and lifestyle_data.get("exercise_plan"):
        story.append(Paragraph("<b>Physical Activity & Exercise Plan:</b>", medical_pdf_styles.body_style))
        for ex in lifestyle_data.get("exercise_plan", []):
            text = f"• <b>{ex.get('activity_name')}:</b> {ex.get('frequency_weekly')}, {ex.get('duration_minutes_per_session')} mins/session. {ex.get('physiological_rationale')}"
            story.append(Paragraph(text, medical_pdf_styles.body_style))
            story.append(Spacer(1, 2))

    return story


def assemble_all_report_sections(
    analysis: Dict[str, Any],
    recommendation_bundle: Dict[str, Any],
    trend_data: Optional[Dict[str, Any]] = None,
    nutrition_data: Optional[Dict[str, Any]] = None,
    lifestyle_data: Optional[Dict[str, Any]] = None,
    wellness_data: Optional[Dict[str, Any]] = None,
) -> List[Any]:
    story = []

    # Cover & Header
    story.extend(build_cover_header(analysis))
    story.append(Spacer(1, 10))

    # Health Score & Summary
    story.extend(build_health_score_section(analysis))
    story.append(Spacer(1, 12))

    # Extracted Lab Parameters Table
    story.extend(build_parameters_table(analysis))
    story.append(Spacer(1, 12))

    # Recommendations, Doctor Questions, ELI10, Limitations
    story.extend(build_recommendations_section(recommendation_bundle))

    # Optional Longitudinal Trend Section
    if trend_data and trend_data.get("trends"):
        story.append(Spacer(1, 14))
        story.extend(build_longitudinal_trend_pdf_section(trend_data))

    # Optional Phase 3C Nutrition & Lifestyle Section
    if nutrition_data or lifestyle_data or wellness_data:
        story.append(Spacer(1, 14))
        story.extend(build_nutrition_lifestyle_pdf_section(nutrition_data or {}, lifestyle_data or {}, wellness_data or {}))

    return story
