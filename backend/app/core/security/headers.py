from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.core.config.settings import settings


def setup_security(app: FastAPI) -> None:
    """
    Configures CORS middleware to allow frontend communication from local dev & Render cloud.
    """
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_origin_regex=r"https://.*\.onrender\.com|http://localhost:\d+|http://127\.0\.0\.1:\d+",
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
