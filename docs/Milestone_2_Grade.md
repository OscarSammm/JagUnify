# Milestone 2 Grade — Venture 7: JagUnify

**Graded:** April 8, 2026
**Deadline:** April 5, 2026 (end of day)
**Late Commits:** None — all 53 commits are on or before 4/5/2026.

---

## Overall Grade: 92/100

---

## Summary

JagUnify is one of the strongest technical submissions. The team built a working campus information assistant with a complete RAG pipeline: 377 markdown files scraped from catalog.tamusa.edu, ChromaDB vector indexing with LlamaIndex, two-stage retrieval with a cross-encoder re-ranker, GPT-4o-mini generation with strict grounding prompts (temperature=0), citation formatting with source URL mapping, and a React frontend with clickable inline citations and source display. The evaluation is honest and thorough (20 test cases with documented failures). The scope was deliberately narrowed to catalog-only for reliability — a strong engineering judgment call. Weaknesses are primarily in documentation completeness and contribution balance.

### Video Review Notes
The demo video is ~12 minutes (first 6 min = code walkthrough, last 6 min = live demo). **Strengths:** Thorough code walkthrough showing ingestion, retrieval (two-stage with cross-encoder re-ranker), citation formatter, and generator prompt engineering. Live demo shows GPA/academic probation question answered with inline citations, credit requirements for bachelor's degree answered, grade appeal process answered — all with clickable citation links verified against real TAMUSA catalog pages. Clean refusal: "What are the operating hours of the library?" returns "I cannot find supporting information." **Gaps:** (1) **No admissions or financial-aid question demonstrated** — requirements explicitly require this; all questions were academic policy. (2) Retrieved source chunks/scores not visually shown in UI — only clickable links. (3) Scope narrowed to catalog-only without showing scope freeze on screen. (4) False refusal on "MOUSA" abbreviation reveals retrieval fragility. For the final demo, include admissions/financial-aid questions and show source evidence visibility.

---

## Category Breakdown

### 1. End-to-End Demo Path (24/25)
- Full RAG pipeline: ingestion → vector indexing → two-stage retrieval (20 candidates → re-rank → top 7) → grounded generation → citation formatting. ✓
- Cross-encoder re-ranker (`ms-marco-MiniLM-L-12-v2`) for retrieval quality — excellent engineering choice. ✓
- Strict grounding prompt enforcing citation on every sentence, refusal when no context. ✓
- Citation formatter: strips hallucinated URLs, validates brackets, renumbers continuously, builds source list. ✓
- FastAPI backend with input validation (500-char limit, 10-turn history cap). ✓
- Multi-turn conversation support via `condense_question()`. ✓
- React frontend with clickable amber citation links and Sources section. ✓
- TAMUSA-themed UI with campus background. ✓
- **Minor:** Request locking (one request at a time) could be a demo bottleneck.

### 2. Code Quality & Architecture (19/20)
- Clean module separation: `ingestion.py`, `retrieval.py`, `generator.py`, `citation_formatter.py`, `app.py`.
- LlamaIndex + ChromaDB + OpenAI integration is well-architected.
- Pydantic models for request validation. ✓
- CORS properly configured. ✓
- 1024-token chunks with 50-token overlap using SentenceSplitter. ✓
- Frontend components cleanly separated (ChatWindow, MessageBubble, ChatInput). ✓
- Tailwind CSS with consistent theming. ✓
- **Issue:** Generator.py contains an embedded test harness (all 20 evaluation cases) — should be in a separate test file.
- **Issue:** 103MB demo video committed to repo (should use Git LFS or external link).

### 3. Documentation & Deliverables (22/25)
- `Milestone 2 Deliverables.md` — comprehensive requirements spec. ✓
- `evaluation_test_cases.md` — 20 test cases with metrics and "what changed since Sprint 1" section. ✓
- `mvp_demo_script.md` — has demo order, questions, expected behavior, refusal example. ✓
- `milestone2_status.md` — brief but covers complete/in-progress/risky/ownership. ✓
- README — excellent, with scope statement, in/out of scope, refusal behavior, setup instructions. ✓
- `.env.example` with OpenAI key and CORS config. ✓
- `requirements.txt` present. ✓
- `sprint_board.md` with task ownership. ✓
- **Issue:** `data_sources.md` is a flat file list — missing required columns (source category, type, date collected, MVP inclusion status).
- **Issue:** PRD not updated to reflect catalog-only scope narrowing (still mentions "Advising, Financial Aid, Tutoring, IT").
- **Issue:** `mvp_demo_script.md` doesn't include backup questions (required by spec).
- **Issue:** `milestone2_status.md` has no explicit go/no-go assessment.

### 4. Evaluation Evidence (14/15)
- 20 test cases with clear pass/fail and root cause analysis.
- Retrieval accuracy: 92%, Grounding accuracy: 100%, Refusal accuracy: 83%.
- Honest failure reporting: TC12 (graduate program gap), TC17 (parking query returns grounded answer instead of refusing). ✓
- "What changed since Sprint 1" section documenting improvements. ✓
- **Minor:** Could benefit from more refusal test cases.

### 5. Repository Hygiene (13/15)
- `.gitignore`, `.env.example`, `requirements.txt` all present. ✓
- Clean project structure. ✓
- **Issue:** 103MB demo video in repo — should be external or Git LFS.
- **Issue:** Duplicate PRD.md (root and docs/).

---

## Individual Grades

| Team Member | Commits | Contribution Area | Grade |
|---|---|---|---|
| 1anArr3d (Ian Arredondo) | 19 | Core RAG pipeline, FastAPI backend, citation system, re-ranker, evaluation — primary engineer | 97/100 |
| T Do (Trieu Do) | 14 | Frontend (React migration, UI polish, source links, input behavior), setup docs | 93/100 |
| Christian Hernandez | 7 | Architecture diagram, sprint board, widget, README for M2, documentation | 85/100 |
| dustinheagerty (Dustin Heagerty) | 7 | PRD, spike recovery report, evaluation test cases, scope statement | 85/100 |
| OscarSammm (Oscar Hernandez) | 5 | Initial project setup (PRD, spike plan, README) — should increase contributions for final sprint | 65/100 |

**Note:** Ian built the core RAG pipeline and Trieu built the frontend — strong engineering work. Oscar should increase contributions for the final sprint. Christian and Dustin contributed documentation and should take on more coding tasks going forward.

---

## Key Recommendations for Sprint 2
1. Complete `data_sources.md` with required columns (category, type, date collected, MVP inclusion).
2. Update PRD to reflect catalog-only scope narrowing.
3. Add backup questions to demo script.
4. Add explicit go/no-go assessment to status doc.
5. Move 103MB demo video out of repo (use external link or Git LFS).
6. Extract test harness from generator.py into separate test file.
7. Oscar must begin contributing code immediately.
8. Address TC12 (graduate programs) and TC17 (parking) failures.
