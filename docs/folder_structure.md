# Folder Structure Explanation

```
hackathon codex/
├── AI_Health_Companion_Architecture.md # Master Architecture Document (Single Source of Truth)
├── README.md                           # Main Project Overview & Getting Started Guide
├── pyproject.toml                      # Backend Python Dependencies & Tool Settings
├── .env.example                        # Configuration Blueprint
├── .gitignore                          # Git Exclusions
├── docs/                               # Architecture, Folder, and Standards Documentation
│   ├── architecture_overview.md
│   ├── folder_structure.md
│   └── coding_standards.md
├── backend/                            # FastAPI Application Root
│   ├── app/
│   │   ├── main.py                     # Application Entry Point & Lifespan Hooks
│   │   ├── api/                        # Routing & Dependencies
│   │   │   ├── dependencies.py         # FastAPI Dependency Injection
│   │   │   └── v1/
│   │   │       ├── router.py           # V1 Router Aggregator
│   │   │       └── endpoints/          # Endpoint Controllers
│   │   │           ├── health.py       # Health Check Endpoint
│   │   │           ├── version.py      # Version Info Endpoint
│   │   │           ├── documents.py    # Placeholders for Future Ingestion
│   │   │           ├── reports.py      # Placeholders for Future Analysis
│   │   │           ├── prescriptions.py# Placeholders for Future Prescriptions
│   │   │           ├── chat.py         # Placeholders for Future RAG Chat
│   │   │           ├── trends.py       # Placeholders for Future Trends
│   │   │           └── share.py        # Placeholders for Future QR Sharing
│   │   ├── core/                       # Core App Setup
│   │   │   ├── config/                 # Settings & Constants
│   │   │   │   ├── settings.py
│   │   │   │   └── constants.py
│   │   │   ├── logging.py              # Structured JSON Logging
│   │   │   ├── exceptions.py           # Central Exception Handler
│   │   │   ├── middleware.py           # Timing & Request ID Middleware
│   │   │   └── security/               # Security & Headers Middleware
│   │   ├── db/                         # Database Configuration
│   │   │   └── session.py              # SQLite Engine & SQLModel Sessions
│   │   ├── models/                     # SQLModel Entity Definitions (Per-domain)
│   │   │   ├── user.py
│   │   │   ├── report.py
│   │   │   ├── extracted_value.py
│   │   │   ├── prescription.py
│   │   │   ├── risk_analysis.py
│   │   │   ├── recommendation.py
│   │   │   ├── doctor_question.py
│   │   │   ├── job.py
│   │   │   ├── chat.py
│   │   │   ├── guidelines.py
│   │   │   ├── trend.py
│   │   │   └── share.py
│   │   ├── schemas/                    # Pydantic Request/Response Models
│   │   │   ├── base.py
│   │   │   ├── health.py
│   │   │   ├── version.py
│   │   │   ├── report.py
│   │   │   └── chat.py
│   │   ├── repositories/               # Data Access Repositories
│   │   │   ├── base.py
│   │   │   ├── user_repository.py
│   │   │   ├── report_repository.py
│   │   │   └── job_repository.py
│   │   ├── services/                   # Business Logic Service Layer
│   │   │   ├── base.py
│   │   │   └── health_service.py
│   │   └── utils/                      # Helper Utilities
│   │       ├── file_utils.py
│   │       └── datetime_utils.py
│   └── tests/                          # Backend Test Suite
│       ├── conftest.py
│       ├── test_health.py
│       ├── test_version.py
│       ├── test_db.py
│       ├── test_cors.py
│       └── test_exceptions.py
└── frontend/                           # React + Vite + Tailwind CSS Application
    ├── package.json
    ├── vite.config.ts
    ├── tailwind.config.js
    ├── index.html
    └── src/
        ├── App.tsx
        ├── main.tsx
        ├── index.css
        ├── components/
        │   ├── ui/                     # Generic Reusable Design Tokens & Primitives
        │   │   ├── Button.tsx
        │   │   ├── Card.tsx
        │   │   ├── Input.tsx
        │   │   ├── Modal.tsx
        │   │   ├── Table.tsx
        │   │   ├── Badge.tsx
        │   │   ├── Typography.tsx
        │   │   ├── Container.tsx
        │   │   ├── LoadingSpinner.tsx
        │   │   ├── ErrorAlert.tsx
        │   │   └── EmptyState.tsx
        │   └── layout/                 # Structural Layout Components
        │       ├── Navbar.tsx
        │       ├── Footer.tsx
        │       └── RootLayout.tsx
        ├── pages/                      # Page Views (No App Features in Phase 1)
        │   ├── LandingPage.tsx
        │   ├── HomePage.tsx
        │   ├── AboutPage.tsx
        │   ├── NotFoundPage.tsx
        │   └── ErrorDemoPage.tsx
        └── services/
            └── api.ts                  # API Integration Client
```
