# --------------------------------------------------
# File: medicine_service.py
# Purpose: Service orchestrator for medicine resolution, schedule parsing, safety checks, and AI explanations.
# Module: Medicine Services
# Used By: Prescription Service & API Controllers
# Future Phase: Phase 3A Medicine Intelligence
# --------------------------------------------------

from typing import List, Dict, Any
from backend.app.medicine.registry import medicine_registry
from backend.app.medicine.schedule.parser import schedule_parser
from backend.app.medicine.interactions.registry import interaction_registry
from backend.app.medicine.explainer.engine import medicine_explainer_engine
from backend.app.rag.retrieval import hybrid_retriever
from backend.app.core.logging import logger


class MedicineService:
    """Service orchestrator for medicine resolution, schedule parsing, safety rules, and AI RAG explanations."""

    def analyze_medicines(self, raw_medicine_names: List[Dict[str, str]], is_pregnant: bool = False) -> Dict[str, Any]:
        resolved_medicines = []
        generic_keys = []

        for item in raw_medicine_names:
            raw_name = item.get("medicine_name_raw") or item.get("name", "Unknown Medicine")
            raw_freq = item.get("frequency_raw") or item.get("frequency", "OD")
            raw_food = item.get("food_instruction_raw") or item.get("food_instruction", "PC")
            raw_dosage = item.get("dosage", "As prescribed")
            raw_duration = item.get("duration", "7 days")

            # Stage 1: Resolution Pipeline (Brand -> Generic -> Active Ingredient -> Knowledge Base)
            info = medicine_registry.resolve_medicine(raw_name)
            generic_keys.append(info.generic_name)

            # Stage 2: Schedule Parsing (OD, BD, TDS, HS, SOS -> Data-driven TimeSlots)
            schedule = schedule_parser.parse_schedule(raw_freq, raw_food=raw_food, duration=raw_duration)

            # Stage 3: Medicine Explanation & ELI10 Engine
            explainer_res = medicine_explainer_engine.explain_medicine(info)

            # Stage 4: Hybrid RAG Search for Evidence Citations
            query = f"{info.generic_name} {info.purpose} precautions mechanism"
            retrieval_res = hybrid_retriever.retrieve(query, top_k=2)

            evidence_citations = [
                {
                    "citation_id": f"cit_{idx+1}",
                    "source_organization": getattr(chunk, "source_name", "WHO / Clinical Guidelines"),
                    "title": getattr(chunk, "title", f"Drug Reference: {info.generic_name}"),
                    "medical_topic": getattr(chunk, "medical_topic", info.generic_name),
                    "excerpt": getattr(chunk, "chunk_text", ""),
                    "relevance_score": round(float(getattr(chunk, "rrf_score", 0.9)), 3),
                }
                for idx, chunk in enumerate(retrieval_res.retrieved_chunks)
            ]

            medicine_payload = {
                "medicine_name_raw": raw_name,
                "brand_name": info.brand_name,
                "generic_name": info.generic_name,
                "active_ingredient": info.active_ingredient,
                "drug_class": info.drug_class,
                "category": info.category,
                "dosage": raw_dosage,
                "purpose": info.purpose,
                "mechanism": info.mechanism,
                "schedule": schedule.model_dump(),
                "side_effects": info.side_effects,
                "contraindications": info.contraindications,
                "food_warnings": info.food_warnings,
                "driving_warning": info.driving_warning,
                "pregnancy_warning": info.pregnancy_warning,
                "pregnancy_category": info.pregnancy_category,
                "storage": info.storage,
                "explanation": explainer_res["explanation"],
                "eli10": explainer_res["eli10"],
                "disclaimer": explainer_res["disclaimer"],
                "evidence": evidence_citations,
                "ocr_confidence": info.ocr_confidence,
                "resolution_confidence": info.resolution_confidence,
                "knowledge_confidence": info.knowledge_confidence,
                "is_unknown": info.is_unknown,
                "possible_matches": info.possible_matches,
            }
            resolved_medicines.append(medicine_payload)

        # Stage 5: Clinical Safety & Modular Interaction Engine
        safety_analysis = interaction_registry.evaluate_safety(generic_keys, is_pregnant=is_pregnant)

        logger.info(f"Analyzed {len(resolved_medicines)} medicine(s) with {len(safety_analysis.interactions)} interaction(s).")

        return {
            "medicines": resolved_medicines,
            "safety_analysis": safety_analysis.model_dump(),
        }


medicine_service = MedicineService()
