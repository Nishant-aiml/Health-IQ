# --------------------------------------------------
# File: alcohol.py
# Purpose: Alcohol interaction rule definitions.
# Module: Medicine Interaction Engine / Rules
# Used By: Interaction Checker
# Future Phase: Phase 3A Medicine Intelligence
# --------------------------------------------------

from typing import List
from backend.app.medicine.interactions.models import DrugInteractionItem

ALCOHOL_RISKS = {
    "metformin": ("HIGH", "Lactic Acidosis Risk", "Alcohol increases the risk of metformin-induced lactic acidosis and hypoglycemia."),
    "paracetamol": ("HIGH", "Hepatotoxicity Risk", "Chronic alcohol use with paracetamol markedly increases severe liver injury risk."),
    "cetirizine": ("MEDIUM", "Central Nervous System Depression", "Alcohol enhances drowsiness and motor impairment caused by antihistamines."),
    "aspirin": ("MEDIUM", "Gastric Bleeding Risk", "Alcohol and aspirin combined significantly increase gastrointestinal ulcer and bleeding risk."),
}


def check_alcohol_warnings(generic_names: List[str]) -> List[DrugInteractionItem]:
    results: List[DrugInteractionItem] = []
    for g_name in generic_names:
        key = g_name.lower()
        if key in ALCOHOL_RISKS:
            sev, title, desc = ALCOHOL_RISKS[key]
            results.append(
                DrugInteractionItem(
                    drug_a=g_name.capitalize(),
                    severity=sev,
                    interaction_type="alcohol",
                    title=f"Alcohol Warning: {title} ({g_name.capitalize()})",
                    description=desc,
                    recommendation="Avoid alcohol consumption while taking this medication.",
                    evidence_source="Clinical Alcohol-Drug Interaction Guidelines",
                )
            )
    return results
