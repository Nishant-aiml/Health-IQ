# --------------------------------------------------
# File: json_export.py
# Purpose: Versioned JSON Report Export Generator.
# Module: Export Engine
# Used By: Export APIs & Download Service
# Future Phase: Phase 2E Export System
# --------------------------------------------------

import json
from datetime import datetime
from typing import Dict, Any
from backend.app.export.models import VersionedJSONExport


class JSONExportService:
    """
    JSON Export Service.

    Why it exists:
        Generates structured, versioned JSON exports (`schema_version: "1.0"`) with timestamps.
    """

    def generate_json_export(
        self,
        analysis: Dict[str, Any],
        recommendation_bundle: Dict[str, Any],
    ) -> str:
        payload = VersionedJSONExport(
            generated_at=datetime.utcnow().isoformat() + "Z",
            report_id=analysis.get("report_id", 0),
            analysis=analysis,
            recommendations=recommendation_bundle,
        )
        return json.dumps(payload.dict(), indent=2, default=str)


json_export_service = JSONExportService()
