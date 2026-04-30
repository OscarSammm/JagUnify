# Final Demo — Dry Run Notes
**Date:** April 29, 2026 | **Branch:** `main` | **Model:** `gpt-4o-mini`

---

## Setup

- Backend started from `src/` via `python -m uvicorn app:app --reload`
- Frontend started from `frontend/` via `npm run dev` (Vite on `http://localhost:5173`)
- `.env` confirmed: `OPENAI_API_KEY` set, `CORS_ORIGIN=http://localhost:5173`
- ChromaDB index loaded from `src/storage/` (no rebuild needed)
- Startup message confirmed: `JagUnify advisor ready.`

---

## Scenarios Run

### 1. Admissions — Grounded answer with citations

**Question:** What are the admission requirements for first-year students at TAMUSA?

Live output: grounded answer with inline citations linking to `catalog.tamusa.edu/undergraduate/student-enrollment/admissions/domestic-students/`. Automatic admission criteria (top 35%, 3.0 GPA, SAT 1100+), regular admission path, and Apply Texas instructions cited correctly.

**Result:** PASS

---

### 2. Academic Policy — Multi-turn conversation

**Turn 1:** What is the required GPA to avoid academic probation?

Live output: 2.0 cumulative institutional GPA with citation to academic policies page. Teacher Preparation Program requirement (2.75) also surfaced.

**Turn 2:** What are the requirements for a Computer Science degree?

Live output: 120-credit BS plan with core, support, and major course breakdown. Multi-turn context preserved correctly — system treated this as a follow-up without re-explaining the prior answer.

**Turn 3:** What are the electives?

Live output: upper-division CS elective options retrieved from the degree plan page. History correctly condensed the prior turns to resolve "electives" as CS electives.

**Result:** PASS — multi-turn conversation maintained context across three turns.

---

### 3. Financial Aid

**Question:** What does the financial aid process look like?

Live output: FAFSA steps (studentaid.gov, school code 042485, October 1 open date), priority deadline April 15, JagWire monitoring, and degree-seeking enrollment requirement. Citations to both undergraduate and graduate financial aid pages.

**Result:** PASS

---

### 4. Refusal — Out-of-scope dining

**Question:** What dining options are available on campus?

No catalog document covers dining, so the system refuses rather than guessing.

Live output: `"I cannot find supporting information in the indexed TAMUSA documents."`

**Result:** PASS — clean refusal, no hallucination.

---

### 5. Refusal — Hallucination probe

**Question:** What NFL players graduated from TAMUSA?

**Question:** Are there any famous people on campus?

Live output: both returned the standard refusal. No fabricated names or unsupported claims.

**Result:** PASS — system correctly refused both hallucination probes.

---

## Timing

- Cold start (first query after uvicorn launch): ~8–12s — cross-encoder loads on first request
- Warm queries: ~3–6s
- No timeouts observed (30s frontend limit not triggered)

---

## Issues Observed

None. All scenarios completed without errors.
