# --------------------------------------------------
# File: pregnancy.py
# Purpose: Pregnancy and lactation safety classification dictionary.
# Module: Medicine Knowledge / Pregnancy
# Used By: Medicine Registry & Safety Rules Engine
# Future Phase: Phase 3A Medicine Intelligence
# --------------------------------------------------

PREGNANCY_CATEGORIES = {
    "metformin": {"category": "B", "note": "Crosses placenta. Generally considered safe under physician supervision for gestational diabetes."},
    "amoxicillin": {"category": "B", "note": "Widely used and considered safe during pregnancy when indicated."},
    "atorvastatin": {"category": "X", "note": "CONTRAINDICATED in pregnancy due to potential fetal harm in cholesterol biosynthesis."},
    "amlodipine": {"category": "C", "note": "Use only if potential benefit justifies potential risk to fetus."},
    "pantoprazole": {"category": "B", "note": "No evidence of risk in animal studies; use if clinically indicated."},
    "omeprazole": {"category": "C", "note": "Use if benefits outweigh risks. Consult obstetrician."},
    "azithromycin": {"category": "B", "note": "Animal reproduction studies show no evidence of impaired fertility or harm to fetus."},
    "telmisartan": {"category": "D", "note": "CONTRAINDICATED in 2nd and 3rd trimesters. Can cause serious fetal renal failure and injury."},
    "paracetamol": {"category": "B", "note": "First-line pain reliever during pregnancy at lowest effective dose for shortest duration."},
    "cetirizine": {"category": "B", "note": "Low risk during pregnancy; consult doctor before starting."},
    "levothyroxine": {"category": "A", "note": "Essential replacement therapy. Dose requirements often INCREASE during pregnancy."},
    "aspirin": {"category": "D", "note": "Avoid full doses during 3rd trimester (may cause premature closure of ductus arteriosus). Low-dose (75mg) may be prescribed for preeclampsia prevention under strict doctor care."},
}
