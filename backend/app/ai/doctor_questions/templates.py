# --------------------------------------------------
# File: templates.py
# Purpose: Doctor discussion question templates mapped by canonical parameter and pattern.
# Module: AI Engine / Doctor Questions
# Used By: Doctor Questions Generator
# Future Phase: Phase 2C AI Recommendations
# --------------------------------------------------

DOCTOR_QUESTION_TEMPLATES = {
    "Hemoglobin": {
        "question": "Should I undergo additional testing for iron deficiency (such as Serum Ferritin or Total Iron Binding Capacity)?",
        "rationale": "Helps distinguish iron-deficiency anemia from other microcytic or chronic disease anemia causes.",
    },
    "Fasting Blood Sugar": {
        "question": "Would an HbA1c test or oral glucose tolerance test be recommended to evaluate long-term glycemic control?",
        "rationale": "HbA1c measures 3-month average glucose levels rather than single-moment fasting levels.",
    },
    "Serum Creatinine": {
        "question": "Should we monitor my estimated Glomerular Filtration Rate (eGFR) and check an ultrasound or urine protein test?",
        "rationale": "Evaluates kidney filtration performance and checks for early renal protein leakage.",
    },
    "Total Cholesterol": {
        "question": "Would a complete lipid profile (HDL, LDL, Triglycerides) help determine my cardiovascular risk score?",
        "rationale": "Total cholesterol alone does not differentiate protective HDL from atherogenic LDL particles.",
    },
    "Thyroid Stimulating Hormone": {
        "question": "Should we order a free T3 and free T4 panel to evaluate thyroid gland activity?",
        "rationale": "Clarifies whether pituitary TSH elevation reflects clinical or subclinical hypothyroidism.",
    },
}
