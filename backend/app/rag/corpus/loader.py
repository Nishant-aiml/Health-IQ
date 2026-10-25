# --------------------------------------------------
# File: loader.py
# Purpose: Medical Knowledge Corpus Loader for WHO, CDC, NIH, ICMR guidelines.
# Module: RAG Engine / Corpus
# Used By: Hybrid Retriever Index Builder
# Future Phase: Phase 2D Hybrid RAG
# --------------------------------------------------

from typing import List
from backend.app.rag.models import CorpusDocument, DocumentChunk
from backend.app.rag.corpus.document import create_chunks_from_document
from backend.app.rag.corpus.metadata import get_default_corpus_metadata
from backend.app.core.logging import logger


class CorpusLoader:
    """
    Curated Medical Guidelines Corpus Loader.

    Why it exists:
        Loads evidence-based medical guidelines from authoritative international bodies
        (WHO, CDC, NIH, ICMR). Provides grounded clinical context to prevent LLM hallucinations.
    """

    def __init__(self):
        self._documents: List[CorpusDocument] = []
        self._initialize_curated_corpus()

    def _initialize_curated_corpus(self):
        # 1. WHO Anemia Guidelines
        self._documents.append(
            CorpusDocument(
                doc_id="WHO_ANEMIA_2023",
                title="WHO Guidelines on Hemoglobin Baselines and Anemia Diagnosis",
                source="WHO",
                publication="World Health Organization 2023 Guidelines",
                medical_topic="Hematology",
                content=(
                    "Anemia is defined as a reduction in the mass of circulating red blood cells or hemoglobin concentration below normal reference thresholds. "
                    "In adult males, hemoglobin lower than 13.8 g/dL and in non-pregnant adult females lower than 12.0 g/dL signals mild to moderate anemia. "
                    "Microcytic anemia (characterized by MCV < 80 fL) is most frequently caused by nutritional iron deficiency. "
                    "Management includes oral iron supplementation (ferrous sulfate/fumarate), dietary vitamin C for iron absorption, and serum ferritin screening."
                ),
                metadata=get_default_corpus_metadata("WHO", "Hematology"),
            )
        )

        # 2. CDC Diabetes & Glycemic Guidelines
        self._documents.append(
            CorpusDocument(
                doc_id="CDC_DIABETES_2024",
                title="CDC Standards for Fasting Blood Sugar and Diabetes Prevention",
                source="CDC",
                publication="CDC Diabetes Public Guidelines 2024",
                medical_topic="Endocrinology",
                content=(
                    "Fasting plasma glucose levels between 70 and 99 mg/dL represent normal fasting glycemic baseline. "
                    "Fasting blood glucose from 100 to 125 mg/dL indicates impaired fasting glucose (pre-diabetes). "
                    "Fasting values of 126 mg/dL or higher on two separate occasions confirm a diabetes diagnosis. "
                    "Lifestyle intervention focusing on 150 minutes of weekly aerobic exercise, high-fiber soluble diets, and weight management reduces progression risk by 58%."
                ),
                metadata=get_default_corpus_metadata("CDC", "Endocrinology"),
            )
        )

        # 3. NIH Kidney & Renal Health Guidelines
        self._documents.append(
            CorpusDocument(
                doc_id="NIH_RENAL_2023",
                title="NIH Clinical Guide to Serum Creatinine and Kidney Health",
                source="NIH",
                publication="National Institutes of Health Renal Care Manual",
                medical_topic="Nephrology",
                content=(
                    "Serum creatinine is a waste product generated from normal muscle breakdown and filtered exclusively by renal glomeruli. "
                    "Normal female baselines range from 0.59 to 1.04 mg/dL while male baselines range from 0.74 to 1.35 mg/dL. "
                    "Elevated creatinine indicates reduced renal clearance. Patients with elevated renal markers should ensure proper hydration, "
                    "avoid nonsteroidal anti-inflammatory drugs (NSAIDs like ibuprofen/naproxen), and consult a nephrologist for eGFR evaluation."
                ),
                metadata=get_default_corpus_metadata("NIH", "Nephrology"),
            )
        )

        # 4. ICMR Lipid & Metabolic Guidelines
        self._documents.append(
            CorpusDocument(
                doc_id="ICMR_LIPID_2023",
                title="ICMR Guidelines on Lipid Management and Metabolic Syndrome",
                source="ICMR",
                publication="Indian Council of Medical Research Guidelines",
                medical_topic="Cardiology",
                content=(
                    "Total cholesterol levels under 200 mg/dL and fasting triglycerides under 150 mg/dL are recommended for optimal cardiovascular health. "
                    "Combined elevation of fasting glucose and blood triglycerides is a hallmark of metabolic syndrome risk. "
                    "Dietary recommendations include substituting saturated fats with monounsaturated oils (mustard/olive oil), increasing fiber, and daily physical activity."
                ),
                metadata=get_default_corpus_metadata("ICMR", "Cardiology"),
            )
        )

    def load_all_chunks(self) -> List[DocumentChunk]:
        """Loads and chunks all documents in the curated corpus."""
        all_chunks: List[DocumentChunk] = []
        for doc in self._documents:
            chunks = create_chunks_from_document(doc)
            all_chunks.extend(chunks)
        logger.info(f"Loaded {len(self._documents)} medical documents into {len(all_chunks)} chunks.")
        return all_chunks


corpus_loader = CorpusLoader()
