# --------------------------------------------------
# File: rules.py
# Purpose: Clinical rules database for Food-Medicine interactions and timing advice.
# Module: Food-Medicine Interaction Engine / Rules
# Used By: Interaction Checker
# Future Phase: Phase 3C Nutrition & Lifestyle Intelligence
# --------------------------------------------------

from typing import List
from backend.app.nutrition.interactions.models import FoodMedicineInteraction, InteractionSeverity


CLINICAL_FOOD_DRUG_RULES: List[FoodMedicineInteraction] = [
    FoodMedicineInteraction(
        drug_name="Warfarin",
        interacting_food_or_substance="Vitamin K-rich Foods (Spinach, Kale, Broccoli, Brussels Sprouts)",
        severity=InteractionSeverity.HIGH,
        mechanism_and_reason="Vitamin K promotes blood clotting factor synthesis, antagonizing the anticoagulant action of Warfarin.",
        actionable_timing_guidance="Maintain a strictly consistent daily intake of green leafy vegetables. Do not suddenly double or stop your green vegetable intake without consulting your physician.",
        evidence_level="FDA & WHO Anticoagulation Prescribing Guidelines",
    ),
    FoodMedicineInteraction(
        drug_name="Levothyroxine",
        interacting_food_or_substance="Calcium Supplements, Dairy, Coffee & High Fiber Foods",
        severity=InteractionSeverity.HIGH,
        mechanism_and_reason="Calcium and dietary fiber bind to Levothyroxine in the gut, reducing oral bioavailability by up to 40%.",
        actionable_timing_guidance="Take Levothyroxine on an empty stomach with plain water at least 30-60 minutes before breakfast, espresso, or calcium/dairy consumption.",
        evidence_level="American Thyroid Association Clinical Practice Guidelines",
    ),
    FoodMedicineInteraction(
        drug_name="Iron Supplements",
        interacting_food_or_substance="Tea, Coffee, Dairy & Calcium Supplements",
        severity=InteractionSeverity.MEDIUM,
        mechanism_and_reason="Tannins in tea/coffee and calcium ions bind to non-heme iron, inhibiting intestinal transport.",
        actionable_timing_guidance="Separate iron supplements from tea, coffee, and milk by at least 2 hours. Take iron with Vitamin C (citrus juice) to enhance absorption.",
        evidence_level="WHO Micronutrient Anemia Guidelines",
    ),
    FoodMedicineInteraction(
        drug_name="Metformin",
        interacting_food_or_substance="Alcohol & Long-term Vitamin B12 Depletion",
        severity=InteractionSeverity.MEDIUM,
        mechanism_and_reason="Metformin alters ileal membrane calcium-dependent B12 absorption; alcohol increases risk of lactic acidosis.",
        actionable_timing_guidance="Take Metformin with meals to minimize gastrointestinal discomfort. Avoid excessive alcohol and ask your doctor to check B12 levels annually.",
        evidence_level="ADA Standards of Medical Care in Diabetes",
    ),
    FoodMedicineInteraction(
        drug_name="Atorvastatin",
        interacting_food_or_substance="Grapefruit & Grapefruit Juice",
        severity=InteractionSeverity.HIGH,
        mechanism_and_reason="Furanocoumarins in grapefruit inhibit intestinal CYP3A4 enzymes, significantly elevating systemic drug levels and myopathy risk.",
        actionable_timing_guidance="Avoid consuming grapefruit or grapefruit juice while taking statins (Atorvastatin, Simvastatin).",
        evidence_level="FDA Clinical Pharmacology Warning",
    ),
    FoodMedicineInteraction(
        drug_name="Lisinopril",
        interacting_food_or_substance="High Potassium Foods & Salt Substitutes (Potassium Chloride)",
        severity=InteractionSeverity.MEDIUM,
        mechanism_and_reason="ACE inhibitors decrease aldosterone secretion, reducing renal potassium excretion and increasing hyperkalemia risk.",
        actionable_timing_guidance="Avoid potassium-based salt substitutes. Consume potassium-rich foods (bananas, coconut water) in moderate, consistent amounts.",
        evidence_level="AHA Clinical Hypertension Guidelines",
    ),
]
