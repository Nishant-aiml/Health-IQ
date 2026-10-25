# Architecture Overview — AI Health Intelligence Platform (HealthLens AI)

## Product Vision
AI Health Companion is an AI-powered personal health intelligence platform designed to transform raw medical documents (lab reports & prescriptions) into explainable, conversational, personalized health insights.

## Core Architectural Principles
1. **Explainable AI**: Every output carries supporting evidence citations and explicitly stated limitations.
2. **Clinical Safety**: No clinical authority simulation, no diagnosis claims, no prescription dosage modifications.
3. **Fault Isolation**: Tiered OCR and asynchronous queueing ensure single document errors never cascade.
4. **Consent-First Sharing**: Explicit per-item selection for QR-code based temporary health profile sharing.

## High-Level System Architecture
```
┌──────────────────────────────────────────────────────────────┐
│                        FRONTEND (React)                       │
│   Upload · Dashboard · Chat · Trends · Medicine Explainer · QR │
└─────────────────────────────┬────────────────────────────────┘
                               │ REST (JSON)
                               ▼
┌──────────────────────────────────────────────────────────────┐
│                      API LAYER (FastAPI)                      │
└─────────────────────────────┬────────────────────────────────┘
                               │
        ┌──────────────────┬──┴───┬──────────────────┐
        ▼                  ▼      ▼                  ▼
  ┌───────────┐      ┌───────────┐      ┌───────────┐      ┌───────────┐
  │ INGESTION │      │ ANALYSIS  │      │  AI / RAG │      │  SHARING  │
  │   QUEUE   │      │  ENGINE   │      │   ENGINE  │      │  MODULE   │
  └─────┬─────┘      └─────┬─────┘      └─────┬─────┘      └─────┬─────┘
        │                  │                  │                  │
        └──────────────────┴────────┬─────────┴──────────────────┘
                                     ▼
                        ┌──────────────────────┐
                        │   SQLite DATABASE     │
                        └──────────────────────┘
```

## Phase Roadmap
- **Phase 1 (Current)**: Enterprise Foundation — FastAPI, SQLModel database schemas, generic UI design system, health/version APIs, logging, security, modular routing.
- **Phase 2**: Core AI & RAG Engine — Multi-tier OCR, abnormal parameter canonicalization, FAISS+BM25 hybrid RAG, evidence/limitation generation, report chat.
- **Phase 3**: Value Addition — Medicine explainer, multi-language support (English/Hindi), trend timeline engine.
- **Phase 4 & 5**: Reminders, Food checker, Patient QR Health Card.
