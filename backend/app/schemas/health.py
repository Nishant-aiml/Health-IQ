from pydantic import BaseModel, Field


class HealthStatus(BaseModel):
    status: str = Field(json_schema_extra={"example": "healthy"})
    database: str = Field(json_schema_extra={"example": "connected"})
    environment: str = Field(json_schema_extra={"example": "development"})
    timestamp: str = Field(json_schema_extra={"example": "2026-07-31T06:30:00Z"})
