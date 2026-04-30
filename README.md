# JagUnify

JagUnify is an AI-powered academic advisor chatbot for Texas A&M University–San Antonio students. It answers questions about degree requirements, admissions, financial aid, academic policies, and registration using official catalog sources — with verifiable citations.

## MVP Scope

**In Scope**
- TAMUSA undergraduate and graduate catalog content (`catalog.tamusa.edu`)
- Degree requirements (majors, credit hours, graduation criteria)
- Academic policies (GPA requirements, probation, appeals, registration)
- Admissions requirements (first-year and transfer)
- Financial aid (FAFSA process, eligibility, deadlines)
- Course and curriculum information from the catalog

**Out of Scope**
- Campus services not in the catalog (library hours, dining, housing, parking)
- Athletics, student life, and extracurricular activities
- Real-time or operational information (event schedules, office hours)
- External outcomes data (job placement, salaries, alumni info)
- Any non-TAMUSA or non-catalog sources

**Refusal Behavior**

The system refuses if no relevant catalog source is retrieved, the question falls outside the catalog domain, or the answer cannot be supported with at least one citation:

> "I cannot find supporting information in the indexed TAMUSA documents."

## Features

- Grounded answers with inline citations linking to official `catalog.tamusa.edu` pages
- Multi-turn conversation — follow-up questions retain prior context
- Clean refusal when a question falls outside the indexed catalog
- Two-stage retrieval: vector similarity (top 20) → cross-encoder reranker (top 7)
- React chat interface with campus background

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | React + Vite + Tailwind CSS |
| Backend | FastAPI (Python) |
| RAG Pipeline | LlamaIndex + ChromaDB |
| LLM | OpenAI `gpt-4o-mini` |
| Re-ranker | `cross-encoder/ms-marco-MiniLM-L-12-v2` |

## Data

The catalog index is built from `data/techdep_data/catalog.jsonl` — 2,028 structured records scraped from `catalog.tamusa.edu` by the TAMUSA technology department. Each record contains a `url`, `title`, and `full_body` field. The index is persisted to `src/storage/` (ChromaDB).

## Setup

### Prerequisites

- Python 3.10+
- Node.js 18+
- OpenAI API key with access to `gpt-4o-mini`

### Backend

1. Clone the repo and create a `.env` file in the project root (see `.env.example`):
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

2. Install Python dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Build the vector index (first time only — reads from `data/techdep_data/catalog.jsonl`):
   ```
   cd src
   python retrieval.py
   ```
   Expect ~2 minutes. If `src/storage/` already exists and is current, skip this step.

4. Start the backend:
   ```
   cd src
   python -m uvicorn app:app --reload
   ```
   Backend runs on `http://127.0.0.1:8000`. Startup confirms: `JagUnify advisor ready.`

### Frontend

1. Install dependencies:
   ```
   cd frontend
   npm install
   ```

2. Start the dev server:
   ```
   npm run dev
   ```
   Open the URL Vite prints (default `http://localhost:5173`).

## Example Interactions

**Grounded answer:** "What is the required GPA to avoid academic probation?"
> A minimum 2.0 cumulative institutional GPA is required to avoid academic probation. Students in the Teacher Preparation Program must maintain a 2.75. [1]

**Refusal:** "What are the dining options on campus?"
> I cannot find supporting information in the indexed TAMUSA documents.

## Evaluation

Tested against a 20-case suite (14 grounded + 6 refusal):

| Metric | Result |
|---|---|
| Retrieval Accuracy | 14/14 (100%) |
| Grounding Accuracy | 14/14 (100%) |
| Refusal Accuracy | 5/5 (100%) |

See `docs/evaluation_test_cases.md` for full case details.

## Project Status

Sprint 3 complete. Final demo delivered April 29, 2026. See `docs/Final_Demo/` for the runbook, slides, and demo video.

## Team

- Oscar Hernandez (Team Lead)
- Ian Arredondo
- Christian Hernandez
- Dustin Heagerty
- Trieu Do
