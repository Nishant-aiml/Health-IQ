# --------------------------------------------------
# File: fusion.py
# Purpose: Reciprocal Rank Fusion (RRF) algorithm combining dense and sparse rank scores.
# Module: RAG Engine / Retrieval
# Used By: Hybrid Retriever
# Future Phase: Phase 2D Hybrid RAG
# --------------------------------------------------

from typing import List, Tuple, Dict
from backend.app.rag.models import DocumentChunk
from backend.app.core.config.rag import rag_settings


def reciprocal_rank_fusion(
    dense_results: List[Tuple[DocumentChunk, float]],
    sparse_results: List[Tuple[DocumentChunk, float]],
    dense_weight: float = 0.5,
    sparse_weight: float = 0.5,
    k_constant: int = 60,
    top_k: int = 3,
) -> List[DocumentChunk]:
    """
    Executes Reciprocal Rank Fusion (RRF) over dense and sparse retrieval ranks.

    Formula:
        RRF Score(chunk) = (dense_weight / (k + dense_rank)) + (sparse_weight / (k + sparse_rank))

    Inputs:
        dense_results: List of (chunk, score) from FAISS dense search.
        sparse_results: List of (chunk, score) from BM25 search.
        dense_weight: Weight assigned to dense ranking.
        sparse_weight: Weight assigned to sparse ranking.
        k_constant: RRF constant (default 60).
        top_k: Number of final top chunks to return.

    Returns:
        List of fused DocumentChunk instances ordered by RRF score.
    """
    rrf_scores: Dict[str, float] = {}
    chunk_map: Dict[str, DocumentChunk] = {}

    # Rank dense results
    for rank, (chunk, score) in enumerate(dense_results, start=1):
        c_id = chunk.chunk_id
        chunk_map[c_id] = chunk
        rrf_scores[c_id] = rrf_scores.get(c_id, 0.0) + (dense_weight / (k_constant + rank))

    # Rank sparse results
    for rank, (chunk, score) in enumerate(sparse_results, start=1):
        c_id = chunk.chunk_id
        chunk_map[c_id] = chunk
        rrf_scores[c_id] = rrf_scores.get(c_id, 0.0) + (sparse_weight / (k_constant + rank))

    # Sort chunks by RRF score descending
    sorted_ids = sorted(rrf_scores.keys(), key=lambda cid: rrf_scores[cid], reverse=True)

    fused_chunks: List[DocumentChunk] = []
    for cid in sorted_ids[:top_k]:
        chk = chunk_map[cid]
        chk.score = round(rrf_scores[cid], 5)
        fused_chunks.append(chk)

    return fused_chunks
