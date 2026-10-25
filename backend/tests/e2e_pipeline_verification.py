# --------------------------------------------------
# File: e2e_pipeline_verification.py
# Purpose: Comprehensive end-to-end pipeline verification test script.
# Module: Test Suite / E2E
# Used By: Agent verification & CLI execution
# Future Phase: Phase 2 Core Platform Verification
# --------------------------------------------------

import time
import requests
import json

BASE_URL = "http://127.0.0.1:8000/api/v1"


def run_e2e_verification():
    print("=" * 60)
    print("STARTING COMPREHENSIVE END-TO-END PIPELINE TEST")
    print("=" * 60)

    # Step 1: Health Check
    print("\n[Step 1] Testing System Health Check (/health)...")
    resp = requests.get(f"{BASE_URL}/health")
    assert resp.status_code == 200, f"Health check failed: {resp.text}"
    health_data = resp.json()
    print(f"   [OK] Health Check PASSED: status={health_data['data']['status']}, db={health_data['data']['database']}")

    # Step 2: Batch Document Submission (.txt format)
    print("\n[Step 2] Submitting Sample Lab Report to Document Batch Ingestion (/documents/batch)...")
    sample_report_text = (
        "METROPOLIS HEALTHCARE LAB REPORT\n"
        "Patient: John Doe, Age: 35, Gender: Male\n"
        "Hemoglobin: 11.2 g/dL (Normal Range: 13.8 - 17.2)\n"
        "Fasting Blood Sugar: 118 mg/dL (Normal Range: 70 - 99)\n"
        "Serum Calcium: 7.5 mg/dL (Normal Range: 8.5 - 10.2)\n"
        "Total Cholesterol: 235 mg/dL (Normal Range: 125 - 200)\n"
        "Triglycerides: 180 mg/dL (Normal Range: < 150)\n"
    )

    files = [("files", ("john_doe_lab_report.txt", sample_report_text.encode("utf-8"), "text/plain"))]
    data = {"doc_type": "lab_report"}

    upload_resp = requests.post(f"{BASE_URL}/documents/batch", files=files, data=data)
    assert upload_resp.status_code == 200, f"Upload failed: {upload_resp.text}"
    upload_data = upload_resp.json()["data"]
    batch_id = upload_data["batch_id"]
    job_ids = upload_data["job_ids"]
    print(f"   [OK] Batch Submission Accepted: batch_id={batch_id}, job_ids={job_ids}")

    # Step 3: Poll Batch Status until Completed
    print("\n[Step 3] Polling Worker Ingestion Progress (/documents/batch/{id}/status)...")
    report_id = None
    for attempt in range(15):
        time.sleep(1)
        params = [("job_ids", j_id) for j_id in job_ids]
        status_resp = requests.get(f"{BASE_URL}/documents/batch/{batch_id}/status", params=params)
        assert status_resp.status_code == 200, f"Status check failed: {status_resp.text}"
        status_items = status_resp.json()["data"]
        item = status_items[0]
        print(f"   Attempt {attempt+1}: Stage='{item['stage']}', Status='{item['status']}'")

        if item["status"] == "completed":
            report_id = item["report_id"]
            print(f"   [OK] Document Processing COMPLETED! report_id={report_id}")
            break
        elif item["status"] == "failed":
            raise RuntimeError(f"Processing failed: {item['error_reason']}")

    assert report_id is not None, "Report processing timed out."

    # Step 4: Fetch Report Analysis Engine Results
    print(f"\n[Step 4] Fetching Report Analysis Engine Results (/reports/{report_id})...")
    report_resp = requests.get(f"{BASE_URL}/reports/{report_id}")
    assert report_resp.status_code == 200, f"Fetch report failed: {report_resp.text}"
    analysis = report_resp.json()["data"]
    print(f"   [OK] Health Score: {analysis['health_score']}/100")
    print(f"   [OK] Summary: '{analysis['summary']}'")
    print(f"   [OK] Extracted Parameters ({len(analysis['parameters'])}):")
    for p in analysis["parameters"]:
        print(f"      - {p['canonical_name']}: {p['value']} {p['unit']} (Severity: {p['severity']}, Critical: {p['is_critical']})")

    print(f"   [OK] Critical Alerts Count: {len(analysis['critical_alerts'])}")
    print(f"   [OK] Correlated Patterns Count: {len(analysis['detected_patterns'])}")

    # Step 5: Fetch Structured Recommendations & Evidence Chains
    print(f"\n[Step 5] Fetching Recommendations & Evidence Chains (/reports/{report_id}/recommendations)...")
    rec_resp = requests.get(f"{BASE_URL}/reports/{report_id}/recommendations")
    assert rec_resp.status_code == 200, f"Fetch recommendations failed: {rec_resp.text}"
    rec_data = rec_resp.json()["data"]
    print(f"   [OK] Recommendations Count: {len(rec_data['recommendations'])}")
    for r in rec_data["recommendations"]:
        print(f"      - [{r['priority']}] {r['title']}: {r['summary']}")
    print(f"   [OK] Evidence Chains Count: {len(rec_data['evidence_chains'])}")
    print(f"   [OK] Doctor Questions Count: {len(rec_data['doctor_questions'])}")
    print(f"   [OK] ELI10 Explanation: '{rec_data['eli10_explanation'][:80]}...'")

    # Step 6: Grounded Medical RAG Chat Execution
    print(f"\n[Step 6] Testing Grounded Medical RAG Chat (/chat/{report_id})...")
    chat_payload = {"question": "Why is my hemoglobin and calcium low?"}
    chat_resp = requests.post(f"{BASE_URL}/chat/{report_id}", json=chat_payload)
    assert chat_resp.status_code == 200, f"Chat query failed: {chat_resp.text}"
    chat_data = chat_resp.json()["data"]
    print(f"   [OK] Chat Response Received:")
    print(f"      Answer: '{chat_data['answer'][:120]}...'")
    print(f"      Citations ({len(chat_data['citations'])}): {[c['title'] for c in chat_data['citations']]}")

    # Step 7: PDF Medical Report Export
    print(f"\n[Step 7] Testing PDF Medical Report Generation (/reports/{report_id}/pdf)...")
    pdf_resp = requests.get(f"{BASE_URL}/reports/{report_id}/pdf")
    assert pdf_resp.status_code == 200, f"PDF export failed: {pdf_resp.text}"
    assert pdf_resp.headers["content-type"] == "application/pdf"
    assert len(pdf_resp.content) > 1000, "PDF byte stream too small"
    assert pdf_resp.content.startswith(b"%PDF")
    print(f"   [OK] PDF Export Successful ({len(pdf_resp.content)} bytes generated)")

    # Step 8: JSON Versioned Report Export
    print(f"\n[Step 8] Testing Versioned JSON Export (/reports/{report_id}/json)...")
    json_resp = requests.get(f"{BASE_URL}/reports/{report_id}/json")
    assert json_resp.status_code == 200, f"JSON export failed: {json_resp.text}"
    parsed_json = json_resp.json()
    assert parsed_json["schema_version"] == "1.0"
    print(f"   [OK] JSON Export Successful (schema_version='1.0', report_id={parsed_json['report_id']})")

    # Step 9: CSV Multi-Dataset Report Export
    print(f"\n[Step 9] Testing Multi-Dataset CSV Export (/reports/{report_id}/csv)...")
    csv_resp = requests.get(f"{BASE_URL}/reports/{report_id}/csv")
    assert csv_resp.status_code == 200, f"CSV export failed: {csv_resp.text}"
    csv_text = csv_resp.text
    assert "EXTRACTED LABORATORY PARAMETERS" in csv_text
    assert "ACTION RECOMMENDATIONS" in csv_text
    print(f"   [OK] CSV Export Successful ({len(csv_text.splitlines())} lines generated)")

    print("\n" + "=" * 60)
    print("ALL PIPELINE STAGES & EXPORTS VERIFIED SUCCESSFULLY!")
    print("=" * 60)


if __name__ == "__main__":
    run_e2e_verification()
