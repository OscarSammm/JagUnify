# Data Sources — JagUnify
**Last updated:** 2026-04-30

---

## Primary Data Source

**Source:** Texas A&M University – San Antonio Academic Catalog  
**URL:** `catalog.tamusa.edu`  
**Format:** JSONL (`data/techdep_data/catalog.jsonl`)  
**Records:** 2,028  
**Provided by:** TAMUSA Technology Department  
**Collection method:** Crawl of `catalog.tamusa.edu`; each page converted to a structured JSON record

---

## Record Structure

Each record in `catalog.jsonl` represents one page from the TAMUSA academic catalog and contains:

| Field | Description |
|---|---|
| `url` | Canonical URL for the catalog page |
| `title` | Page title |
| `full_body` | Full text content of the page |

---

## Coverage by Category

| Category | Description | Approx. Records |
|---|---|---|
| Undergraduate Programs | Degree plans, concentrations, minors, certificates (BS, BA, BBA, BAAS, BGS) | ~600 |
| Graduate Programs | Master's and certificate programs (MS, MA, MBA, MPA, MEd) | ~250 |
| Course Listings (UG) | Undergraduate course descriptions by department prefix (A–Z) | ~550 |
| Course Listings (Grad) | Graduate course descriptions by department prefix | ~200 |
| Academic Policies | Registration, grades, probation, graduation, degree requirements, attendance | ~120 |
| Admissions | Domestic, international, transfer admissions, TSI, Academic Fresh Start | ~60 |
| Financial Aid | FAFSA, loans, scholarships, disbursement, SAP policy | ~120 |
| Student Services | Academic resources, military affairs, Title IX, student life | ~50 |
| Administrative | Board of Regents, university administration, faculty roster | ~78 |

---

## MVP Scope

All 2,028 records are indexed in the ChromaDB vector store under `src/storage/`. The retrieval pipeline retrieves the 20 most semantically similar chunks per query and passes the top 7 through the cross-encoder reranker before LLM generation.

---

## Explicitly Out of Scope

The following are **not** present in `catalog.tamusa.edu` and are therefore out of JagUnify's scope. Queries on these topics trigger a clean refusal.

- Dining and meal plans
- Athletics and sports
- Campus parking operations and maps
- Library hours and services
- Weather and campus events
- Admission requirements for other universities
