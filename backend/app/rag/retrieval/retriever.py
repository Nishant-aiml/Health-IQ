# --------------------------------------------------
# File: retriever.py
# Purpose: Unified Hybrid Medical Retriever orchestrator (Dense + Sparse + RRF).
# Module: RAG Engine / Retrieval
# Used By: Grounded Chat Service
# Future Phase: Phase 2D Hybrid RAG
# --------------------------------------------------

import time
from typing import List
from backend.app.rag.models import DocumentChunk, RetrievalResult
from backend.app.rag.corpus import corpus_loader
from backend.app.rag.query import query_rewriter
from backend.app.rag.providers import vector_store_provider
from backend.app.rag.retrieval.dense import dense_retriever
from backend.app.rag.retrieval.sparse import sparse_bm25_retriever
from backend.app.rag.retrieval.planner import retrieval_planner
from backend.app.rag.retrieval.fusion import reciprocal_rank_fusion
from backend.app.core.config.rag import rag_settings
from backend.app.core.logging import logger


class HybridRetriever:
    """
    Unified Hybrid Medical Retriever.

    Why it exists:
        Combines semantic FAISS dense search with BM25 keyword search using Reciprocal Rank Fusion (RRF).
        Indexes the WHO, CDC, NIH, ICMR corpus at initialization.
    """

    def __init__(self):
        self._is_indexed = False

    def _ensure_indexed(self):
        if not self._is_indexed:
            chunks = corpus_loader.load_all_chunks()
            vector_store_provider.build_index(chunks)
            sparse_bm25_retriever.index(chunks)
            self._is_indexed = True
            logger.info("HybridRetriever initialized and indexed WHO/CDC/NIH/ICMR corpus.")

    def retrieve(self, query: str, top_k: int = None) -> RetrievalResult:
        start_time = time.perf_counter()
        self._ensure_indexed()

        k = top_k or rag_settings.TOP_K_FINAL

        # Step 1: Query Expansion Rewriting
        rewritten_q = query_rewriter.rewrite_query(query)

        # Step 2: Adaptive Weight Planning
        dense_w, sparse_w = retrieval_planner.plan_weights(query)

        # Step 3: Execute Parallel Retrieval (Dense + Sparse)
        dense_res = dense_retriever.retrieve(rewritten_q, top_k=rag_settings.TOP_K_DENSE)
        sparse_res = sparse_bm25_retriever.retrieve(rewritten_q, top_k=rag_settings.TOP_K_SPARSE)

        # Step 4: Reciprocal Rank Fusion (RRF)
        fused_chunks = reciprocal_rank_fusion(
            dense_results=dense_res,
            sparse_results=sparse_res,
            dense_weight=dense_w,
            sparse_weight=sparse_w,
            k_constant=rag_settings.RRF_K_CONSTANT,
            top_k=k,
        )

        duration = round((time.perf_counter() - start_time) * 1000, 2)
        logger.info(f"Hybrid retrieval completed in {duration}ms. Fused top-{len(fused_chunks)} chunks.")

        return RetrievalResult(
            query=query,
            retrieved_chunks=fused_chunks,
            execution_time_ms=duration,
        )


hybrid_retriever = HybridRetriever()
