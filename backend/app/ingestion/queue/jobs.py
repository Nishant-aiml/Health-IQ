# --------------------------------------------------
# File: jobs.py
# Purpose: Individual document ingestion job task processor incorporating Phase 2B Analysis.
# Module: Ingestion Engine / Queue
# Used By: Worker Pool Consumer
# --------------------------------------------------

import json
from sqlmodel import Session
from backend.app.db.session import engine
from backend.app.models.job import Job
from backend.app.models.report import Report
from backend.app.models.extracted_value import ExtractedValue
from backend.app.models.risk_analysis import RiskAnalysis
from backend.app.models.user import User
from backend.app.ocr import tiered_ocr_pipeline
from backend.app.analysis.parser import normalize_report_data
from backend.app.analysis import (
    evaluate_parameter_severity,
    evaluate_critical_alerts,
    calculate_health_score,
    pattern_registry,
)
from backend.app.analysis.demographic_ranges import get_demographic_normal_range
from backend.app.ingestion.queue.states import JobStage, JobStatus
from backend.app.repositories.job_repository import job_repository
from backend.app.repositories.report_repository import report_repository
from backend.app.services.history_service import history_service
from backend.app.core.logging import logger


async def process_document_job(job_id: int, file_bytes: bytes, filename: str) -> bool:
    """
    Executes OCR extraction, parameter normalization, Phase 2B analysis, and history sync.

    Why it exists:
        Acts as worker task handler. Performs stage transitions (`extracting -> parsing -> analyzed -> completed`),
        creates `ExtractedValue` and `RiskAnalysis` DB records, and syncs history.
    """
    logger.info(f"Worker picking up Job #{job_id} for file '{filename}'...")

    with Session(engine) as session:
        job = job_repository.get_by_id(session, job_id)
        if not job:
            logger.error(f"Job #{job_id} not found in database.")
            return False

        # Stage 1: OCR Extraction
        job_repository.update_stage_and_status(session, job_id, JobStage.EXTRACTING, JobStatus.IN_PROGRESS)
        ocr_result = await tiered_ocr_pipeline.execute(file_bytes, filename)

        if not ocr_result.success:
            logger.error(f"Job #{job_id} OCR failed: {ocr_result.error_message}")
            job_repository.update_stage_and_status(
                session, job_id, JobStage.FAILED, JobStatus.FAILED, error_reason=ocr_result.error_message
            )
            report_repository.update_status(session, job.report_id, JobStage.FAILED)
            return False

        # Stage 2: Parsing & Canonical Normalization
        job_repository.update_stage_and_status(session, job_id, JobStage.PARSING, JobStatus.IN_PROGRESS)
        report = report_repository.get_by_id(session, job.report_id)
        report.extraction_method_used = ocr_result.provider_used
        session.add(report)
        session.commit()

        # Fetch demographic info
        user = session.get(User, report.user_id) if report else None
        age = user.age if user else 30
        gender = user.gender if user else "male"
        pregnant = user.pregnant if user else False

        normalized_items = normalize_report_data(ocr_result.extracted_text)

        # Stage 3: Phase 2B Deterministic Analysis
        job_repository.update_stage_and_status(session, job_id, "analyzed", JobStatus.IN_PROGRESS)
        
        extracted_param_map = {}
        processed_values_for_db = []

        for item in [i for i in normalized_items if i.get("is_valid", True)]:
            c_name = item["canonical_name"]
            val = item["value"]
            unit = item["unit"]
            low, high = get_demographic_normal_range(c_name, age=age, gender=gender, pregnant=pregnant)

            severity = evaluate_parameter_severity(c_name, val, low, high)

            param_obj = {
                "raw_name": c_name,
                "canonical_name": c_name,
                "value": val,
                "unit": unit,
                "severity": severity,
                "normal_range_low": low,
                "normal_range_high": high,
                "is_critical": False,
            }
            extracted_param_map[c_name] = param_obj
            processed_values_for_db.append(param_obj)

        # Evaluate Critical Value Alerts
        critical_alert_objects = evaluate_critical_alerts(processed_values_for_db)
        critical_param_names = {alert["parameter_name"] for alert in critical_alert_objects}

        for p_obj in processed_values_for_db:
            if p_obj["canonical_name"] in critical_param_names:
                p_obj["is_critical"] = True
                p_obj["severity"] = "critical"

        # Evaluate Rule-Based Patterns & Health Score
        detected_patterns = pattern_registry.evaluate_all(extracted_param_map)
        score_result = calculate_health_score(processed_values_for_db)

        # Persist ExtractedValue rows
        for p_obj in processed_values_for_db:
            extracted_val = ExtractedValue(
                report_id=report.id,
                parameter_canonical_name=p_obj["canonical_name"],
                raw_value=p_obj["value"],
                unit=p_obj["unit"],
                normal_range_low=p_obj["normal_range_low"],
                normal_range_high=p_obj["normal_range_high"],
                severity=p_obj["severity"],
                is_critical=p_obj["is_critical"],
            )
            session.add(extracted_val)

        # Persist RiskAnalysis entity
        risk_analysis = RiskAnalysis(
            report_id=report.id,
            health_score=score_result["score"],
            detected_patterns=json.dumps(detected_patterns),
            summary_text_en=score_result["summary"],
        )
        session.add(risk_analysis)

        # Complete Job & Report Stage
        job_repository.update_stage_and_status(session, job_id, JobStage.COMPLETED, JobStatus.COMPLETED)
        report_repository.update_status(session, report.id, JobStage.COMPLETED)
        session.commit()

        # Sync to Longitudinal History Engine
        try:
            history_service.sync_report_to_history(
                session,
                report.id,
                {
                    "health_score": score_result["score"],
                    "extracted_values": processed_values_for_db,
                    "abnormal_parameters": [p for p in processed_values_for_db if p.get("severity") != "NORMAL"],
                    "critical_alerts": critical_alert_objects,
                }
            )
        except Exception as e:
            logger.warning(f"History sync note for Report #{report.id}: {e}")

        logger.info(f"Job #{job_id} Phase 2B Analysis completed successfully. Score: {score_result['score']}.")
        return True
