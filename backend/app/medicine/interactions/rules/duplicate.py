# --------------------------------------------------
# File: duplicate.py
# Purpose: Duplicate therapy and double-dosing detector rules.
# Module: Medicine Interaction Engine / Rules
# Used By: Interaction Checker
# Future Phase: Phase 3A Medicine Intelligence
# --------------------------------------------------

from typing import List
from collections import Counter
from backend.app.medicine.interactions.models import DrugInteractionItem
from backend.app.medicine.knowledge import GENERIC_DRUGS


def check_duplicate_therapies(generic_names: List[str]) -> List[DrugInteractionItem]:
    """Detects duplicate drug classes or duplicate generic medicine prescriptions."""
    results: List[DrugInteractionItem] = []
    keys_lower = [g.lower() for g in generic_names]

    # Check 1: Identical Generic Medicine Prescribed Twice
    counts = Counter(keys_lower)
    for g_name, count in counts.items():
        if count > 1:
            results.append(
                DrugInteractionItem(
                    drug_a=g_name.capitalize(),
                    drug_b=g_name.capitalize(),
                    severity="HIGH",
                    interaction_type="duplicate",
                    title=f"Duplicate Prescription Detected ({g_name.capitalize()})",
                    description=f"Multiple doses of {g_name.capitalize()} appear on the prescription.",
                    recommendation="Verify with physician to avoid accidental double-dosing.",
                    evidence_source="Clinical Safety Guardrails",
                )
            )

    # Check 2: Same Drug Class Overlap (e.g., 2 Proton Pump Inhibitors)
    classes_seen = {}
    for g_name in keys_lower:
        info = GENERIC_DRUGS.get(g_name)
        if info:
            d_class = info["drug_class"]
            if d_class in classes_seen:
                prev_drug = classes_seen[d_class]
                if prev_drug != g_name:
                    results.append(
                        DrugInteractionItem(
                            drug_a=prev_drug.capitalize(),
                            drug_b=g_name.capitalize(),
                            severity="MEDIUM",
                            interaction_type="duplicate",
                            title=f"Duplicate Drug Class Overlap ({d_class})",
                            description=f"Both {prev_drug.capitalize()} and {g_name.capitalize()} belong to the same drug class ({d_class}).",
                            recommendation="Consult prescribing doctor to confirm if dual therapy is intended.",
                            evidence_source="Pharmacological Class Redundancy Check",
                        )
                    )
            else:
                classes_seen[d_class] = g_name

    return results
