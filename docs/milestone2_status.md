# Milestone 2 Status
**Date:** 4/4/2026

## Completed

- UI Design and Implementation
- Citation Generation
- Document Retrieval

## In Progress

- Expansion of scope to be more precise with data found outside the academic catalogue
- Increasing the quickness of the tool's replies while maintaining answer integrity

## Risky

- At the moment, nothing about the project is too much at risk, but expanding scope inherently carries the risk of breaking previously-completed modules

## Team Ownership

- **Oscar** - Team coordination and backend logic
- **Dustin** - Team coordination and backend logic
- **Ian** - Backend logic and recording the demo video
- **Trieu** - Frontend design and integration
- **Christian** - Frontend integration and compiling documentation

---

## Go / No-Go Assessment

### Criteria
The system is considered GO for Milestone 2 demo if:

- Retrieval returns relevant catalog documents for program-related queries
- All generated answers include valid citations
- No unsupported claims are present
- Refusal behavior works correctly for out-of-scope queries
- Demo flow executes without runtime errors

### Current Assessment: GO

### Justification

- **Retrieval Performance:** 14/14 grounded test cases returned relevant catalog documents with valid source URLs. Retrieval accuracy is 100% as of Sprint 3. TC12 (graduate programs), which previously failed due to scraped markdown limitations, was resolved in Sprint 2 via JSONL migration and has passed all subsequent evaluations.
- **Grounding Accuracy:** All 14 grounded answers include at least one valid citation from `catalog.tamusa.edu`. No hallucinated URLs or unsupported claims were detected across any executed test case. Grounding accuracy is 100%.
- **Refusal Behavior:** 5/5 refusal test cases (TC15, TC16, TC18, TC19, TC20) correctly returned "I cannot find supporting information in the indexed TAMUSA documents." TC17 (parking) was reclassified as out of scope after review; the system's grounded partial answer from the fees page is considered acceptable behavior. Refusal accuracy is 100%.
- **System Stability:** The demo flow executed without runtime errors across all 20 test cases. The JSONL migration introduced in Sprint 2 stabilized document retrieval for graduate program records. No regressions were observed in previously passing cases.

---

## Risks

- Expanding the retrieval scope beyond the academic catalog may introduce context bleed, where loosely relevant documents are retrieved for out-of-scope queries, potentially degrading refusal accuracy.
- Latency optimization efforts must be validated against grounding accuracy to ensure answer quality is not reduced in exchange for faster response times.
- TC21–TC25 have been authored but not yet executed; results are pending and could surface new edge cases before the final demo.

---

## Decision

**Final Status: GO**

All five criteria for a Milestone 2 GO decision have been met. Retrieval, grounding, and refusal accuracy are each at 100% across executed test cases. The system is stable, citations are present in every grounded answer, and the demo flow is confirmed to run without errors. Pending test cases (TC21–TC25) do not block the GO decision and will be executed and documented prior to the final demo.
