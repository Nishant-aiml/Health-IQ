# --------------------------------------------------
# File: router.py
# Purpose: Main API v1 router combining all endpoint sub-routers.
# Module: API Engine / Core Router
# Used By: FastAPI Application (backend/app/main.py)
# --------------------------------------------------

from fastapi import APIRouter
from backend.app.api.v1.endpoints.health import router as health_router
from backend.app.api.v1.endpoints.version import router as version_router
from backend.app.api.v1.endpoints.documents import router as documents_router
from backend.app.api.v1.endpoints.reports import router as reports_router
from backend.app.api.v1.endpoints.chat import router as chat_router
from backend.app.api.v1.endpoints.export import router as export_router
from backend.app.api.v1.endpoints.prescriptions import router as prescriptions_router
from backend.app.api.v1.endpoints.history import router as history_router
from backend.app.api.v1.endpoints.nutrition import router as nutrition_router
from backend.app.api.v1.endpoints.lifestyle import router as lifestyle_router
from backend.app.api.v1.endpoints.wellness import router as wellness_router
from backend.app.api.v1.endpoints.clinical import router as clinical_router
from backend.app.api.v1.endpoints.notes import router as notes_router
from backend.app.api.v1.endpoints.auth import router as auth_router

api_router = APIRouter()

# Include Authentication router
api_router.include_router(auth_router)

# Include core system routers
api_router.include_router(health_router)
api_router.include_router(version_router)

# Include Document Ingestion router
api_router.include_router(documents_router)

# Include Reports & Recommendations router
api_router.include_router(reports_router)

# Include Grounded Report Chat router
api_router.include_router(chat_router)

# Include Multi-Format Export Engine router
api_router.include_router(export_router)

# Include Prescription & Medicine Intelligence router
api_router.include_router(prescriptions_router)

# Include Longitudinal Health Intelligence router
api_router.include_router(history_router)

# Include Nutrition & Lifestyle Intelligence routers
api_router.include_router(nutrition_router)
api_router.include_router(lifestyle_router)
api_router.include_router(wellness_router)

# Include Clinical Collaboration & Ecosystem routers
api_router.include_router(clinical_router)
api_router.include_router(notes_router)
