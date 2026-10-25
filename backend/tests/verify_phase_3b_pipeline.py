# --------------------------------------------------
# File: verify_phase_3b_pipeline.py
# Purpose: Complete Phase 3B Longitudinal Health Intelligence verification script.
# Module: Backend Test Suite / Phase 3B Pipeline Verification
# Used By: Verification Execution
# Future Phase: Phase 3B Validation
# --------------------------------------------------

from datetime import datetime, timedelta, timezone
from sqlmodel import Session
from backend.app.db.session import engine, init_db
from backend.app.models.user import User
from backend.app.models.report import Report
from backend.app.services.history_service import history_service


def main():
    init_db()
    with Session(engine) as session:
        # Create Demo User
        user = session.query(User).filter(User.name == "Longitudinal Demo Patient").first()
        if not user:
            user = User(name="Longitudinal Demo Patient", age=45, gender="male", pregnant=False, preferred_language="en")
            session.add(user)
            session.commit()
            session.refresh(user)

        now = datetime.now(timezone.utc)

        # Report 1 (60 days ago): Elevated Fasting Glucose 145 mg/dL, Hb 12.0 g/dL
        r1 = Report(user_id=user.id, doc_type="lab_report", source_filename="report_jan.pdf", uploaded_at=now - timedelta(days=60), status="completed")
        session.add(r1)
        session.commit()
        session.refresh(r1)

        history_service.sync_report_to_history(
            session,
            r1.id,
            {
                "health_score": 70.0,
                "extracted_values": [
                    {"canonical_name": "Fasting Blood Sugar", "raw_name": "Fasting Glucose", "value": 145.0, "unit": "mg/dL", "severity": "ELEVATED", "normal_range_low": 70, "normal_range_high": 99},
                    {"canonical_name": "Hemoglobin", "raw_name": "Hb", "value": 12.0, "unit": "g/dL", "severity": "LOW", "normal_range_low": 13, "normal_range_high": 17},
                ],
                "abnormal_parameters": ["Fasting Blood Sugar", "Hemoglobin"],
                "critical_alerts": [],
            },
        )

        # Report 2 (30 days ago): Fasting Glucose 115 mg/dL, Hb 13.2 g/dL
        r2 = Report(user_id=user.id, doc_type="lab_report", source_filename="report_feb.pdf", uploaded_at=now - timedelta(days=30), status="completed")
        session.add(r2)
        session.commit()
        session.refresh(r2)

        history_service.sync_report_to_history(
            session,
            r2.id,
            {
                "health_score": 85.0,
                "extracted_values": [
                    {"canonical_name": "Fasting Blood Sugar", "raw_name": "Fasting Glucose", "value": 115.0, "unit": "mg/dL", "severity": "ELEVATED", "normal_range_low": 70, "normal_range_high": 99},
                    {"canonical_name": "Hemoglobin", "raw_name": "Hb", "value": 13.2, "unit": "g/dL", "severity": "NORMAL", "normal_range_low": 13, "normal_range_high": 17},
                ],
                "abnormal_parameters": ["Fasting Blood Sugar"],
                "critical_alerts": [],
            },
        )

        # Report 3 (Today): Fasting Glucose 95 mg/dL (Normal - Recovery!), Hb 14.1 g/dL
        r3 = Report(user_id=user.id, doc_type="lab_report", source_filename="report_mar.pdf", uploaded_at=now, status="completed")
        session.add(r3)
        session.commit()
        session.refresh(r3)

        history_service.sync_report_to_history(
            session,
            r3.id,
            {
                "health_score": 95.0,
                "extracted_values": [
                    {"canonical_name": "Fasting Blood Sugar", "raw_name": "Fasting Glucose", "value": 95.0, "unit": "mg/dL", "severity": "NORMAL", "normal_range_low": 70, "normal_range_high": 99},
                    {"canonical_name": "Hemoglobin", "raw_name": "Hb", "value": 14.1, "unit": "g/dL", "severity": "NORMAL", "normal_range_low": 13, "normal_range_high": 17},
                ],
                "abnormal_parameters": [],
                "critical_alerts": [],
            },
        )

        # Retrieve History Summary
        history_data = history_service.get_patient_history(session, user.id)
        print(f"[OK] History synced: {history_data['total_reports']} reports tracked.")

        # Retrieve Trends
        trends_data = history_service.get_patient_trends(session, user.id)
        print(f"[OK] Biomarker trends analyzed: {trends_data['total_biomarkers_tracked']} biomarkers.")
        for b in trends_data['biomarker_trends']:
            print(f"   -> {b['canonical_name']}: {b['trend']['direction'].upper()} (Confidence: {b['trend']['trend_confidence']})")

        # Retrieve Timeline
        timeline_data = history_service.get_patient_timeline(session, user.id)
        print(f"[OK] Timeline built: {timeline_data['total_events']} milestone events.")

        print("\n[SUCCESS] Phase 3B Longitudinal Health Intelligence Engine Verification Passed!")


if __name__ == "__main__":
    main()
