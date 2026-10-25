# --------------------------------------------------
# File: pregnancy.py
# Purpose: Pregnancy safety rules and warning checks.
# Module: Medicine Interaction Engine / Rules
# Used By: Interaction Checker
# Future Phase: Phase 3A Medicine Intelligence
# --------------------------------------------------

from typing import List
from backend.app.medicine.interactions.models import DrugInteractionItem
from backend.app.medicine.knowledge import PREGNANCY_CATEGORIES


def check_pregnancy_warnings(generic_names: List[str], is_pregnant: bool = False) -> List[DrugInteractionItem]:
    results: List[DrugInteractionItem] = []
    for g_name in generic_names:
        key = g_name.lower()
        info = PREGNANCY_CATEGORIES.get(key)
        if info:
            cat = info["category"]
            note = info["note"]
            severity = "HIGH" if cat in ["D", "X"] else "MEDIUM" if cat == "C" else "LOW"

            if is_pregnant and cat in ["D", "X"]:
                results.append(
                    DrugInteractionItem(
                        drug_a=g_name.capitalize(),
                        severity="HIGH",
                        interaction_type="pregnancy",
                        title=f"CRITICAL: Pregnancy Category {cat} Warning ({g_name.capitalize()})",
                        description=f"Category {cat}: {note}",
                        recommendation="Immediate physician consultation required prior to use during pregnancy.",
                        evidence_source="FDA / WHO Pregnancy Risk Guidelines",
                    )
                )
            elif cat in ["C", "D", "X"]:
                results.append(
                    DrugInteractionItem(
                        drug_a=g_name.capitalize(),
                        severity=severity,
                        interaction_type="pregnancy",
                        title=f"Pregnancy Category {cat} Caution ({g_name.capitalize()})",
                        description=note,
                        recommendation="Inform your doctor if pregnant, planning pregnancy, or breastfeeding.",
                        evidence_source="FDA Pregnancy Risk Categories",
                    )
                )
    return results
