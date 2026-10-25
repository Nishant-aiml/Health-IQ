# --------------------------------------------------
# File: loader.py
# Purpose: Pharmacology and WHO Essential Medicines reference documents loader for Hybrid RAG.
# Module: RAG Engine / Medicine Corpus
# Used By: Hybrid Medical RAG Indexer
# Future Phase: Phase 3A Medicine Intelligence
# --------------------------------------------------

from typing import List, Dict, Any
from backend.app.core.logging import logger

DRUG_REFERENCE_DOCUMENTS: List[Dict[str, Any]] = [
    {
        "source_name": "WHO Model List of Essential Medicines",
        "source_url": "https://www.who.int/medicines/publications/essentialmedicines/en/",
        "title": "WHO Essential Medicines: Antidiabetic Agents (Metformin)",
        "medical_topic": "Metformin",
        "chunk_text": (
            "Metformin hydrochloride is a biguanide antidiabetic agent recommended as first-line therapy for type 2 diabetes mellitus. "
            "It decreases hepatic glucose production and increases peripheral insulin sensitivity. "
            "Primary precautions include renal function monitoring (eGFR < 30 mL/min contraindicated) and avoiding heavy alcohol intake to prevent lactic acidosis."
        ),
    },
    {
        "source_name": "WHO Model List of Essential Medicines",
        "source_url": "https://www.who.int/medicines/publications/essentialmedicines/en/",
        "title": "WHO Essential Medicines: Antibiotics (Amoxicillin)",
        "medical_topic": "Amoxicillin",
        "chunk_text": (
            "Amoxicillin is a moderate-spectrum beta-lactam penicillin antibiotic used for upper respiratory, ear, nose, throat, and urinary tract infections. "
            "Patient compliance: Complete the full prescribed course even if symptoms resolve early to prevent antibiotic resistance."
        ),
    },
    {
        "source_name": "ICMR Guidelines for Cardiovascular Health",
        "source_url": "https://www.icmr.gov.in/",
        "title": "ICMR Guidelines: Lipid Lowering Therapy (Atorvastatin)",
        "medical_topic": "Atorvastatin",
        "chunk_text": (
            "Atorvastatin competitively inhibits HMG-CoA reductase to reduce LDL cholesterol and cardiovascular morbidity. "
            "Statins should be taken consistently, preferably in the evening. Muscle pain (myalgia) or dark urine should be reported to a physician."
        ),
    },
    {
        "source_name": "CDC Hypertension Guidelines",
        "source_url": "https://www.cdc.gov/bloodpressure/",
        "title": "CDC Standards: Antihypertensive Therapy (Amlodipine & Telmisartan)",
        "medical_topic": "Antihypertensives",
        "chunk_text": (
            "Calcium Channel Blockers (Amlodipine) and Angiotensin II Receptor Blockers (Telmisartan) lower blood pressure and reduce cardiac events. "
            "Patients should monitor blood pressure regularly. Telmisartan is contraindicated in 2nd and 3rd trimester pregnancy."
        ),
    },
    {
        "source_name": "National Institutes of Health (NIH) Drug Safety",
        "source_url": "https://www.ncbi.nlm.nih.gov/books/NBK548010/",
        "title": "NIH Clinical Safety: Proton Pump Inhibitors (Pantoprazole & Omeprazole)",
        "medical_topic": "Proton Pump Inhibitors",
        "chunk_text": (
            "Proton Pump Inhibitors (Pantoprazole, Omeprazole) suppress stomach acid by blocking H+/K+-ATPase parietal cell pumps. "
            "Optimal efficacy is achieved when administered 30 to 60 minutes before breakfast."
        ),
    },
]


def load_medicine_corpus_documents() -> List[Dict[str, Any]]:
    logger.info(f"Loaded {len(DRUG_REFERENCE_DOCUMENTS)} medicine reference guidelines into Hybrid RAG corpus.")
    return DRUG_REFERENCE_DOCUMENTS
