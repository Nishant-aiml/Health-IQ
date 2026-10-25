# --------------------------------------------------
# File: drug_drug.py
# Purpose: Deterministic Drug-Drug interaction rule definitions.
# Module: Medicine Interaction Engine / Rules
# Used By: Interaction Checker
# Future Phase: Phase 3A Medicine Intelligence
# --------------------------------------------------

from typing import List, Dict, Tuple
from backend.app.medicine.interactions.models import DrugInteractionItem

KNOWN_DRUG_DRUG_INTERACTIONS: List[Tuple[str, str, str, str, str, str]] = [
    # (Drug A, Drug B, Severity, Title, Description, Recommendation)
    (
        "aspirin",
        "ibuprofen",
        "HIGH",
        "NSAID Co-Administration & Antiplatelet Antagonism",
        "Ibuprofen interferes with the irreversible antiplatelet effect of low-dose Aspirin, increasing cardiovascular risk and gastric bleeding.",
        "Avoid taking Ibuprofen simultaneously with Aspirin. Separate dosing by at least 8 hours if medically required.",
    ),
    (
        "telmisartan",
        "aspirin",
        "MEDIUM",
        "Renal Hemodynamic Interference",
        "High-dose Aspirin or NSAIDs can attenuate the blood pressure-lowering effect of Angiotensin II Receptor Blockers (Telmisartan).",
        "Monitor blood pressure regularly if taking NSAIDs concurrently with Telmisartan.",
    ),
    (
        "atorvastatin",
        "amlodipine",
        "MEDIUM",
        "Statin Concentration Elevation",
        "Amlodipine increases serum exposure of Atorvastatin, slightly elevating the risk of muscle discomfort (myalgia).",
        "Limit Atorvastatin dose or monitor for unexplained muscle pain, tenderness, or weakness.",
    ),
    (
        "pantoprazole",
        "azithromycin",
        "LOW",
        "Gastric Absorption & Bioavailability Timing",
        "Proton pump inhibitors alter gastric pH which may slightly affect initial absorption timing.",
        "Maintain scheduled administration times.",
    ),
    (
        "metformin",
        "telmisartan",
        "LOW",
        "Glycemic & Electrolyte Co-Monitoring",
        "Both agents affect metabolic regulation; combination is clinically common for diabetic hypertensives.",
        "Routine periodic monitoring of serum creatinine and HbA1c is recommended.",
    ),
]


def check_drug_drug_interactions(generic_names: List[str]) -> List[DrugInteractionItem]:
    """Checks list of generic medicine keys for deterministic drug-drug interactions."""
    results: List[DrugInteractionItem] = []
    keys_lower = [g.lower() for g in generic_names]

    for drug_a, drug_b, severity, title, desc, rec in KNOWN_DRUG_DRUG_INTERACTIONS:
        if drug_a in keys_lower and drug_b in keys_lower:
            results.append(
                DrugInteractionItem(
                    drug_a=drug_a.capitalize(),
                    drug_b=drug_b.capitalize(),
                    severity=severity,
                    interaction_type="drug_drug",
                    title=title,
                    description=desc,
                    recommendation=rec,
                    evidence_source="WHO / Clinical Pharmacology Guidelines",
                )
            )
    return results
