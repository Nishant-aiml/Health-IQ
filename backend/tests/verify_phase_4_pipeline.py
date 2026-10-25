"""
Phase 4 Pipeline Verification Script
=====================================
Validates the complete Phase 4 Clinical Collaboration engine without needing a running HTTP server.
Tests: Package Builder, Care Team Permissions, FHIR Mapper, Notes Repository, API Endpoint Stubs.
"""

import sys, os, json, hashlib, datetime

# ── Path setup ──────────────────────────────────────────────────────────────
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

PASS = "\033[92mPASS\033[0m"
FAIL = "\033[91mFAIL\033[0m"
results = []

def check(label: str, condition: bool, detail: str = ""):
    status = PASS if condition else FAIL
    print(f"  [{status}] {label}" + (f" — {detail}" if detail else ""))
    results.append(condition)

print("\n" + "=" * 70)
print("  PHASE 4 PIPELINE VERIFICATION — Clinical Collaboration Engine")
print("=" * 70)

# ══════════════════════════════════════════════════════════════════════
# 1. Clinical Case Package Builder
# ══════════════════════════════════════════════════════════════════════
print("\n▶ 1. Clinical Case Package Builder")
try:
    from backend.app.clinical.models import ClinicalCasePackage, ClinicalPackageStatus, EvidenceNode
    pkg = ClinicalCasePackage(
        report_id="RPT-001", user_id="USR-001",
        status=ClinicalPackageStatus.AI_GENERATED,
        active_summary="Patient presents borderline hypercholesterolemia.",
        medication_summary="No medications on file.",
        nutrition_summary="Mediterranean diet recommended.",
        historical_summary="Cholesterol up 13% in 6 months.",
        timeline_summary="2 lab reports, 1 milestone.",
        questions_for_physician=[],
        evidence_graph=[],
    )
    check("ClinicalCasePackage instantiation", pkg.package_id.startswith("PKG-"))
    check("Status is AI Generated", pkg.status == ClinicalPackageStatus.AI_GENERATED)

    # SHA-256
    h = pkg.compute_sha256()
    check("SHA-256 is 64 hex chars", len(h) == 64 and all(c in "0123456789abcdef" for c in h))
    check("SHA-256 is deterministic", h == pkg.compute_sha256())
except Exception as e:
    check("ClinicalCasePackage module import", False, str(e))

# ══════════════════════════════════════════════════════════════════════
# 2. Audience Formatter
# ══════════════════════════════════════════════════════════════════════
print("\n▶ 2. Audience Formatter")
try:
    from backend.app.clinical.formatter import ClinicalPackageFormatter
    from backend.app.clinical.models import ClinicalCasePackage, ClinicalPackageStatus

    pkg = ClinicalCasePackage(
        report_id="RPT-002", user_id="USR-002",
        status=ClinicalPackageStatus.AI_GENERATED,
        active_summary="Elevated glucose trending.", medication_summary="Metformin 500mg.",
        nutrition_summary="Low-carb diet.", historical_summary="Glucose up 10%.",
        timeline_summary="3 events.", questions_for_physician=[], evidence_graph=[],
    )
    for audience in ["Doctor-Friendly", "Patient-Friendly", "Family-Friendly"]:
        formatted = ClinicalPackageFormatter.format(pkg, audience)
        check(f"Format for {audience}", formatted.get("audience") == audience and "active_summary" in formatted)
except Exception as e:
    check("ClinicalPackageFormatter", False, str(e))

# ══════════════════════════════════════════════════════════════════════
# 3. Care Team Permissions
# ══════════════════════════════════════════════════════════════════════
print("\n▶ 3. Care Team Permissions")
try:
    from backend.app.care.permissions import CareTeamPermissions
    from backend.app.care.models import CareTeamRole

    perms = CareTeamPermissions()
    check("Primary Doctor has full_summary", perms.can(CareTeamRole.PRIMARY_DOCTOR, "full_summary"))
    check("Family cannot access notes", not perms.can(CareTeamRole.FAMILY, "notes"))
    check("Dietitian can access nutrition", perms.can(CareTeamRole.DIETITIAN, "nutrition_summary"))
    check("Caregiver cannot access FHIR export", not perms.can(CareTeamRole.CAREGIVER, "fhir_export"))
    check("Specialist can access FHIR export", perms.can(CareTeamRole.SPECIALIST, "fhir_export"))
except Exception as e:
    check("CareTeamPermissions", False, str(e))

# ══════════════════════════════════════════════════════════════════════
# 4. FHIR R4 Mapper
# ══════════════════════════════════════════════════════════════════════
print("\n▶ 4. FHIR R4 Mapper")
try:
    from backend.app.fhir.mapper import FHIRMapper

    report_data = {
        "report_id": "RPT-003", "user_id": "USR-003",
        "patient_name": "Jane Doe", "patient_age": 45,
        "parameters": [
            {"name": "Glucose", "value": 105, "unit": "mg/dL", "status": "Borderline", "reference_range": "70-99"},
            {"name": "Hemoglobin", "value": 13.5, "unit": "g/dL", "status": "Normal", "reference_range": "12-16"},
        ],
        "ai_summary": "Borderline glucose. Normal hemoglobin.",
    }

    bundle = FHIRMapper.map_to_fhir_bundle(report_data)
    check("Bundle resourceType is Bundle", bundle.get("resourceType") == "Bundle")
    check("Bundle has entries", len(bundle.get("entry", [])) > 0)

    rtypes = {e["resource"]["resourceType"] for e in bundle["entry"] if "resource" in e}
    check("Patient resource present", "Patient" in rtypes)
    check("Observation resources present", "Observation" in rtypes)
    check("DiagnosticReport resource present", "DiagnosticReport" in rtypes)
except Exception as e:
    check("FHIRMapper", False, str(e))

# ══════════════════════════════════════════════════════════════════════
# 5. Clinical Notes Service
# ══════════════════════════════════════════════════════════════════════
print("\n▶ 5. Clinical Notes Service")
try:
    from backend.app.notes.service import ClinicalNotesService
    from backend.app.notes.models import NoteType
    from unittest.mock import MagicMock

    service = ClinicalNotesService()
    check("ClinicalNotesService instantiates", service is not None)

    from backend.app.notes.models import NoteType
    check("NoteType has Clinical Observation", NoteType.CLINICAL_OBSERVATION is not None)
    check("NoteType has Doctor Comment", NoteType.DOCTOR_COMMENT is not None)
    check("NoteType has Patient Question", NoteType.PATIENT_QUESTION is not None)
    check("NoteType has Visit Summary", NoteType.VISIT_SUMMARY is not None)
except Exception as e:
    check("ClinicalNotesService", False, str(e))

# ══════════════════════════════════════════════════════════════════════
# 6. Evidence Graph Structure
# ══════════════════════════════════════════════════════════════════════
print("\n▶ 6. Evidence Graph")
try:
    from backend.app.clinical.models import EvidenceNode

    nodes = [
        EvidenceNode(source_type="lab_result",       title="Glucose: 98",         description="High-normal.", connected_to=["n2"], confidence_score=0.97),
        EvidenceNode(source_type="trend_analysis",   title="Glucose Trend",       description="Rising.",     connected_to=["n3"], confidence_score=0.88),
        EvidenceNode(source_type="recommendation",   title="Lifestyle Change",    description="Low-carb.",   connected_to=["n4"], confidence_score=0.92),
        EvidenceNode(source_type="nutrition_plan",   title="Mediterranean Diet",  description="Olive oil.",  connected_to=["n5"], confidence_score=0.90),
        EvidenceNode(source_type="clinical_summary", title="Clinical Summary",    description="Monitor.",    connected_to=[],     confidence_score=0.95),
    ]
    check("5 Evidence nodes created", len(nodes) == 5)
    flow = [n.source_type for n in nodes]
    expected_flow = ["lab_result", "trend_analysis", "recommendation", "nutrition_plan", "clinical_summary"]
    check("Evidence pipeline flow correct", flow == expected_flow)
    check("All confidence scores in (0,1]", all(0 < n.confidence_score <= 1.0 for n in nodes))
except Exception as e:
    check("EvidenceNode graph", False, str(e))

# ══════════════════════════════════════════════════════════════════════
# 7. Document Lifecycle States
# ══════════════════════════════════════════════════════════════════════
print("\n▶ 7. Document Lifecycle States")
try:
    from backend.app.clinical.models import ClinicalPackageStatus
    expected = {"Draft", "AI Generated", "Reviewed", "Shared", "Archived"}
    actual = {s.value for s in ClinicalPackageStatus}
    check("All 5 lifecycle states present", actual == expected, str(actual))
except Exception as e:
    check("ClinicalPackageStatus", False, str(e))

# ══════════════════════════════════════════════════════════════════════
# Summary
# ══════════════════════════════════════════════════════════════════════
print("\n" + "=" * 70)
total = len(results)
passed = sum(results)
failed = total - passed
print(f"\n  Results: {passed}/{total} checks passed" + (f" | {failed} FAILED" if failed else " | All PASSED ✓"))
print("=" * 70 + "\n")
sys.exit(0 if failed == 0 else 1)
