# --------------------------------------------------
# File: builder.py
# Purpose: Combines patient report, Phase 2B/2C outputs, and retrieved chunks into a single prompt context.
# Module: RAG Engine / Context
# Used By: Grounded Chat Engine
# Future Phase: Phase 2D Hybrid RAG
# --------------------------------------------------

from typing import Dict, Any, List
from backend.app.rag.models import DocumentChunk
from backend.app.rag.context.ranker import context_ranker
from backend.app.rag.context.compressor import context_compressor


class ContextBuilder:
    """
    Structured RAG Context Builder.

    Why it exists:
        Integrates patient laboratory values, Health Score, detected patterns, structured recommendations,
        and top-K retrieved WHO/CDC/NIH/ICMR guidelines into a single structured prompt context.
    """

    def build_full_context(
        self,
        report_analysis: Dict[str, Any],
        recommendation_bundle: Dict[str, Any],
        retrieved_chunks: List[DocumentChunk],
    ) -> str:
        # Rank and compress chunks
        ranked_chunks = context_ranker.rank_context_chunks(retrieved_chunks)
        final_chunks = context_compressor.compress_chunks(ranked_chunks)

        sections: List[str] = []

        # Section 1: Patient Report Summary
        sections.append("=== PATIENT MEDICAL REPORT CONTEXT ===")
        sections.append(f"Report ID: {report_analysis.get('report_id')}")
        sections.append(f"Source File: {report_analysis.get('source_filename')}")
        sections.append(f"Overall Health Score: {report_analysis.get('health_score')}/100")
        sections.append(f"Summary: {report_analysis.get('summary')}")

        # Section 2: Extracted Laboratory Values
        sections.append("\n=== EXTRACTED LABORATORY VALUES ===")
        for p in report_analysis.get("parameters", []):
            range_str = f"{p.get('normal_range_low')} - {p.get('normal_range_high')}" if p.get('normal_range_low') is not None else "N/A"
            sections.append(
                f"• {p.get('canonical_name')}: {p.get('value')} {p.get('unit')} "
                f"(Baseline: {range_str} {p.get('unit')}) | Severity: {p.get('severity')}"
            )

        # Section 3: Detected Correlated Patterns
        patterns = report_analysis.get("detected_patterns", [])
        if patterns:
            sections.append("\n=== DETECTED CLINICAL PATTERNS ===")
            for pat in patterns:
                sections.append(f"• {pat.get('pattern_name')}: {pat.get('summary')}")

        # Section 4: Phase 2C Recommendations
        recs = recommendation_bundle.get("recommendations", [])
        if recs:
            sections.append("\n=== CLINICAL ACTION RECOMMENDATIONS ===")
            for r in recs:
                sections.append(f"• [{r.get('priority')}] {r.get('title')}: {r.get('summary')}")

        # Section 5: Retrieved Medical Guidelines (WHO/CDC/NIH/ICMR)
        if final_chunks:
            sections.append("\n=== RETRIEVED AUTHORITATIVE MEDICAL GUIDELINES ===")
            for idx, c in enumerate(final_chunks, start=1):
                sections.append(
                    f"[{idx}] Source: {c.source} ({c.title}) | Section: {c.medical_topic}\n"
                    f"Excerpt: \"{c.text}\""
                )

        return "\n".join(sections)


context_builder = ContextBuilder()
