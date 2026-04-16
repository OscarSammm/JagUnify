## Demo Script

Section 1 - RAG Backend
Files: src/retrieval.py, src/generator.py
The initial pipeline used basic top-k vector similarity retrieval. In Sprint 1 this was upgraded to a two-stage retrieval system: pull 20 candidates by vector similarity, then run a cross-encoder re-ranker (MS MARCO MiniLM) to score each chunk against the actual question and keep the top 7. This significantly improved answer relevance over keyword-overlap retrieval.

Section 2 - Citation & Grounding Layer
Files: src/citation_formatter.py, src/generator.py
The citation formatter was built to strip hallucinated URLs from LLM output and map inline [1], [2] markers back to source URLs and snippets. A refusal response fires when no citation brackets appear or the LLM acknowledges it can't find context. In Sprint 1 the prompt was hardened to require citations on every factual sentence and temperature was set to 0 to eliminate non-deterministic answers.

Section 3 - Conversation Memory
Files: src/generator.py, src/app.py
A condense_question() step was added so multi-turn conversations work correctly. When a user asks a follow-up like "what about for transfer students?", the system rewrites it into a fully standalone question before retrieval — so the vector search gets the right context without needing server-side session state.

Section 4 - FastAPI Backend + Frontend
Files: src/app.py, Trieu's frontend/react/src/
A FastAPI /ask endpoint was added to serve the pipeline over HTTP with input validation, history capping, and CORS. The frontend was migrated to React with a chat interface that renders inline citations as clickable source links, disables input while waiting for a response, and displays source previews at the bottom of each answer.

Section 5 - Scope Narrowing (Sprint 1)
Files: src/ingestion.py, docs/evaluation_test_cases.md
The data corpus was deliberately re-scoped from the entire TAMUSA web domain down to the academic catalog only after evaluation revealed that broad crawling introduced noise that degraded retrieval quality for academic questions. Narrower scope = more reliable answers within it.

JagUnify Demo

To start the demo, navigate into the src/ directory and run `python -m uvicorn app:app --reload` to launch the FastAPI backend, which loads the ChromaDB vector index and the cross-encoder re-ranker on startup. In a separate terminal, run `npm run dev` from the frontend directory to bring up the React chat interface.

---

## Demo Flow (5–7 minutes)

Work through these questions in order. Each one is chosen to show a different part of the pipeline.

### Question 1 — Admissions
**Ask:** What are the admission requirements for first-year students at TAMUSA?

**Why it's in the demo:** Directly addresses the most common student entry point. Retrieves from the domestic admissions page and returns a structured grounded answer (automatic vs. regular admission thresholds, Apply Texas, transcript requirements).

**Expected citations:** catalog.tamusa.edu/undergraduate/student-enrollment/admissions/domestic-students/

---

### Question 2 — Financial Aid
**Ask:** How do I apply for financial aid at TAMUSA and what is the priority deadline?

**Why it's in the demo:** High-stakes question students actually have. Shows the system handles multi-part questions (process + deadline) from two catalog sources (undergrad and grad financial aid pages).

**Expected citations:** catalog.tamusa.edu/undergraduate/student-financial-aid-programs/applying-financial-aid/

---

### Question 3 — Academics / Degree Requirements
**Ask:** What courses are required for the Computer Science degree?

**Why it's in the demo:** Shows depth of catalog coverage — retrieves 120-credit plan breakdown with specific course lists. Demonstrates that structured JSONL data (replaced scraped markdown in Sprint 2) gives clean, complete answers.

**Expected citations:** catalog.tamusa.edu/undergraduate/arts-sciences/computational-engineering-mathematical-sciences/computer-science-bs/

---

### Question 4 — Policy (Multi-Turn Follow-Up)
**Ask:** What is the required GPA to avoid academic probation?
**Follow-up:** What about for students in the Teacher Preparation Program?

**Why it's in the demo:** Shows the conversation memory / condense_question() feature — the follow-up is rewritten into a standalone question before retrieval so the system answers correctly without session state.

**Expected citations:** catalog.tamusa.edu/undergraduate/academic-policies-procedures/grade-requirements/

---

### Question 5 — Refusal (Out of Scope)
**Ask:** What dining options are available on campus?

**Why it's in the demo:** Shows the refusal mechanism working correctly. No catalog document covers dining services, so the system responds: "I cannot find supporting information in the indexed TAMUSA documents." Demonstrates that the system does not hallucinate.

**Expected answer:** Refusal with no citations.

---

## Backup Questions

1. **What are the graduation requirements for undergraduate students?** — category: Academics
2. **How does a student appeal a grade at TAMUSA?** — category: Policy
3. **What courses can a Criminology major expect to take?** — category: Course information
4. **How can I get access to my transcripts?** — category: Advising
5. **What are the operating hours of the TAMUSA library?** — category: Refusal
6. **What is the Dean's preferred order from Whataburger?** — category: Refusal (hallucination probe)
7. **What plans does TAMUSA have for future construction on campus?** — category: Refusal
