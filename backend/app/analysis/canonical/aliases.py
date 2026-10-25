# --------------------------------------------------
# File: aliases.py
# Purpose: Canonical lab parameter synonym alias mappings with robust matching.
# Module: Analysis Engine / Canonical Dictionary
# Used By: Report Normalizer
# --------------------------------------------------

from typing import Dict, Optional

# Standard Dictionary of Lab Parameter Synonym Aliases
CANONICAL_ALIASES: Dict[str, str] = {
    # Hematology / CBC
    "hb": "Hemoglobin",
    "hgb": "Hemoglobin",
    "hemoglobin": "Hemoglobin",
    "haemoglobin": "Hemoglobin",
    "wbc": "White Blood Cell Count",
    "white blood cell": "White Blood Cell Count",
    "white blood cells": "White Blood Cell Count",
    "white blood cell (wbc)": "White Blood Cell Count",
    "leukocytes": "White Blood Cell Count",
    "rbc": "Red Blood Cell Count",
    "red blood cell": "Red Blood Cell Count",
    "erythrocytes": "Red Blood Cell Count",
    "platelets": "Platelet Count",
    "plt": "Platelet Count",
    "platelet count": "Platelet Count",
    "mcv": "Mean Corpuscular Volume",
    "mch": "Mean Corpuscular Hemoglobin",
    "mchc": "Mean Corpuscular Hemoglobin Concentration",

    # Metabolic & Blood Sugar
    "fbs": "Fasting Blood Sugar",
    "fasting glucose": "Fasting Blood Sugar",
    "fasting blood sugar": "Fasting Blood Sugar",
    "fasting plasma glucose": "Fasting Blood Sugar",
    "ppbs": "Postprandial Blood Sugar",
    "hba1c": "HbA1c",
    "glycated hemoglobin": "HbA1c",

    # Lipid Profile
    "cholesterol": "Total Cholesterol",
    "total cholesterol": "Total Cholesterol",
    "triglycerides": "Triglycerides",
    "tg": "Triglycerides",
    "hdl": "HDL Cholesterol",
    "hdl cholesterol": "HDL Cholesterol",
    "ldl": "LDL Cholesterol",
    "ldl cholesterol": "LDL Cholesterol",

    # Kidney Function
    "creatinine": "Serum Creatinine",
    "serum creatinine": "Serum Creatinine",
    "bun": "Blood Urea Nitrogen",
    "urea": "Blood Urea",

    # Thyroid Function
    "tsh": "Thyroid Stimulating Hormone",
    "thyroid stimulating hormone": "Thyroid Stimulating Hormone",
    "t3": "Triiodothyronine (T3)",
    "t4": "Thyroxine (T4)",
}


def resolve_canonical_name(raw_name: str) -> Optional[str]:
    """
    Resolves a raw lab parameter string to its canonical dictionary name.

    Inputs:
        raw_name: Raw parameter string extracted by OCR.

    Returns:
        Canonical parameter string if matched, or None if unrecognized.
    """
    cleaned_key = raw_name.strip().lower()
    if cleaned_key in CANONICAL_ALIASES:
        return CANONICAL_ALIASES[cleaned_key]

    # Partial / substring match fallback
    for key, canonical_name in CANONICAL_ALIASES.items():
        if key in cleaned_key or cleaned_key in key:
            return canonical_name

    return None
