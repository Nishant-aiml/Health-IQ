from typing import List, Union
from pydantic import AnyHttpUrl, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict
from backend.app.core.config.constants import (
    API_V1_STR,
    PROJECT_NAME,
    PROJECT_VERSION,
    PROJECT_DESCRIPTION,
)


class Settings(BaseSettings):
    APP_NAME: str = PROJECT_NAME
    APP_VERSION: str = PROJECT_VERSION
    APP_DESCRIPTION: str = PROJECT_DESCRIPTION
    API_V1_STR: str = API_V1_STR
    APP_ENV: str = "development"
    DEBUG: bool = True
    PORT: int = 8000
    HOST: str = "0.0.0.0"

    # Database Settings
    DATABASE_URL: str = "sqlite:///./health_companion.db"
    DB_FALLBACK_TO_SQLITE: bool = False

    # Security & CORS Settings
    CORS_ORIGINS: List[str] = [
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:3000",
    ]
    ALLOWED_HOSTS: List[str] = ["localhost", "127.0.0.1"]

    # Logging
    LOG_LEVEL: str = "INFO"
    LOG_FORMAT: str = "json"

    # Future AI API Keys
    SARVAM_API_KEY: str = ""
    GLM_API_KEY: str = ""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=True,
    )


settings = Settings()
