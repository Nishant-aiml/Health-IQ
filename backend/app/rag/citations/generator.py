# --------------------------------------------------
# File: generator.py
# Purpose: Citation generator extracting explicit WHO/CDC/NIH/ICMR provenance references.
# Module: RAG Engine / Citations
# Used By: Grounded Chat Engine
# Future Phase: Phase 2D Hybrid RAG
# --------------------------------------------------

from typing import List, Dict, Any
from backend.app.rag.models import DocumentChunk
from backend.app.rag.citations.models import CitationReference


class CitationGenerator:
    """
    Citation Generator.

    Why it exists:
        Generates explicit, transparent citation references for retrieved WHO, CDC, NIH, ICMR chunks
        and internal lab parameters used in generating the grounded response.
    """

    def generate_citations(
        self,
        retrieved_chunks: List[DocumentChunk],
        report_parameters: List[Dict[str, Any]],
    ) -> List[CitationReference]:
        citations: List[CitationReference] = []

        # 1. External Guideline Citations
        for c in retrieved_chunks:
            citations.append(
                CitationReference(
                    citation_id=f"CITE_{c.doc_id}",
                    source_organization=c.source,
                    title=c.title,
                    medical_topic=c.medical_topic,
                    excerpt=c.text[:150] + "...",
                    relevance_score=c.score,
                )
            )

        # 2. Internal Lab Parameter Citations
        for p in report_parameters:
            if p.get("severity", "normal") != "normal":
                citations.append(
                    CitationReference(
                        citation_id=f"CITE_PARAM_{p.get('canonical_name')}",
                        source_organization="Patient Report",
                        title=f"Lab Parameter: {p.get('canonical_name')}",
                        medical_topic="Extracted Parameter Value",
                        excerpt=f"Observed value: {p.get('value')} {p.get('unit')} (Severity: {p.get('severity')})",
                        relevance_score=1.0,
                    )
                )

        return citations


citation_generator = CitationGenerator()
