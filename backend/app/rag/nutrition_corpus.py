# --------------------------------------------------
# File: nutrition_corpus.py
# Purpose: Nutrition RAG Corpus indexing WHO, ICMR, and clinical food composition guidelines.
# Module: RAG Engine / Nutrition Corpus
# Used By: Hybrid RAG Retriever & Grounded Chat
# Future Phase: Phase 3C Nutrition & Lifestyle Intelligence
# --------------------------------------------------

from typing import List, Dict, Any

NUTRITION_CORPUS_DOCUMENTS: List[Dict[str, str]] = [
    {
        "id": "nutr_001",
        "title": "WHO Healthy Diet & Macronutrient Guidelines",
        "source": "World Health Organization (WHO) Guidelines",
        "content": (
            "A healthy diet for adults includes fruit, vegetables, legumes (e.g. lentils and beans), nuts, and whole grains "
            "(e.g. unprocessed maize, millet, oats, wheat, and brown rice). At least 400g (5 portions) of fruit and vegetables per day. "
            "Free sugars should constitute less than 10% of total energy intake, and total fat less than 30% of total energy intake, "
            "with unsaturated fats (found in fish, avocado, and nuts) preferred over saturated fats."
        ),
    },
    {
        "id": "nutr_002",
        "title": "ICMR Dietary Guidelines for Indian Adults",
        "source": "Indian Council of Medical Research (ICMR-NIN)",
        "content": (
            "Pair non-heme iron sources (spinach, green leafy vegetables, legumes) with Vitamin C rich foods (lemon juice, amla, oranges) "
            "to enhance non-heme iron bio-absorption. Avoid drinking tea or coffee within 60 minutes of meals as polyphenols and tannins "
            "bind iron and calcium, significantly reducing intestinal absorption."
        ),
    },
    {
        "id": "nutr_003",
        "title": "FDA Clinical Food-Drug Interaction References",
        "source": "FDA Clinical Pharmacology Guidelines",
        "content": (
            "Warfarin requires consistent daily Vitamin K intake; sudden changes in green leafy vegetable consumption alter prothrombin time/INR. "
            "Levothyroxine absorption is inhibited by calcium supplements, milk, coffee, and dietary fiber; take on an empty stomach at least 30-60 mins before breakfast. "
            "Grapefruit inhibits CYP3A4, elevating statin systemic blood levels and muscle toxicity risk."
        ),
    },
    {
        "id": "nutr_004",
        "title": "AHA Cardiovascular & Hydration Guidelines",
        "source": "American Heart Association (AHA)",
        "content": (
            "Adequate daily fluid intake (approx 35 mL per kg of body weight) supports vascular compliance, renal solute clearance, and electrolyte homeostasis. "
            "In patients with elevated serum uric acid or creatinine, maintaining consistent daily fluid intake promotes urinary excretion of uric acid crystals."
        ),
    },
]


def get_nutrition_corpus_docs() -> List[Dict[str, str]]:
    return NUTRITION_CORPUS_DOCUMENTS
