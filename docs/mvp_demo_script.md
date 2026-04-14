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

To start the demo, I navigated into the src/ directory and ran python -m uvicorn app:app --reload to launch the FastAPI backend, which loaded the ChromaDB vector index and the cross-encoder re-ranker on startup. In a separate terminal, I ran npm run dev from the frontend/ directory to bring up the React chat interface. From there, I walked through a series of grounded academic questions, each returning cited answers with source links mapped back to the official TAMUSA catalog, before finishing with a refusal case to demonstrate the system's out-of-scope behavior.

---

## Backup Questions:

1. What are the hours of Student Business Services?

category: Administrative

2. How can I get access to my transcripts?

category: Advising

3. What courses can a Criminology major expect to take?

category: Course information

4. What is the Dean's preferred order from Whataburger?

category: Refusal

5. What plans does TAMUSA have for future construction on campus?

category: Refusal
