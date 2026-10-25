# --------------------------------------------------
# File: contraindications.py
# Purpose: Physiological and disease contraindications lookup dictionary.
# Module: Medicine Knowledge / Contraindications
# Used By: Medicine Registry
# Future Phase: Phase 3A Medicine Intelligence
# --------------------------------------------------

CONTRAINDICATIONS = {
    "metformin": ["Severe Renal Impairment (eGFR < 30 mL/min)", "Acute Lactic Acidosis", "Severe Hepatic Failure"],
    "amoxicillin": ["Known Severe Hypersensitivity to Penicillins or Beta-Lactams", "Infectious Mononucleosis"],
    "atorvastatin": ["Active Liver Disease", "Unexplained Persistent Elevation of Serum Transaminases", "Pregnancy & Lactation"],
    "amlodipine": ["Severe Hypotension", "Cardiogenic Shock", "Severe Aortic Stenosis"],
    "pantoprazole": ["Hypersensitivity to substituted benzimidazoles", "Concurrent use with Rilpivirine"],
    "omeprazole": ["Hypersensitivity to Omeprazole", "Co-administration with nelfinavir or rilpivirine"],
    "azithromycin": ["History of Cholestatic Jaundice/Hepatic Dysfunction associated with prior Azithromycin use"],
    "telmisartan": ["Biliary Obstructive Disorders", "Severe Hepatic Impairment", "Concurrent Aliskiren in Diabetes"],
    "paracetamol": ["Severe Active Liver Failure or Hepatic Disease", "Severe Hypersensitivity"],
    "cetirizine": ["Severe End-Stage Renal Failure (CrCl < 10 mL/min)"],
    "levothyroxine": ["Uncorrected Adrenal Insufficiency", "Thyrotoxicosis", "Acute Myocardial Infarction"],
    "aspirin": ["Active Peptic Ulceration", "Bleeding Diathesis/Hemophilia", "Severe Renal or Hepatic Failure", "Children under 16 with Viral Fever (Reye Syndrome)"],
}
