# --------------------------------------------------
# File: seed.py
# Purpose: Comprehensive seed data for HealthLens AI platform.
#          Ensures all features (Dashboard, Prescriptions, Trends, Clinical Summary,
#          Nutrition, Lifestyle, Chat) work out-of-the-box on clean deployments.
# Module: Core Database Infrastructure
# --------------------------------------------------

import json
from datetime import datetime, timezone, timedelta
from sqlmodel import Session, select
from backend.app.core.logging import logger
from backend.app.models.user import User
from backend.app.models.report import Report
from backend.app.models.extracted_value import ExtractedValue
from backend.app.models.risk_analysis import RiskAnalysis
from backend.app.models.recommendation import Recommendation
from backend.app.models.doctor_question import DoctorQuestion
from backend.app.models.prescription import Prescription
from backend.app.models.prescription_medicine import PrescriptionMedicine
from backend.app.models.medicine_interaction import MedicineInteraction
from backend.app.models.historical_report import HistoricalReport
from backend.app.models.historical_parameter import HistoricalParameter
from backend.app.models.timeline_event import TimelineEvent, TimelineEventType
from backend.app.models.trend import TrendSnapshot
from backend.app.notes.models import ClinicalNote, NoteType


def seed_database_if_empty(session: Session) -> None:
    """
    Checks if seed data exists; if the database is clean, provisions complete
    realistic patient data so every feature renders fully on first launch.
    """
    try:
        existing_user = session.exec(select(User).where(User.id == 1)).first()
        existing_report = session.exec(select(Report).where(Report.id == 1)).first()

        if existing_user and existing_report:
            logger.info("Seed data already present. Skipping initialization.")
            return

        logger.info("Database is empty or missing baseline seed data. Initializing demo dataset...")

        now = datetime.now(timezone.utc)
        three_months_ago = now - timedelta(days=90)
        six_months_ago = now - timedelta(days=180)

        # -------------------------------------------------------------
        # 1. Primary Patient User
        # -------------------------------------------------------------
        if not existing_user:
            user = User(
                id=1,
                name="John Doe",
                email="john.doe@healthlens.ai",
                age=38,
                gender="male",
                pregnant=False,
                preferred_language="en",
                created_at=six_months_ago,
            )
            session.add(user)
            session.commit()
            session.refresh(user)
        else:
            user = existing_user

        # -------------------------------------------------------------
        # 2. Report #1: Comprehensive Metabolic & CBC Report
        # -------------------------------------------------------------
        if not existing_report:
            report = Report(
                id=1,
                user_id=user.id,
                doc_type="lab_report",
                source_filename="metropolis_comprehensive_blood_report.pdf",
                extraction_method_used="TieredOCR (TextDocxProvider + PyMuPDF)",
                status="completed",
                uploaded_at=now,
            )
            session.add(report)
            session.commit()
            session.refresh(report)

            # -------------------------------------------------------------
            # 3. Extracted Biomarker Values for Report #1
            # -------------------------------------------------------------
            biomarkers = [
                ExtractedValue(
                    report_id=report.id,
                    parameter_canonical_name="Hemoglobin",
                    raw_value=11.2,
                    unit="g/dL",
                    normal_range_low=13.8,
                    normal_range_high=17.2,
                    severity="mild",
                    is_critical=False,
                ),
                ExtractedValue(
                    report_id=report.id,
                    parameter_canonical_name="Fasting Blood Sugar",
                    raw_value=128.0,
                    unit="mg/dL",
                    normal_range_low=70.0,
                    normal_range_high=99.0,
                    severity="moderate",
                    is_critical=False,
                ),
                ExtractedValue(
                    report_id=report.id,
                    parameter_canonical_name="HbA1c",
                    raw_value=6.8,
                    unit="%",
                    normal_range_low=4.0,
                    normal_range_high=5.6,
                    severity="moderate",
                    is_critical=False,
                ),
                ExtractedValue(
                    report_id=report.id,
                    parameter_canonical_name="Total Cholesterol",
                    raw_value=245.0,
                    unit="mg/dL",
                    normal_range_low=125.0,
                    normal_range_high=200.0,
                    severity="moderate",
                    is_critical=False,
                ),
                ExtractedValue(
                    report_id=report.id,
                    parameter_canonical_name="Triglycerides",
                    raw_value=195.0,
                    unit="mg/dL",
                    normal_range_low=50.0,
                    normal_range_high=150.0,
                    severity="moderate",
                    is_critical=False,
                ),
                ExtractedValue(
                    report_id=report.id,
                    parameter_canonical_name="HDL Cholesterol",
                    raw_value=38.0,
                    unit="mg/dL",
                    normal_range_low=40.0,
                    normal_range_high=60.0,
                    severity="mild",
                    is_critical=False,
                ),
                ExtractedValue(
                    report_id=report.id,
                    parameter_canonical_name="LDL Cholesterol",
                    raw_value=168.0,
                    unit="mg/dL",
                    normal_range_low=50.0,
                    normal_range_high=100.0,
                    severity="moderate",
                    is_critical=False,
                ),
                ExtractedValue(
                    report_id=report.id,
                    parameter_canonical_name="Serum Creatinine",
                    raw_value=0.95,
                    unit="mg/dL",
                    normal_range_low=0.7,
                    normal_range_high=1.3,
                    severity="normal",
                    is_critical=False,
                ),
                ExtractedValue(
                    report_id=report.id,
                    parameter_canonical_name="Serum Calcium",
                    raw_value=7.8,
                    unit="mg/dL",
                    normal_range_low=8.5,
                    normal_range_high=10.2,
                    severity="mild",
                    is_critical=False,
                ),
                ExtractedValue(
                    report_id=report.id,
                    parameter_canonical_name="Vitamin D (25-OH)",
                    raw_value=14.2,
                    unit="ng/mL",
                    normal_range_low=30.0,
                    normal_range_high=100.0,
                    severity="moderate",
                    is_critical=False,
                ),
                ExtractedValue(
                    report_id=report.id,
                    parameter_canonical_name="Platelet Count",
                    raw_value=240000.0,
                    unit="/mcL",
                    normal_range_low=150000.0,
                    normal_range_high=450000.0,
                    severity="normal",
                    is_critical=False,
                ),
                ExtractedValue(
                    report_id=report.id,
                    parameter_canonical_name="WBC Count",
                    raw_value=7400.0,
                    unit="/mcL",
                    normal_range_low=4000.0,
                    normal_range_high=11000.0,
                    severity="normal",
                    is_critical=False,
                ),
            ]
            for bm in biomarkers:
                session.add(bm)

            # -------------------------------------------------------------
            # 4. Risk Analysis & Detected Patterns for Report #1
            # -------------------------------------------------------------
            detected_patterns = [
                {
                    "pattern_name": "Mild Microcytic Anemia",
                    "confidence": "high",
                    "triggered_by": ["Hemoglobin"],
                    "summary": "Hemoglobin 11.2 g/dL indicates mild iron-deficiency anemia.",
                },
                {
                    "pattern_name": "Impaired Fasting Glucose Pattern",
                    "confidence": "high",
                    "triggered_by": ["Fasting Blood Sugar", "HbA1c"],
                    "summary": "Elevated fasting blood sugar (128 mg/dL) and HbA1c (6.8%) indicate prediabetic glycemic stress.",
                },
                {
                    "pattern_name": "Atherogenic Dyslipidemia Pattern",
                    "confidence": "high",
                    "triggered_by": ["Total Cholesterol", "LDL Cholesterol", "Triglycerides"],
                    "summary": "Elevated LDL (168 mg/dL) and triglycerides (195 mg/dL) with borderline low HDL (38 mg/dL).",
                },
                {
                    "pattern_name": "Hypovitaminosis D",
                    "confidence": "high",
                    "triggered_by": ["Vitamin D (25-OH)"],
                    "summary": "Low 25-hydroxy vitamin D level (14.2 ng/mL) requires dietary supplementation.",
                },
            ]

            risk_analysis = RiskAnalysis(
                report_id=report.id,
                health_score=74,
                detected_patterns=json.dumps(detected_patterns),
                summary_text_en=(
                    "Overall Health Score is 74/100. Patient exhibits borderline glycemic stress (FBS 128 mg/dL, HbA1c 6.8%), "
                    "atherogenic dyslipidemia (Total Chol 245 mg/dL, LDL 168 mg/dL), mild anemia (Hb 11.2 g/dL), and low Vitamin D. "
                    "Renal function and complete blood counts are otherwise stable."
                ),
                summary_text_hi="समग्र स्वास्थ्य स्कोर 74/100 है। ग्लूकोज और कोलेस्ट्रॉल में हल्का विचलन देखा गया है।",
            )
            session.add(risk_analysis)

            # -------------------------------------------------------------
            # 5. Recommendations & Plain-Language Explanations
            # -------------------------------------------------------------
            eli10 = (
                "Think of Hemoglobin as tiny delivery trucks carrying oxygen to your muscles; right now you have slightly "
                "fewer trucks than normal. Fasting blood sugar means your body has extra sugar energy waiting in the bloodstream "
                "after overnight rest. Cholesterol is like soft wax that helps build cells; when you have extra wax, healthy fats "
                "and fiber help keep your blood pipes clean and clear."
            )

            diet_plan = {
                "breakfast": "Steel-cut oatmeal with chia seeds, walnuts, and cinnamon (soluble fiber to stabilize glucose).",
                "lunch": "Grilled lentils/chickpeas with spinach and lemon squeeze (Vitamin C enhances plant iron absorption).",
                "dinner": "Steamed vegetables with baked salmon or tofu and quinoa (Omega-3 fatty acids for lipid control).",
                "hydration": "2.5 to 3.0 Liters daily. Limit sugary beverages and sodas.",
            }

            exercise_plan = {
                "cardio": "30 minutes of brisk walking 5 days per week (150 mins total).",
                "post_meal": "10-minute light stroll within 30 minutes after dinner to reduce glycemic spike.",
                "strength": "Bodyweight or light resistance training twice a week.",
            }

            evidence_sources = [
                "WHO Guidelines on Nutritional Anemias (2020)",
                "ADA Standards of Medical Care in Diabetes (2024)",
                "ACC/AHA Guideline on the Management of Blood Cholesterol",
            ]

            limitations = [
                "This algorithmic assessment is strictly informational and does not constitute a formal diagnosis.",
                "Review all dietary and lifestyle adjustments with your primary care physician.",
            ]

            recommendation = Recommendation(
                report_id=report.id,
                explanation_json=json.dumps({"summary": "Metabolic & Lipid Optimization Protocol"}),
                eli10_json=json.dumps({"explanation": eli10}),
                diet_plan_json=json.dumps(diet_plan),
                exercise_json=json.dumps(exercise_plan),
                evidence_sources=json.dumps(evidence_sources),
                limitations_json=json.dumps(limitations),
                generated_at=now,
            )
            session.add(recommendation)

            # -------------------------------------------------------------
            # 6. Doctor Questions
            # -------------------------------------------------------------
            questions = [
                {
                    "question_text": "Should I undergo additional testing for iron deficiency (such as Serum Ferritin or TIBC)?",
                    "target_parameter": "Hemoglobin",
                    "clinical_rationale": "Differentiates nutritional iron deficiency from chronic microcytic traits.",
                    "priority": "HIGH",
                },
                {
                    "question_text": "Would a repeat HbA1c test in 12 weeks be appropriate to evaluate glycemic trajectory?",
                    "target_parameter": "Fasting Blood Sugar",
                    "clinical_rationale": "Assesses response to dietary interventions and Metformin therapy.",
                    "priority": "HIGH",
                },
                {
                    "question_text": "Should we consider a Vitamin D3 therapeutic replenishment protocol (e.g. 60,000 IU weekly)?",
                    "target_parameter": "Vitamin D (25-OH)",
                    "clinical_rationale": "Corrects moderate deficiency (14.2 ng/mL) to support calcium homeostasis.",
                    "priority": "MEDIUM",
                },
            ]
            doctor_q = DoctorQuestion(
                report_id=report.id,
                questions_json=json.dumps(questions),
                generated_at=now,
            )
            session.add(doctor_q)

            # -------------------------------------------------------------
            # 7. Prescription #1 with Complete Medicine Intelligence
            # -------------------------------------------------------------
            rx = Prescription(
                id=1,
                report_id=report.id,
                medicine_name_raw="Glycomet 500mg, Lipitor 20mg, Ecosprin 75mg, Brufen 400mg, Pan-D",
                generic_name="Metformin, Atorvastatin, Aspirin, Ibuprofen, Pantoprazole",
                active_ingredient="Metformin HCl, Atorvastatin Ca, Acetylsalicylic Acid, Ibuprofen, Pantoprazole + Domperidone",
                dosage="As prescribed",
                frequency="BD",
                duration="30 days",
            )
            session.add(rx)
            session.commit()
            session.refresh(rx)

            medicines = [
                PrescriptionMedicine(
                    prescription_id=rx.id,
                    medicine_name_raw="Tab. Glycomet 500mg",
                    brand_name="Glycomet",
                    generic_name="Metformin",
                    active_ingredient="Metformin Hydrochloride",
                    dosage="500mg",
                    frequency_code="BD",
                    times_per_day=2,
                    timing_slots="Morning, Night",
                    relation_to_food="with_food",
                    purpose="Type 2 diabetes glycemic regulation & insulin sensitivity",
                    drug_class="Biguanide",
                    category="Antidiabetic",
                    ocr_confidence=0.98,
                    resolution_confidence=0.99,
                    knowledge_confidence=0.98,
                ),
                PrescriptionMedicine(
                    prescription_id=rx.id,
                    medicine_name_raw="Tab. Lipitor 20mg",
                    brand_name="Lipitor",
                    generic_name="Atorvastatin",
                    active_ingredient="Atorvastatin Calcium",
                    dosage="20mg",
                    frequency_code="OD",
                    times_per_day=1,
                    timing_slots="Night",
                    relation_to_food="after_food",
                    purpose="Cardiovascular LDL cholesterol reduction & plaque stabilization",
                    drug_class="HMG-CoA Reductase Inhibitor",
                    category="Statin / Lipid Regulating",
                    ocr_confidence=0.99,
                    resolution_confidence=0.99,
                    knowledge_confidence=0.99,
                ),
                PrescriptionMedicine(
                    prescription_id=rx.id,
                    medicine_name_raw="Tab. Ecosprin 75mg",
                    brand_name="Ecosprin",
                    generic_name="Aspirin",
                    active_ingredient="Acetylsalicylic Acid",
                    dosage="75mg",
                    frequency_code="OD",
                    times_per_day=1,
                    timing_slots="Morning",
                    relation_to_food="after_food",
                    purpose="Cardioprotective antiplatelet prophylaxis",
                    drug_class="Antiplatelet / Salicylate",
                    category="Cardiovascular",
                    ocr_confidence=0.97,
                    resolution_confidence=0.98,
                    knowledge_confidence=0.98,
                ),
                PrescriptionMedicine(
                    prescription_id=rx.id,
                    medicine_name_raw="Tab. Brufen 400mg",
                    brand_name="Brufen",
                    generic_name="Ibuprofen",
                    active_ingredient="Ibuprofen",
                    dosage="400mg",
                    frequency_code="SOS",
                    times_per_day=1,
                    timing_slots="Afternoon",
                    relation_to_food="after_food",
                    purpose="Analgesic / anti-inflammatory for joint discomfort",
                    drug_class="NSAID",
                    category="Analgesic",
                    ocr_confidence=0.95,
                    resolution_confidence=0.96,
                    knowledge_confidence=0.95,
                ),
                PrescriptionMedicine(
                    prescription_id=rx.id,
                    medicine_name_raw="Cap. Pan-D",
                    brand_name="Pan-D",
                    generic_name="Pantoprazole + Domperidone",
                    active_ingredient="Pantoprazole 40mg + Domperidone 30mg",
                    dosage="1 Capsule",
                    frequency_code="OD",
                    times_per_day=1,
                    timing_slots="Morning",
                    relation_to_food="before_food",
                    purpose="Gastric acid suppression & gastrointestinal mucosal protection",
                    drug_class="Proton Pump Inhibitor + Prokinetic",
                    category="Gastrointestinal",
                    ocr_confidence=0.96,
                    resolution_confidence=0.97,
                    knowledge_confidence=0.96,
                ),
            ]
            for m in medicines:
                session.add(m)

            # Safety Interactions (Aspirin + Ibuprofen HIGH severity alert!)
            interactions = [
                MedicineInteraction(
                    prescription_id=rx.id,
                    drug_a="Aspirin",
                    drug_b="Ibuprofen",
                    severity="HIGH",
                    interaction_type="drug_drug",
                    title="NSAID Co-Administration & Antiplatelet Antagonism",
                    description=(
                        "Ibuprofen competitively inhibits the irreversible antiplatelet effect of low-dose Aspirin, "
                        "reducing cardiovascular protection while substantially elevating gastric mucosal irritation and bleeding risk."
                    ),
                    recommendation="Avoid taking Ibuprofen simultaneously with Aspirin. Consult physician regarding non-NSAID alternatives (e.g. Paracetamol).",
                    evidence_source="FDA Drug Safety Communication / WHO Essential Medicines",
                ),
                MedicineInteraction(
                    prescription_id=rx.id,
                    drug_a="Atorvastatin",
                    drug_b="Grapefruit / Dietary",
                    severity="MEDIUM",
                    interaction_type="food",
                    title="CYP3A4 Metabolic Dietary Precaution",
                    description="Excessive consumption of grapefruit or grapefruit juice inhibits CYP3A4 enzymes, raising systemic Atorvastatin exposure.",
                    recommendation="Avoid large quantities of grapefruit juice while on Atorvastatin therapy.",
                    evidence_source="Clinical Pharmacology Database",
                ),
            ]
            for inter in interactions:
                session.add(inter)

            # -------------------------------------------------------------
            # 8. Longitudinal Health History (3 sequential quarterly reports)
            # -------------------------------------------------------------
            hist_reports = [
                HistoricalReport(
                    report_id=report.id,
                    user_id=user.id,
                    source_filename="metropolis_comprehensive_blood_report.pdf",
                    doc_type="lab_report",
                    collection_date=now,
                    health_score=74.0,
                    total_parameters=12,
                    abnormal_parameters_count=5,
                    critical_alerts_count=0,
                    created_at=now,
                ),
                HistoricalReport(
                    report_id=report.id,
                    user_id=user.id,
                    source_filename="quarterly_checkup_jul2026.pdf",
                    doc_type="lab_report",
                    collection_date=three_months_ago,
                    health_score=68.0,
                    total_parameters=12,
                    abnormal_parameters_count=7,
                    critical_alerts_count=0,
                    created_at=three_months_ago,
                ),
                HistoricalReport(
                    report_id=report.id,
                    user_id=user.id,
                    source_filename="baseline_health_screening_apr2026.pdf",
                    doc_type="lab_report",
                    collection_date=six_months_ago,
                    health_score=62.0,
                    total_parameters=12,
                    abnormal_parameters_count=8,
                    critical_alerts_count=1,
                    created_at=six_months_ago,
                ),
            ]
            for hr in hist_reports:
                session.add(hr)

            # Sequential Historical Parameter points showing positive trend
            trend_parameters = [
                # Fasting Blood Sugar: 142 -> 136 -> 128 (Improving)
                ("Fasting Blood Sugar", 142.0, "mg/dL", "improving", six_months_ago),
                ("Fasting Blood Sugar", 136.0, "mg/dL", "improving", three_months_ago),
                ("Fasting Blood Sugar", 128.0, "mg/dL", "improving", now),
                # Hemoglobin: 10.4 -> 10.8 -> 11.2 (Improving)
                ("Hemoglobin", 10.4, "g/dL", "improving", six_months_ago),
                ("Hemoglobin", 10.8, "g/dL", "improving", three_months_ago),
                ("Hemoglobin", 11.2, "g/dL", "improving", now),
                # Total Cholesterol: 275 -> 260 -> 245 (Improving)
                ("Total Cholesterol", 275.0, "mg/dL", "improving", six_months_ago),
                ("Total Cholesterol", 260.0, "mg/dL", "improving", three_months_ago),
                ("Total Cholesterol", 245.0, "mg/dL", "improving", now),
                # HbA1c: 7.4 -> 7.1 -> 6.8 (Improving)
                ("HbA1c", 7.4, "%", "improving", six_months_ago),
                ("HbA1c", 7.1, "%", "improving", three_months_ago),
                ("HbA1c", 6.8, "%", "improving", now),
            ]

            for param_name, val, unit, direction, dt in trend_parameters:
                hp = HistoricalParameter(
                    report_id=report.id,
                    user_id=user.id,
                    canonical_name=param_name,
                    raw_name=param_name,
                    value=val,
                    unit=unit,
                    severity="moderate" if val > 120 or val < 11.5 else "mild",
                    collection_date=dt,
                )
                session.add(hp)

                ts = TrendSnapshot(
                    user_id=user.id,
                    parameter_canonical_name=param_name,
                    report_date=dt,
                    value=val,
                    unit=unit,
                    direction=direction,
                    magnitude=val,
                    rate_of_change=-4.2 if direction == "improving" and "Sugar" in param_name else 3.7,
                    confidence="HIGH",
                )
                session.add(ts)

            # -------------------------------------------------------------
            # 9. Chronological Timeline Events
            # -------------------------------------------------------------
            timeline_events = [
                TimelineEvent(
                    user_id=user.id,
                    report_id=report.id,
                    event_type=TimelineEventType.HEALTH_SCORE_CHANGED,
                    title="Health Score Improved to 74",
                    description="Your overall health score improved from 68 to 74 following dietary adjustments and Metformin therapy.",
                    event_date=now,
                    severity_level="SUCCESS",
                    icon_hint="trending-up",
                ),
                TimelineEvent(
                    user_id=user.id,
                    report_id=report.id,
                    event_type=TimelineEventType.ALERT_RESOLVED,
                    title="Critical Alert Resolved",
                    description="Serum fasting glucose dropped below acute threshold with zero critical flags on this panel.",
                    event_date=now - timedelta(days=2),
                    severity_level="SUCCESS",
                    icon_hint="check-circle",
                ),
                TimelineEvent(
                    user_id=user.id,
                    report_id=report.id,
                    event_type=TimelineEventType.PRESCRIPTION_UPDATED,
                    title="Cardiometabolic Medications Prescribed",
                    description="Dr. R. Sharma prescribed Glycomet 500mg BID and Lipitor 20mg HS. Added warning against Ibuprofen co-use.",
                    event_date=now - timedelta(days=5),
                    severity_level="INFO",
                    icon_hint="pill",
                ),
                TimelineEvent(
                    user_id=user.id,
                    report_id=report.id,
                    event_type=TimelineEventType.PATTERN_DETECTED,
                    title="Prediabetic & Lipid Trajectory Monitored",
                    description="Longitudinal analysis confirms consistent downward trend in fasting blood glucose (-14 mg/dL over 6 months).",
                    event_date=three_months_ago,
                    severity_level="WARNING",
                    icon_hint="activity",
                ),
                TimelineEvent(
                    user_id=user.id,
                    report_id=report.id,
                    event_type=TimelineEventType.UPLOAD,
                    title="Baseline Clinical Panel Ingested",
                    description="First digital health record created with 12 lab parameters standardized.",
                    event_date=six_months_ago,
                    severity_level="INFO",
                    icon_hint="file-text",
                ),
            ]
            for ev in timeline_events:
                session.add(ev)

            # -------------------------------------------------------------
            # 10. Clinical Doctor Notes
            # -------------------------------------------------------------
            clinical_notes = [
                ClinicalNote(
                    report_id=report.id,
                    user_id=user.id,
                    author_name="Dr. R. Sharma, MD",
                    author_role="Consultant Physician / Internist",
                    note_type=NoteType.VISIT_SUMMARY,
                    content=(
                        "Patient John Doe (38M) evaluated for routine quarterly follow-up. Demonstrating excellent adherence "
                        "to low-glycemic dietary modifications. HbA1c reduced from 7.4% to 6.8%. Fasting glucose is down to 128 mg/dL. "
                        "Cautioned against concurrent use of over-the-counter Ibuprofen with daily cardioprotective Aspirin due to antiplatelet antagonism. "
                        "Repeat complete metabolic panel in 12 weeks."
                    ),
                    created_at=now - timedelta(days=3),
                ),
                ClinicalNote(
                    report_id=report.id,
                    user_id=user.id,
                    author_name="Dr. Priya Patel, RD",
                    author_role="Clinical Nutrition Specialist",
                    note_type=NoteType.CLINICAL_OBSERVATION,
                    content=(
                        "Reviewed patient 14-day continuous dietary log. Patient is incorporating soluble fiber (steel-cut oats, lentils, psyllium). "
                        "Recommended adding Vitamin C sources (citrus, bell peppers) alongside iron-rich plant meals to enhance non-heme iron uptake for mild anemia."
                    ),
                    created_at=now - timedelta(days=7),
                ),
            ]
            for note in clinical_notes:
                session.add(note)

            session.commit()
            logger.info("Successfully provisioned complete demo seed dataset into database.")

    except Exception as exc:
        logger.error(f"Error while seeding database: {exc}")
        session.rollback()
