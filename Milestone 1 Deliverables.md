# Milestone 1 Deliverables  
## Team: JagUnify  
### Focus: Grounded, Verifiable TAMUSA Campus Information Assistant  

---

## Context

- The team did not deliver a spike demo in the previous session.  
- You have been directed to focus the project on **grounded, verifiable responses using TAMUSA campus documents**.  
- All LLM outputs must be supported by citations and traceable to source documents.  

Milestone 1 must demonstrate that your system is a **grounded retrieval system**, not a generic chatbot.

---

# Milestone 1 Objective

By Milestone 1, your team must demonstrate:

- A working Retrieval-Augmented Generation (RAG) pipeline  
- TAMUSA campus documents ingested and indexed  
- LLM outputs grounded in retrieved content  
- Explicit citations included in every answer  
- Verifiable traceability to source documents  
- Measurable evaluation of grounding accuracy  
- Clean and professional GitHub organization  

---

# 1. Final PRD-Lite (1–2 pages)

Your PRD must clearly define the product as:

> A grounded TAMUSA campus information assistant with verifiable citations.

## The PRD must include:

### A. Problem Definition
- What problem students face (e.g., fragmented campus information)
- Why hallucinated answers are unacceptable
- Why grounding is required

### B. Target Users
- TAMUSA students (freshmen, transfer, etc.)
- Optional: faculty or staff use cases

### C. Grounding Requirement (Non-Negotiable)

Explicitly state:

- Every generated answer must cite at least one retrieved TAMUSA document
- Answers must not include information not present in retrieved sources
- If no relevant source is retrieved, the system must refuse to answer

### D. MVP Scope (April 5 Demo)

Must include:

- User question input
- Retrieval from indexed TAMUSA documents
- Answer generation
- Inline citation(s)
- Source preview (snippet display)

### E. Acceptance Criteria (Testable)

Examples:

- 100% of answers include citations
- No unsupported claims outside retrieved text
- System refuses when no supporting source exists
- Retrieval latency within acceptable limit

---

# 2. Working RAG Backend (Required)

You must implement:

- Document ingestion pipeline
- Chunking strategy
- Embedding + vector index
- Retrieval step (top-k configurable)
- LLM generation using retrieved context
- Citation formatting layer

Mock retrieval or hard-coded answers are not acceptable.

---

# 3. Document Ingestion & Indexing

You must demonstrate:

- TAMUSA campus documents collected (official sources only)
- Clear documentation of:
  - Source URLs
  - Date collected
  - Any preprocessing steps
- Chunking strategy explanation (size, overlap)

Create:

/docs/data_sources.md

This must list:

- All source URLs
- Type of document (policy, FAQ, handbook, etc.)
- Date indexed

---

# 4. Citation & Verification Layer

You must implement a citation mechanism that:

- Displays citation markers in output (e.g., [1], [2])
- Links to or references exact document sources
- Optionally shows snippet preview used in generation

If an answer cannot be supported, the system must respond:

"I cannot find supporting information in the indexed TAMUSA documents."

---

# 5. Evaluation Starter Kit (Minimum 20 Test Questions)

Create:

/docs/evaluation_test_cases.md

Include:

- 20 TAMUSA-related questions
- Expected source document(s)
- Retrieved document(s)
- Generated answer
- Verification status (Pass/Fail grounding)

Required metrics:

- Retrieval accuracy (% correct document retrieved)
- Grounding accuracy (% answer fully supported)
- Refusal accuracy (% correct refusals when no answer found)

---

# 6. Spike Recovery Document

Because no spike demo was delivered, you must submit:

/docs/spike_results.md

This must include:

- What was attempted
- Why demo was not delivered
- Current system status
- Revised architecture
- Clear plan to complete RAG pipeline before Milestone 2

---

# 7. Architecture Diagram (1 page)

Create:

/docs/architecture.png

It must clearly show:

User Question  
→ Query Embedding  
→ Vector Search  
→ Top-k Retrieval  
→ Context Injection  
→ LLM Generation  
→ Citation Formatting  
→ Output  

Label deterministic components vs LLM components.

---


# 8. Required Technical Walkthrough Video (No UI Required)

In addition to the live demo, you must submit a short technical walkthrough video (5–8 minutes).

This video must demonstrate:

- How documents are ingested and indexed  
- How embeddings are generated  
- How retrieval is executed (show top-k results in logs or console)  
- How retrieved context is passed into the LLM  
- How citation formatting is implemented  
- How refusal behavior is triggered when no grounding is found  

You must show:

- The actual source code files  
- The retrieval pipeline running (console/log output is acceptable)  
- The generated answer with visible citation mapping  

A polished UI is NOT required.  
This is an engineering verification video, not a product demo.

Acceptable format:
- Screen recording (MP4)  
- Linked in README or placed under `/docs/demo_video.mp4`  

If this technical walkthrough is missing, Milestone 1 is incomplete.

---
# 8. GitHub Repository Requirements

Your repository must include:

- /docs/PRD.md  
- /docs/data_sources.md  
- /docs/spike_results.md  
- /docs/evaluation_test_cases.md  
- /docs/architecture.png  
- /src/ingestion.py  
- /src/retrieval.py  
- /src/generator.py  
- /src/citation_formatter.py  

Additionally:

- Updated README with:
  - Clear project description
  - Setup instructions
  - How to ingest documents
  - How to run retrieval
  - Demo instructions
- requirements.txt
- .env.example
- At least one meaningful commit per team member
- Sprint 1 issue board with assigned owners

---

# Required Live Demo for Milestone 1

You must demonstrate:

1. A TAMUSA-related question
2. Retrieved documents displayed
3. Generated answer with inline citations
4. Source preview/snippet shown
5. A refusal case when no supporting source exists

If answers are generated without retrieval evidence, Milestone 1 is incomplete.

---

# Not Acceptable for Milestone 1

- Generic chatbot without document grounding
- No citations
- No source listing
- No retrieval evaluation
- Hard-coded answers
- No working backend pipeline

---

# Milestone 1 Standard

Your project must evolve from:

"We answer TAMUSA questions with GPT."

To:

"We engineered a grounded, citation-based campus information system with verifiable retrieval and measurable accuracy."

This is the expected senior-level standard.
