# --------------------------------------------------
# File: prescription_service.py
# Purpose: Service orchestrator for processing prescription uploads, database persistence, and queries.
# Module: Prescription Services
# Used By: Prescriptions API Endpoint Controller
# Future Phase: Phase 3A Medicine Intelligence
# --------------------------------------------------

from typing import Dict, Any, List
from sqlmodel import Session, select
from backend.app.db.session import init_db
from backend.app.models.user import User
from backend.app.models.report import Report
from backend.app.models.prescription import Prescription
from backend.app.models.prescription_medicine import PrescriptionMedicine
from backend.app.models.medicine_interaction import MedicineInteraction
from backend.app.repositories.user_repository import user_repository
from backend.app.prescription.extractor import prescription_extractor
from backend.app.services.medicine_service import medicine_service
from backend.app.core.exceptions import NotFoundException, ValidationException
from backend.app.core.logging import logger


class PrescriptionService:
    """Service orchestrator for prescription document ingestion, database persistence, and analysis retrieval."""

    async def analyze_prescription(
        self,
        session: Session,
        file_bytes: bytes = None,
        filename: str = "prescription.pdf",
        pasted_text: str = None,
    ) -> Dict[str, Any]:
        # Ensure database tables exist
        init_db()

        # Ensure default user
        user = user_repository.get_by_name(session, "Demo Patient")
        if not user:
            user = User(name="Demo Patient", age=35, gender="male", pregnant=False, preferred_language="en")
            session.add(user)
            session.commit()
            session.refresh(user)

        # Step 1: Extract prescription text & medicine items
        if pasted_text and pasted_text.strip():
            raw_text = pasted_text.strip()
            ocr_method = "Copy-Pasted Text"
            from backend.app.prescription.parser import prescription_parser
            parsed_items = prescription_parser.parse_text(raw_text)
        elif file_bytes:
            extraction_res = await prescription_extractor.extract_prescription(file_bytes, filename)
            if not extraction_res.success or not extraction_res.items:
                raise ValidationException(extraction_res.error_message or "Could not extract medicines from prescription file.")
            raw_text = extraction_res.raw_ocr_text
            ocr_method = extraction_res.extraction_method
            parsed_items = extraction_res.items
        else:
            raise ValidationException("Either prescription file or pasted text must be provided.")

        raw_medicine_dicts = [item.model_dump() for item in parsed_items]
        analysis_res = medicine_service.analyze_medicines(raw_medicine_dicts, is_pregnant=user.pregnant)

        # Step 2: Create Report database record
        report = Report(
            user_id=user.id,
            doc_type="prescription",
            source_filename=filename,
            extraction_method_used=ocr_method,
            status="completed",
        )
        session.add(report)
        session.commit()
        session.refresh(report)

        # Step 3: Create Prescription database record
        prescription = Prescription(
            report_id=report.id,
            medicine_name_raw="Multiple Prescribed Medicines",
            dosage="As prescribed",
            frequency="OD",
            duration="7 days",
        )
        session.add(prescription)
        session.commit()
        session.refresh(prescription)

        # Step 4: Save Normalized PrescriptionMedicine database records
        for med in analysis_res["medicines"]:
            schedule = med["schedule"]
            pm = PrescriptionMedicine(
                prescription_id=prescription.id,
                medicine_name_raw=med["medicine_name_raw"],
                brand_name=med["brand_name"],
                generic_name=med["generic_name"],
                active_ingredient=med["active_ingredient"],
                dosage=med["dosage"],
                frequency_code=schedule["frequency_code"],
                times_per_day=schedule["times_per_day"],
                timing_slots=",".join([slot["slot_name"] for slot in schedule["timing_slots"] if slot["is_active"]]),
                relation_to_food=schedule["relation_to_food"],
                purpose=med["purpose"],
                drug_class=med["drug_class"],
                category=med["category"],
                ocr_confidence=med["ocr_confidence"],
                resolution_confidence=med["resolution_confidence"],
                knowledge_confidence=med["knowledge_confidence"],
            )
            session.add(pm)

        # Step 5: Save Normalized MedicineInteraction database records
        safety = analysis_res["safety_analysis"]
        for interaction in safety.get("interactions", []) + safety.get("duplicate_therapies", []):
            mi = MedicineInteraction(
                prescription_id=prescription.id,
                drug_a=interaction["drug_a"],
                drug_b=interaction.get("drug_b"),
                severity=interaction["severity"],
                interaction_type=interaction["interaction_type"],
                title=interaction["title"],
                description=interaction["description"],
                recommendation=interaction["recommendation"],
                evidence_source=interaction.get("evidence_source", "Clinical Guidelines"),
            )
            session.add(mi)

        session.commit()
        logger.info(f"Prescription #{prescription.id} saved with {len(analysis_res['medicines'])} medicines.")

        return {
            "prescription_id": prescription.id,
            "report_id": report.id,
            "source_filename": filename,
            "ocr_method": ocr_method,
            "medicines": analysis_res["medicines"],
            "safety_analysis": analysis_res["safety_analysis"],
        }

    def get_prescription_by_id(self, session: Session, prescription_id: int) -> Dict[str, Any]:
        init_db()
        prescription = session.get(Prescription, prescription_id)
        if not prescription:
            raise NotFoundException(f"Prescription #{prescription_id} not found.")

        # Fetch PrescriptionMedicines
        meds_stmt = select(PrescriptionMedicine).where(PrescriptionMedicine.prescription_id == prescription_id)
        pm_list = session.exec(meds_stmt).all()

        # Reconstruct structured response via MedicineService
        raw_medicine_dicts = [
            {
                "medicine_name_raw": pm.medicine_name_raw,
                "dosage": pm.dosage,
                "frequency_raw": pm.frequency_code,
                "food_instruction_raw": pm.relation_to_food,
            }
            for pm in pm_list
        ]

        analysis_res = medicine_service.analyze_medicines(raw_medicine_dicts)

        return {
            "prescription_id": prescription.id,
            "report_id": prescription.report_id,
            "source_filename": "prescription.pdf",
            "medicines": analysis_res["medicines"],
            "safety_analysis": analysis_res["safety_analysis"],
        }


prescription_service = PrescriptionService()
