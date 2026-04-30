# JagUnify Runbook
**Branch:** `main` | **Demo Date:** April 29, 2026

---

## Prerequisites

- Python 3.10+
- Node.js 18+
- An OpenAI API key with access to `gpt-4o-mini`
- Git clone of this repo on `main`

---

## Environment Setup

Create a `.env` file in the project root (`JagUnify/JagUnify/.env`):

```
OPENAI_API_KEY=your_openai_key_here
CORS_ORIGIN=http://localhost:5173
```

`CORS_ORIGIN` must match the port Vite starts on. Vite defaults to `5173`; if that port is taken it increments to `5174` — update accordingly.

Install Python dependencies from the project root:

```
pip install -r requirements.txt
```

Install frontend dependencies:

```
cd frontend
npm install
```

---

## Starting the Backend

From the `src/` directory:

```
cd src
python -m uvicorn app:app --reload
```

On startup you will see:

```
JagUnify advisor ready.
INFO: Application startup complete.
```

The cross-encoder model (`cross-encoder/ms-marco-MiniLM-L-12-v2`) loads on first startup and prints a harmless `UNEXPECTED` warning about `bert.embeddings.position_ids` — this can be ignored.

Backend runs on `http://127.0.0.1:8000`.

---

## Starting the Frontend

In a separate terminal, from the `frontend/` directory:

```
cd frontend
npm run dev
```

Vite will print the local URL (default `http://localhost:5173`). Open that URL in the browser.

---

## JSONL Data Layout

The catalog index is built from `data/techdep_data/catalog.jsonl`. Each record is a structured JSON object representing one page from `catalog.tamusa.edu`. Records include fields such as `url`, `title`, and `full_body`.

The index is persisted to `src/storage/` (ChromaDB). If `src/storage/` does not exist or is stale, rebuild it:

```
cd src
python retrieval.py
```

This wipes any existing storage and rebuilds from `catalog.jsonl`. Expect ~2 minutes on first run.

---

## How Catalog Scope Is Enforced

JagUnify answers questions using only content retrieved from the indexed catalog records. Scope is enforced at two levels:

1. **Retrieval:** ChromaDB returns the 20 most semantically similar chunks. The cross-encoder reranker scores each chunk against the query and passes the top 7 to the LLM. If no relevant chunks exist, scores are low and no useful context reaches the model.

2. **Grounding prompt:** The system prompt requires an inline citation (`[1]`, `[2]`, etc.) on every factual sentence. If the LLM cannot ground a claim in a retrieved chunk, it must refuse. The `citation_formatter.py` strips any URL the LLM fabricates and maps each citation marker to a verified source URL from the index.

Out-of-scope questions (dining, athletics, parking, other universities) trigger a clean refusal: `"I cannot find supporting information in the indexed TAMUSA documents."`

---

## Common Errors

| Symptom | Cause | Fix |
|---|---|---|
| `Cannot reach backend` | Backend not running or CORS mismatch | Start uvicorn; check `CORS_ORIGIN` matches Vite port |
| `Request timed out` | Reranker + OpenAI call exceeded 30s | Retry; first query after cold start is slowest |
| `Backend error. Check server logs.` | 500 from FastAPI — usually missing API key or malformed request | Check `OPENAI_API_KEY` is set in `.env`; check uvicorn logs |
| `UNEXPECTED` warning on startup | Cross-encoder loaded from a different architecture | Harmless — ignore |
| Stale retrieval results | `src/storage/` built from old scraped markdown data | Delete `src/storage/` and run `python retrieval.py` |
| `uvicorn: command not found` | uvicorn not on PATH | Use `python -m uvicorn app:app --reload` |

---

## Azure OpenAI Branch

The `feature/azure-ai` branch contains an integration with Azure OpenAI (`gpt-4.1-mini` via `https://jagbot.openai.azure.com/`). It is preserved as an enterprise migration path for when the university deploys a managed Azure environment.

**Do not use this branch for the demo.** `main` with direct OpenAI is the tested, stable path. The Azure branch introduces a credential dependency (`AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT`) that adds risk on demo day with no benefit.

To switch to Azure in the future:

```
git checkout feature/azure-ai
```

Then set the following in `.env`:

```
AZURE_OPENAI_ENDPOINT=https://jagbot.openai.azure.com/
AZURE_OPENAI_API_KEY=your_azure_key
AZURE_OPENAI_DEPLOYMENT=gpt-4.1-mini
```
