# --------------------------------------------------
# File: templates.py
# Purpose: Templates for patient-friendly medicine explanations and safety notes.
# Module: Medicine Explanation Engine / Templates
# Used By: Medicine Explainer Engine
# Future Phase: Phase 3A Medicine Intelligence
# --------------------------------------------------

EXPLANATION_DISCLAIMER = (
    "This information is educational and does not replace medical advice. "
    "Never stop or alter dosage of prescribed medicines without consulting your prescribing doctor."
)

EXPLANATION_TEMPLATE = """
{brand_name} (Generic: {generic_name}, Active Ingredient: {active_ingredient}) belongs to the {drug_class} family.

Primary Purpose:
{purpose}

How It Works:
{mechanism}

Common Uses:
- {common_uses}

Standard Adult Dosage:
{adult_dosage}

Important Safety Guidance:
- Food Instruction: {food_warning}
- Driving Precaution: {driving_warning}
- Pregnancy Note: {pregnancy_warning}

Storage & Care:
{storage}
"""
