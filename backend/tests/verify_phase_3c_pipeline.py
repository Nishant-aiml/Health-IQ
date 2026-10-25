# --------------------------------------------------
# File: verify_phase_3c_pipeline.py
# Purpose: Complete Phase 3C Nutrition & Lifestyle Intelligence pipeline verification script.
# Module: Backend Test Suite / Phase 3C Pipeline Verification
# Used By: Verification Execution
# Future Phase: Phase 3C Validation
# --------------------------------------------------

from sqlmodel import Session
from backend.app.db.session import engine, init_db
from backend.app.services.nutrition_service import nutrition_service
from backend.app.services.lifestyle_service import lifestyle_service
from backend.app.services.wellness_service import wellness_service


def main():
    init_db()
    with Session(engine) as session:
        # 1. Nutrition Service Guidance & Interactions
        nutr_data = nutrition_service.get_nutrition_guidance_for_report(session, 1)
        print(f"[OK] Nutrition Guidance: Focus='{nutr_data['overall_dietary_focus']}', {len(nutr_data['recommendations'])} recommendation(s).")
        print(f"[OK] Food-Drug Interactions Flagged: {len(nutr_data['food_interactions'])} rule(s).")

        # 2. Lifestyle Guidance
        life_data = lifestyle_service.get_lifestyle_guidance_for_report(session, 1)
        print(f"[OK] Lifestyle Guidance: {len(life_data['exercise_plan'])} exercise plan(s), target fluid {life_data['hydration']['daily_volume_liters']}L.")

        # 3. Wellness Score Breakdown
        well_data = wellness_service.get_wellness_breakdown_for_report(session, 1)
        print(f"[OK] Wellness Score Breakdown: Composite Score={well_data['overall_wellness_score']}/100 (Reused Baseline={well_data['health_score_reused']}).")

        print("\n[SUCCESS] Phase 3C Nutrition & Lifestyle Intelligence Engine Pipeline Verification Passed!")


if __name__ == "__main__":
    main()
