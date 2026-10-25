# AI Health Companion (HealthLens AI) — Complete Architecture & System Design

---

## 1. Product Vision

AI Health Companion is an AI-powered personal health intelligence platform that turns raw medical documents — lab reports and prescriptions — into an explainable, conversational, personalized health experience.

The core differentiator is **explainable AI**: every AI output (recommendation, risk flag, diet suggestion) is grounded in retrieved medical references and comes with supporting evidence and stated limitations, rather than being an opaque LLM answer. This matters both as a product principle and as a hackathon pitch angle — it directly answers the judge question "how do I know this is trustworthy?" before it's asked.

**Story arc for the pitch:** report understanding → prescription understanding → conversational Q&A → personalized guidance → explainable scoring → shareable summary. Each stage is a working module, so the arc can actually be demoed live, not just described on a slide.

**Positioning:** this is a platform (multiple connected modules sharing one data model and one RAG backbone), not a single-feature demo. Against ~50 competing teams, most of whom will likely build a single "upload → explain" flow, the platform framing plus the evidence/limitations transparency layer is the primary differentiation strategy.

**Design philosophy carried through every module:**
- Never present AI output as unqualified fact — always attach evidence + limitations
- Never simulate clinical authority — no diagnosis claims, no dosage changes, no percentage-based disease predictions
- Fail loud and isolated, not silent and cascading — one broken file, OCR call, or LLM call should never take down the rest of a batch or session
- Consent-first for any sharing — nothing is shared by default, everything shared is selected and revocable

---

## 2. Complete Feature Set (Phased)

### Phase 1 — Core (Must Build)
- Upload PDF/image (single or batch)
- OCR extraction (tiered pipeline: PyMuPDF → Docling → Sarvam Document Intelligence → GLM-4.6V-Flash)
- Report parsing into structured lab values, canonicalized against a standard parameter dictionary
- Abnormal value detection (High/Low/Normal), demographic-adjusted (age, gender, pregnancy)
- Overall AI health summary (plain language)
- Health Score (0–100), transparent and explainable formula
- Diet plan (foods to eat/avoid)
- Exercise recommendations
- Emergency/critical value alerts (a distinct tier above routine high/low)
- Downloadable PDF summary

### Phase 2 — AI Innovation (Must Build — primary judge-facing differentiator)
- RAG-powered AI chat with the uploaded report
- "Explain Like I'm 10" mode
- Multi-parameter health risk analysis (cross-value pattern reasoning — reasoning over combinations of abnormal values, not each independently)
- **Evidence-based recommendations** — every recommendation carries a `supporting_evidence` citation and a `limitations` caveat
- AI-generated questions to ask your doctor
- RAG grounded in trusted medical references (WHO/NIH/CDC/ICMR)

### Phase 3 — Value Addition (If Time Permits)
- Multi-language support (English/Hindi via Sarvam)
- Voice assistant (text-to-speech)
- AI medicine/prescription explainer — upload prescription, explain each medicine, generic name, active ingredient, medicine-specific AI chat
- Grocery recommendations
- Weekly/monthly trend graphs (multi-report timeline)

### Phase 4 — Stretch Goals (Only If Everything Else Works)
- Medicine reminders
- "Can I eat this?" checker (text or nutrition-label based, not full image recognition)

### Phase 5 — Bonus / Judge Surprise (Only If Time Left)
**Patient QR Health Card**
- Patient selects which reports to share (explicit per-item consent)
- AI generates a summary scoped to only the selected items
- A temporary, revocable health profile is created
- A QR code is generated, pointing to a temporary view-only link
- A doctor scans the QR and views the shared summary
- Deliberately scoped as a lightweight consent-driven sharing demo, not a records system

### Explicitly Out of Scope
Full EMR platform, hospital integration, permanent cloud record management, wearable/fitness tracker integration, predictive disease probabilities with percentages, AI changing medication or dosage, AI "what-if" simulator, family health dashboard, hospital cost estimator, community health insights, environmental health alerts, full image-based food scanner, human body visualization, AI doctor copilot. These are excluded because they either require clinical validation the project can't provide, introduce legal/medical liability disproportionate to hackathon scope, or need integrations (hospital systems, wearables) that can't be reliably demoed.

---

## 3. Tech Stack

| Layer | Choice | Rationale |
|---|---|---|
| Backend | **Python — FastAPI** | Async-native (needed for batch ingestion + status polling), auto-generated OpenAPI docs, plays to existing Python strength |
| Database | **SQLite** | Zero-infra, file-based, fully portable for a hackathon demo, sufficient for expected data volume |
| ORM | **SQLModel** (or SQLAlchemy) | Type-safe schema tied directly to FastAPI request/response models |
| OCR (reports) | Sarvam Document Intelligence (primary) → GLM-4.6V-Flash (vision fallback) → PyMuPDF → Docling (born-digital PDFs) | Tiered by document type — cheapest/fastest sufficient method tried first, escalate only when needed |
| OCR (prescriptions) | Same tiered pipeline, with heavier reliance on GLM-4.6V-Flash | Prescriptions are handwriting-heavy; vision-LLM fallback matters more here than for typed lab reports |
| LLM | GLM-4.5-Flash / GLM-4.6-Flash (primary, free tier) → Sarvam-105B (deep-reasoning fallback) | Cost-efficient default, escalates only when reasoning depth is needed (pattern analysis, complex chat turns) |
| RAG | FAISS (dense/semantic) + BM25 (sparse/keyword), combined via reciprocal rank fusion | Hybrid retrieval catches both paraphrased questions and exact medical terms; neither alone is sufficient |
| Frontend | **React + Tailwind CSS + shadcn/ui** | Fast to build, component-driven, fits a dashboard/card-heavy UI |
| Charts | **Recharts** | Health Score gauge, trend lines, risk meters |
| PDF generation | **ReportLab** (server-side, Python) | Consistent doctor-ready summary regardless of frontend state; generated once, not re-rendered per view |
| QR generation | Python `qrcode` library (server-side) | Generates a QR pointing to a temporary, revocable summary URL |
| TTS | Browser Web Speech API (or Sarvam TTS if available) | Avoids an extra backend integration for a Phase 3 nice-to-have |
| Batch ingestion | `asyncio.Queue` + in-process async worker pool | No external infra (Redis/Celery) needed at hackathon scale; explicitly framed in the pitch as "swappable for Celery/Redis at production scale" |
| Deployment (demo) | **ngrok** tunneling a local FastAPI server | Public HTTPS URL for judges without a full cloud deployment; tunnel must be started and verified well before the demo slot |

---

## 4. High-Level System Architecture

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
                        │  users · reports ·    │
                        │  prescriptions ·      │
                        │  values · jobs ·      │
                        │  chats · guidelines ·  │
                        │  shares               │
                        └──────────────────────┘
```

**What each engine owns:**

- **Ingestion Queue** — accepts lab reports and prescriptions; tiered OCR pipeline (PyMuPDF → Docling → Sarvam Document Intelligence → GLM-4.6V-Flash fallback); owns job lifecycle state
- **Analysis Engine** — demographic-adjusted normal-range comparison, severity scoring, critical-value alerts, cross-parameter pattern reasoning, Health Score computation
- **AI / RAG Engine** — hybrid FAISS + BM25 retrieval, recommendation generation with evidence + limitations, chat orchestration, medicine explainer
- **Sharing Module** — consent-based report selection, temporary profile creation, QR code generation, revocable share links

**Why this shape:** the four engines are deliberately independent — Analysis Engine never calls an LLM directly (it hands its output to the AI/RAG Engine), and the Sharing Module never touches OCR or analysis logic at all, only reads already-computed results. This separation means a bug or outage in one engine (e.g. an LLM API being slow) degrades only the features that depend on it, not the whole app — the dashboard's range/severity/Health-Score numbers still render even if the AI recommendation call is failing.

---

## 5. Module Breakdown

### 5.1 Ingestion Module
Accepts single or batch uploads of **either lab reports or prescriptions** — both document types route into the same queue but diverge at the parsing stage. Each file is an independent job with its own lifecycle:

`queued → extracting → parsing → analyzed/explained → completed` (or `failed`, with a stored reason)

One bad file (corrupted PDF, illegible scan) never blocks the rest of the batch — failure is isolated per job, and the frontend can show a per-file checklist ("Report 1: done ✓, Report 2: processing…, Report 3: failed — unreadable scan") rather than one blocking spinner for the whole batch.

**Concurrency model:** a small pool of async workers (3–4) pull jobs off the queue, so multiple files process concurrently rather than serially — this is what makes "upload 3 years of reports at once" a demoable moment instead of a slow sequential wait.

### 5.2 OCR / Extraction Module (tiered)
1. **PyMuPDF** text-layer check — instant, free, for born-digital PDFs (a report exported directly by a lab, not scanned)
2. **Docling** for table-structured extraction if tabular content is detected — preserves column alignment (parameter/value/unit/range) that raw text extraction would lose
3. **Sarvam Document Intelligence** if no text layer exists (scanned/photographed documents) — fully hosted API, no local GPU needed
4. **GLM-4.6V-Flash** vision fallback if Sarvam fails or times out — prompted directly with the image to return structured JSON, skipping a separate OCR-then-parse step; this tier matters especially for prescriptions, where handwriting recognition is the hardest case

All four paths normalize into a single schema: `{parameter_name, value, unit, source_method, confidence}`, tagged by document type (`lab_report` vs `prescription`). Downstream modules never need to know which tier produced the data.

**Failure handling within this module:** each tier has a timeout; if a tier times out or errors, the job automatically escalates to the next tier rather than failing outright. The job only reaches `failed` status if all four tiers are exhausted.

### 5.3 Parsing & Normalization
- **Lab reports:** maps lab-specific parameter names (e.g. "Hb", "Hemoglobin", "HGB") to a canonical dictionary, converts units where needed (mg/dL vs mmol/L), rejects/flags unparseable values rather than silently guessing at a number
- **Prescriptions:** extracts medicine name, dosage, frequency, duration as structured fields; resolves brand name → generic name → active ingredient via a drug-reference lookup (part of the RAG corpus)
- **Edge case handling:** a value that doesn't match any canonical parameter is stored as "unrecognized" and surfaced to the user rather than dropped silently — this avoids the false impression that "no abnormal values were found" when parsing actually failed

### 5.4 Range Comparison & Risk Engine (lab reports)
- **Demographic-adjusted normal ranges** — captured at onboarding (age, gender, pregnancy status); several markers (hemoglobin, creatinine, TSH, and others) have materially different normal ranges by gender and age, and pregnancy shifts several thyroid/blood ranges significantly. Using one generic range table is a correctness gap most competing teams will have; this module deliberately avoids it.
- **Severity scoring** per abnormal value — mild / moderate / severe, based on how far the value deviates from the range midpoint, not just a binary high/low flag
- **Critical-value alert tier** — a curated list of parameters with known dangerous thresholds, shown as a distinct, higher-priority alert from routine "high/low" flags (e.g. a red banner, not just a colored table row)
- **Cross-parameter pattern reasoning** — a rules layer first checks for known correlated-abnormality patterns (e.g. high glucose + high triglycerides + low HDL suggesting a metabolic-syndrome-type pattern; low hemoglobin + low MCV vs. low hemoglobin + high MCV suggesting different anemia types). If a candidate pattern is found, the abnormal value *set* is passed to the LLM to reason over the combination, not each value independently. This is the module that most directly demonstrates "we modeled the problem," not just "we ran an LLM over some numbers."
- **Health Score (0–100)** — a transparent, explainable weighted formula (e.g., weighted proportion of in-range parameters, adjusted down by severity of any abnormal ones). Deliberately not a black box — if a judge asks "how is this computed?" there's a clear, defensible answer.

### 5.5 AI Recommendation Engine
One structured LLM call per report producing:
- Plain-language explanation per abnormal value
- Cross-parameter pattern-level explanation (if a pattern was detected in 5.4)
- "Explain Like I'm 10" variant — same content, simpler framing, not a separate fact set
- Diet plan (foods to eat/avoid), exercise recommendations, lifestyle suggestions

Every recommendation is returned with:
- **Supporting evidence** — the guideline/source that backs it (surfaced as a citation in the UI, e.g. "based on ICMR dietary guidelines")
- **Limitations / considerations** — an explicit statement of what the recommendation does *not* account for (e.g., "based on this single reading; consult a doctor for a full evaluation")

This evidence + limitations structure is the core of the "explainable AI, not just an LLM wrapper" story, and it's the single most defensible answer to a judge pressing on medical-AI safety.

### 5.6 Medicine Explainer Module (Phase 3)
Takes parsed prescription data and, per medicine, generates: what it's for (plain language), generic name, active ingredient, common considerations (e.g. "commonly taken with food") — sourced via RAG against a drug-reference corpus. Never suggests dosage changes — this is a hard rule enforced at the prompt level, and worth explicitly testing (see testing section). Includes a medicine-specific chat scoped to that prescription, using the same chat architecture as report chat with a different context object.

### 5.7 RAG Layer
- **Two corpora:** (1) medical guideline references (WHO/NIH/CDC/ICMR) for report interpretation and diet/lifestyle guidance, (2) drug-reference data for the medicine explainer. Kept separate so a chat session about a prescription doesn't retrieve irrelevant dietary-guideline chunks and vice versa.
- **Hybrid retrieval:** FAISS (semantic) + BM25 (exact-term), combined via reciprocal rank fusion — catches both paraphrased questions ("why would iron be low") and precise term lookups ("TSH normal range")
- Every retrieved chunk is source-tagged; sources surface in the UI as citations, never as raw reproduced text (paraphrased/synthesized, not quoted)
- Backs three consumers: recommendation engine (5.5), report chat (5.8), medicine explainer chat (5.6) — one index, multiple consumers, so corpus quality improvements benefit the whole product at once

### 5.8 Chat Module
A conversation scoped to a specific report, a specific prescription, or (once multiple reports exist) the user's full history. Each turn's context: extracted structured data (values or medicine list) + RAG-retrieved chunks + recent conversation history. Deliberately constrained to grounded answers about the user's own data, not open-domain medical Q&A — a design choice worth stating explicitly in the pitch, since an unconstrained medical chatbot is a much harder trust problem than one scoped to "explain this specific report."

### 5.9 Doctor Questions Generator
One additional structured call using the same abnormal-value/pattern context as the recommendation engine, framed to output a short, specific list of questions worth asking a doctor at the next visit. This reframes "we found problems" into "here's how to act on it productively" — turns the analysis into next-step guidance rather than leaving the user with a list of flagged numbers and nowhere to go.

### 5.10 Trend & Timeline Module (Phase 3)
Once a user has 2+ reports: aligns the same parameter across report dates, computes % change and direction (rising/falling/stable), generates an AI trend narrative (e.g. "your HbA1c rose 12% over 8 months even though each single reading was only mildly high"), renders as a line chart per parameter. This is the single strongest demo line available — a static single-report analysis can miss a trajectory that matters more than any one reading, and saying so out loud is a genuinely differentiated claim against most competing teams' single-upload demos.

### 5.11 PDF Summary Module
Server-side (ReportLab) generation of a one-page clinical summary: patient info, flagged values with severity, AI summary, diet plan highlights, and (if prescriptions were uploaded) a medicine list. Respects the currently selected language. Generated once per report/language combination and cached rather than regenerated per download request.

### 5.12 Multi-language Module (Phase 3)
A language parameter threaded through recommendation, chat, and medicine-explainer prompts. Sarvam-105B generates bilingual content in a single call where possible (both languages in one structured response) so the UI language toggle switches between cached versions instantly, not a re-fetch — important for a smooth live demo where flipping the toggle in front of judges shouldn't introduce a loading delay.

### 5.13 Sharing Module — Patient QR Health Card (Phase 5)
1. Patient selects specific reports/summaries to share via checkboxes (explicit, per-item consent — never "share everything" by default)
2. System generates an AI summary scoped only to the selected items (not the user's full history)
3. A temporary health profile record is created (time-bounded, revocable)
4. A QR code is generated, encoding a link to a temporary, view-only summary page
5. A doctor scans the QR and views the shared summary
6. The patient can revoke the link at any time, immediately invalidating access

Framed explicitly as a consent-and-convenience demo, not a records system — no permanent storage beyond the temporary profile's validity window, and this framing should be stated explicitly to judges to preempt "is this HIPAA-compliant?"-style questions the demo isn't built to answer.

### 5.14 Auxiliary Phase 4 Modules
- **Medicine reminders** — simple scheduled reminder based on parsed prescription frequency/duration (local notification, not a clinical alerting system — no claim of reliability for actual medical adherence)
- **"Can I eat this?" checker** — text/nutrition-label input matched against a small reference table, answered via a RAG-grounded LLM call (deliberately not image recognition, to avoid scope creep and an extra vision-model dependency)

---

## 6. Database Schema (SQLite)

**users** — `id, name, age, gender, pregnant (bool), preferred_language, created_at`

**reports** — `id, user_id, doc_type ('lab_report'|'prescription'), uploaded_at, source_filename, extraction_method_used, status`

**extracted_values** — `id, report_id, parameter_canonical_name, raw_value, unit, normal_range_low, normal_range_high, severity, is_critical`

**prescriptions** — `id, report_id, medicine_name_raw, generic_name, active_ingredient, dosage, frequency, duration`

**risk_analysis** — `id, report_id, health_score, detected_patterns (json), summary_text_en, summary_text_hi`

**recommendations** — `id, report_id, explanation_json, eli10_json, diet_plan_json, exercise_json, evidence_sources (json), limitations_json, generated_at`

**doctor_questions** — `id, report_id, questions_json, generated_at`

**jobs** — `id, report_id, stage, status, error_reason, created_at, updated_at`

**chat_sessions** — `id, user_id, report_id (nullable), prescription_id (nullable), created_at`

**chat_messages** — `id, session_id, role, content, retrieved_sources (json), created_at`

**guidelines_corpus** — `id, source_name, source_url, chunk_text, embedding_vector, corpus_type ('guideline'|'drug_reference')`

**trend_snapshots** *(Phase 3)* — `id, user_id, parameter_canonical_name, report_date, value`

**shared_profiles** *(Phase 5)* — `id, user_id, included_report_ids (json), created_at, expires_at, revoked (bool), share_token`

**Relationships worth noting:** `extracted_values`, `recommendations`, and `risk_analysis` all key off `report_id` (one row per report), while `trend_snapshots` is deliberately denormalized (one row per parameter per date) so timeline queries don't require joining across multiple reports at read time — a query for "show glucose over time" is a single indexed lookup, not a multi-table join, which matters for a snappy trends UI during a live demo.

---

## 7. Detailed User Flow

**Step 1 — Onboarding (once per user).** Short form: age, gender, pregnancy status. Stored once, reused for every subsequent report's range lookups. Framed to the user as "this helps us give you accurate results," not as a generic signup form.

**Step 2 — Upload.** Drag-and-drop or file picker, accepts single or multiple PDFs/images. Document type (lab report vs. prescription) is either auto-detected or selected at upload — auto-detection is a nice-to-have, explicit selection is the safe fallback if detection proves unreliable under time pressure.

**Step 3 — Processing view.** Live per-file status checklist rendered from polling the batch status endpoint. Each row shows the file name and current stage (`extracting → parsing → analyzed → done`), with failed files shown distinctly and non-blockingly.

**Step 4 — Lab report results dashboard.** Health Score gauge front and center, severity-tagged parameter list below (color-coded), critical alerts banner at the top if any critical value was flagged — critical alerts should be visually impossible to miss, deliberately more prominent than routine abnormal flags.

**Step 5 — Drill into a value.** Tapping any parameter opens: plain-language explanation, an "Explain Like I'm 10" toggle, a language toggle, and — directly alongside the explanation, not hidden in a tooltip — the evidence source and stated limitation for that specific recommendation.

**Step 6 — Recommendations tab.** Diet plan (eat/avoid lists), exercise suggestions, lifestyle tips, each carrying a visible citation and limitation, consistent with Step 5's per-value pattern.

**Step 7 — Chat tab.** Free-text input, answers grounded in the user's own report data plus retrieved guideline sources, with sources shown alongside each answer.

**Step 8 — Prescription flow** *(Phase 3)*. Separate upload path or the same upload flow with `doc_type: prescription`. Results show per-medicine cards: generic name, active ingredient, plain-language purpose. A medicine-specific chat is available per prescription, separate from report chat sessions.

**Step 9 — Doctor questions.** Auto-generated list shown as a checklist the user can copy or check off — framed as "bring this to your next appointment," not as a substitute for one.

**Step 10 — Trends tab** *(Phase 3, requires 2+ reports).* Parameter selector, line chart per parameter, AI-generated narrative above the chart stating the actual direction and magnitude of change.

**Step 11 — Download.** One-click PDF summary generation/download in the currently selected language.

**Step 12 — Share via QR** *(Phase 5).* Checklist of the user's reports to select from, a "Generate Share Link" action that produces a QR code shown full-screen (for a doctor to scan directly off the user's device), and a visible "Revoke" button that immediately invalidates the link.

---

## 8. Detailed System / Data Flow (per uploaded document)

1. Upload request hits `POST /documents/batch` → for each file, a `reports` row is created with `status: queued` → a job message `{job_id, file_path, user_id, doc_type}` is pushed onto the in-process `asyncio.Queue` → the endpoint returns immediately with all job IDs (never blocks on processing)
2. An available worker in the pool picks up the job → `status: extracting` → runs the tiered OCR pipeline (5.2), escalating tiers only on timeout/failure
3. Extraction output → `status: parsing` → normalization against the canonical parameter dictionary (5.3); unrecognized values are stored and flagged rather than dropped
4. **If `doc_type: lab_report`:** demographic-adjusted range comparison → severity scoring → critical-value check → rules-based pattern candidate check → (if a pattern candidate exists) LLM pattern-reasoning call → Health Score computed and stored in `risk_analysis`
5. **If `doc_type: prescription`:** medicine fields extracted → generic name/active ingredient resolved via drug-reference RAG lookup → stored in `prescriptions`
6. Recommendation engine call (5.5): RAG retrieval over the relevant corpus → structured JSON generation (explanation + ELI10 + diet/exercise + evidence + limitations, bilingual) → stored in `recommendations`
7. Doctor-questions call (5.9), reusing the same abnormal-value/medicine context — a second, smaller structured call, not re-deriving context from scratch
8. Extracted data is embedded into the report-scoped RAG context (enabling chat in Step 7 of the user flow) and, for lab reports, appended to `trend_snapshots`
9. Job `status: completed` (or `failed`, with `error_reason` stored, if any stage exhausted its fallbacks) → frontend's next poll of `/documents/batch/{batch_id}/status` reflects the change → dashboard renders

**Chat flow (per message):** user message received → hybrid FAISS+BM25 retrieval over the relevant corpus (guideline corpus for report chat, drug-reference corpus for medicine chat) → retrieved chunks + the user's structured extracted values/medicine list + recent conversation history assembled as context → single LLM call → response returned with cited sources → both the user message and the response stored in `chat_messages`

**Share flow:** user selects report IDs on the frontend → `POST /share` with the selected IDs → summary regenerated or reused for just those reports (never the user's full history) → a `shared_profiles` row created with `expires_at` and a unique `share_token` → QR code encodes a URL containing the token → `GET /share/{share_token}` checks `revoked` and `expires_at` before rendering anything → `POST /share/{share_token}/revoke` flips `revoked` to true, and the next view attempt is denied immediately

---

## 9. API Surface (contract only, no implementation)

- `POST /users` — onboarding
- `POST /documents/batch` — upload N files (reports and/or prescriptions), returns job IDs
- `GET /documents/batch/{batch_id}/status` — per-file job polling
- `GET /reports/{report_id}` — full lab-report results (values, severity, health score, recommendations)
- `GET /prescriptions/{prescription_id}` — full medicine explanations
- `GET /reports/{report_id}/summary.pdf` — generate/download PDF
- `POST /chat/{session_id}/message` — send a chat message, get grounded response
- `GET /trends/{user_id}?parameter=...` — timeline data for a given parameter across reports
- `GET /trends/{user_id}/narrative` — AI-generated trend summary across all parameters
- `POST /share` — create a shared profile from selected report IDs, returns QR/token
- `GET /share/{share_token}` — doctor-facing view of the shared summary
- `POST /share/{share_token}/revoke`
- `POST /quiz/{user_id}`, `GET /challenge/{user_id}`, `POST /food-check` — if scoped in

---

## 10. Security / Privacy / Responsible-AI Design Notes

- Raw uploaded files retained only for the active session unless the user opts in to keep them (needed for trend tracking); this should be an explicit, visible opt-in, not a default
- Only structured extracted values persist long-term for history/trends, and only with explicit consent
- Every AI-generated health explanation carries a visible "not a medical diagnosis, consult a doctor" disclaimer
- Medicine explanations never suggest dosage changes — enforced at the prompt/system-instruction level and worth explicitly testing with an adversarial prompt during QA
- The evidence + limitations structure on every recommendation is both a UX feature and a responsible-AI safeguard — it prevents the product from presenting AI output as unqualified fact
- QR sharing is opt-in, per-item, and revocable — no default "share everything," no permanent record created beyond the temporary profile's validity window
- No health data is sent to third parties beyond the OCR/LLM API calls required to process it, and no data is used to train external models
- Critical value alerts explicitly recommend seeking medical attention rather than offering self-management advice

---

## 11. Full Build Phase Sequence (with test checkpoints)

**Phase 1 — Core:** ingestion queue, tiered OCR, parsing, demographic-adjusted range comparison, severity scoring, critical alerts, Health Score, base AI summary, diet/exercise recommendations, PDF export.
→ **Checkpoint:** full lab-report flow tested end-to-end on 3–4 real sample reports; classifications spot-checked by hand; critical-value path deliberately triggered and confirmed distinct from routine flags.

**Phase 2 — AI Innovation:** RAG corpus indexing (FAISS + BM25), recommendation engine upgraded to structured evidence + limitations format, ELI10 mode, cross-parameter pattern reasoning, report chat, doctor-questions generator.
→ **Checkpoint:** this is the primary demo differentiator — test more thoroughly than Phase 1. Verify every recommendation has a non-empty evidence + limitation field, manually spot-check 2–3 citations against their actual source, and rehearse the chat live as if presenting to a judge.

**Phase 3 — Value Addition:** multi-language, prescription upload + medicine explainer + medicine-specific chat, trend graphs, grocery recommendations, TTS.
→ **Checkpoint:** each sub-feature tested independently (bilingual toggle is instant, medicine explainer never suggests dosage changes even under an adversarial prompt, trend chart direction is numerically correct).

**Phase 4 — Stretch:** medicine reminders, "can I eat this" checker. Only start if Phases 1–3 are fully stable.

**Phase 5 — Bonus:** QR Patient Health Card sharing flow.
→ **Checkpoint:** QR tested by scanning with an actual second device; revoke tested to confirm immediate invalidation; unselected reports confirmed excluded from the shared summary.

**Final — Testing & demo prep:** full regression pass across all phases together (catch anything Phase 3/4/5 broke in Phase 1/2), tested across sample lab reports and prescriptions, both languages, chat sanity-checked, ngrok tunnel verified on the actual presenting device, demo script rehearsed with a pre-tested known-good sample set as a fallback in case of live OCR issues, full walkthrough timed and trimmed if it runs long.

---

*Document prepared for the AI Health Companion hackathon project — ~50 competing teams.*
