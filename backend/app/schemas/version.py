from pydantic import BaseModel, Field


class VersionInfo(BaseModel):
    name: str = Field(json_schema_extra={"example": "AI Health Intelligence Platform"})
    version: str = Field(json_schema_extra={"example": "0.1.0"})
    api_version: str = Field(json_schema_extra={"example": "/api/v1"})
    architecture_phase: str = Field(json_schema_extra={"example": "Phase 1 - Foundation"})
