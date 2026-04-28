# Sprint 3 Grade, Venture 7: JagUnify

**Graded:** April 28, 2026
**Sprint Window:** April 15 – April 24, 2026 (extended from April 21)
**Final Demo:** April 29, 2026
**Final Deliverables Due:** May 3, 2026

---

## Overall Grade: 85/100

**Note on individual grades:** This is the venture-level grade. Members who severely under-contributed during Sprint 3 may receive a reduced individual grade applied separately.

**Note on grading scope:** Final-presentation prep items (rehearsal logs / dry-run notes, slide deck drafts, pitch deck refreshes, backup recordings) are not counted against the Sprint 3 grade. They appear in the "Items to Complete by May 3" section instead.

---

## Summary

Sprint 3 made real progress on demo-readiness items but left two of the five P0 items incomplete even with the extended deadline. What did land: the metrics summary in `evaluation_test_cases.md` was refreshed, the admissions question was added to the main demo script, the mobile demo doc and link landed, the branch decision (run on `main` with direct OpenAI for Apr 29) is documented and final, the Go/No-Go assessment in `milestone2_status.md` was filled in with concrete numbers and a final GO decision, refusal test cases TC21-25 were executed and marked PASS, the citation tooltip and backend-down/timeout error UX were both shipped, and the architecture diagram was refreshed.

What did not land:

- **Data sources documentation is still split across two files** (`data_sources.md` and `data_sourcestable.md`). The plan called for consolidating into one file with the JSONL record framing replacing the outdated "377 files" framing.
- **The chunk experiment is still qualitative**. `chunk_experiments.md` records "Medium / High / Low" labels for chunk sizes 512/1024/2048 rather than the per-chunk numeric pass counts on the 20-case suite the plan asked for. The file was last touched April 14, before Sprint 3 started.

Both missing items are P0s owned by Oscar in the plan. Oscar had zero commits during the sprint window or the extended window. The plan called Oscar's Sprint 2 re-engagement out as the key signal Sprint 3 was watching for; that signal did not hold this sprint. The plan also called Trieu out for either landing one frontend polish item or formally descoping; Trieu landed both polish items (citation tooltip and error UX) on Apr 24. That is the right outcome but the timing was tight.

The end-to-end dry-run rehearsal that the plan called for in Sprint 3 is treated as a final-prep item and does not count against the Sprint 3 grade. It is listed in the May 3 deliverables section instead.

The grade is held at 85 because the venture-level deliverables shipped enough for the final demo (the refusal cases, admissions question, error UX, tooltip, architecture diagram are all useful demo artifacts), but two P0 documentation tasks remain unfinished.

---

## Category Breakdown

### 1. Task Completion (33/40)

**P0 (3 of 5 complete):**
- Go/No-Go assessment: shipped (`milestone2_status.md` has the four justification bullets with numbers and a GO decision).
- Refresh metrics summary: shipped (Ian Apr 16).
- Refusal test cases TC21-25: shipped (Dustin Apr 24-25, executed and marked PASS).
- Consolidate data sources documentation: not done. Both `data_sources.md` and `data_sourcestable.md` still exist.
- Re-run chunk experiment with numbers: not done. `chunk_experiments.md` still uses qualitative labels and was last touched Apr 14.

**P1 (3 of 3 graded; dry-run rehearsal deferred to final-prep):**
- Admissions question in main demo script: shipped (Ian Apr 16).
- Finalize full demo flow: shipped.
- Mobile demo verification: shipped (`mobile_demo.md`, Christian Apr 19).
- Dry-run demo end-to-end: deferred to final-prep (May 3 deliverables).

**P2 (3 of 3 complete):**
- Citation tooltip: shipped (Trieu Apr 24).
- Backend-down / timeout error UX: shipped (Trieu Apr 24).
- Branch decision (Azure vs OpenAI): shipped (`main` + direct OpenAI, documented).

**P3 (2 of 3 complete):**
- Expand test coverage: partial (Dustin updated `evaluation_test_cases.md`).
- README refresh: not visible as a discrete Sprint 3 commit.
- Architecture diagram update: shipped (Christian Apr 23).

### 2. Code Quality (18/20)

- Citation tooltip and error-state UX are clean front-end additions.
- The "main" branch is now the canonical demo branch with OpenAI direct integration; the `feature/azure-ai` branch is preserved as a future migration path.
- Chunk experiment file remains stale; this is a code-adjacent quality issue because the conclusion ("use 1024") is not numerically defended.

### 3. Documentation (12/15)

- Go/No-Go is now real; refusal cases are documented with PASS verdicts.
- Architecture diagram is current.
- Data sources documentation is split across two files. A grader looking for "where does the data come from" sees inconsistent framing.
- Chunk experiment doc has a conclusion that the data does not back up.
- No rehearsal log.

### 4. Testing / Evaluation (14/15)

- Refusal cases TC21-25 executed and marked PASS, with notes.
- Metrics section refreshed with TC12 passing and TC17 reclassification.
- Chunk experiment numbers were never produced this sprint.

### 5. Team Contribution (8/10)

| Member | In-window Commits | Sprint 3 Work | Signal |
|---|---|---|---|
| Christian Hernandez | 4 | Mobile demo doc, architecture diagram refresh | Active |
| T Do (Trieu) | 3 | Citation tooltip, backend-down/timeout error UX, delete chat history button | Active (Apr 24, late) |
| Dustin / dustinheagerty | 2 | Go/No-Go refresh, TC21-25 refusal cases | Active (Apr 24, late) |
| Ian / 1anArr3d | 1 | Sprint 3 doc consolidation (metrics, demo script, branch decision) | Light commit count, real work |
| Oscar / OscarSammm | 0 | None | **Concern** |

Oscar's zero contribution is the single largest issue this sprint. Oscar owned both of the missed P0 items (data sources consolidation, numeric chunk experiment). The Sprint 3 plan named Oscar's Sprint 2 re-engagement (3 commits) as the signal Sprint 3 was watching for; that did not sustain.

---

## Per-Task Completion Status

| Priority | Task | Owner | Status |
|---|---|---|---|
| P0 | Complete Go/No-Go assessment | Dustin | Done |
| P0 | Consolidate data sources documentation | Oscar | Not done |
| P0 | Re-run chunk experiment with numbers | Oscar | Not done (still qualitative) |
| P0 | Execute refusal test cases 21-25 | Dustin | Done |
| P0 | Refresh metrics summary | Ian | Done |
| P1 | Admissions question in demo script | Christian | Done |
| P1 | Finalize full demo flow | Christian + Ian | Done |
| P1 | Dry run demo end to end | All | Deferred to final-prep |
| P1 | Mobile demo verification | Christian | Done |
| P2 | Citation tooltip | Trieu | Done |
| P2 | Backend-down / timeout error UX | Trieu | Done |
| P2 | Branch decision (Azure vs OpenAI) | Ian | Done |
| P3 | Expand test coverage | Ian | Partial |
| P3 | README refresh | Christian | Not visible |
| P3 | Architecture diagram update | Christian | Done |

---

## Definition of Done (Sprint 3) Check

- [x] Go/No-Go assessment filled with real numbers and a final decision
- [ ] Single consolidated data sources file reflecting JSONL record structure
- [ ] Chunk experiment has numeric results against the 20 test cases
- [x] Refusal test cases TC21-25 executed and marked PASS or FAIL
- [x] Metrics section refreshed with current numbers
- [x] Admissions question in main demo script
- [~] Full team has done at least one end-to-end dry run (deferred to final-prep)
- [x] Branch decision documented (main / OpenAI)

---

## Items to Complete by May 3 (Final Deliverables)

The May 3 package is required to be under `docs/Final_Demo/` in the repo. Save the following items there:

1. **Final demo slides** (PDF or PPTX) under `docs/Final_Demo/`. Cover: problem (TAMUSA campus info), JSONL pipeline, retrieval + grounding + refusal, evaluation numbers, live-demo plan covering admissions + grounded academic Q + refusal.
2. **Runbook** at `docs/Final_Demo/Runbook.md`. Cover: prerequisites, env setup (OPENAI_API_KEY), how to start backend on `main`, how to start frontend, the JSONL data layout, how the catalog scope is enforced, common errors, the Azure branch as a future migration path.
3. **Final demo video** at `docs/Final_Demo/Final_Demo_Video.mp4`.
4. **Final code on `main`**. Confirm `main` reflects the demo state and the Azure branch remains preserved but not active.

Sprint 3 carryovers that should land before May 3:

5. **Consolidate data sources documentation** into a single `docs/data_sources.md`. Replace the outdated "377 files" framing with JSONL record types: what categories live in `catalog.jsonl`, how many records per category, which are in MVP scope. Delete `data_sourcestable.md` after merge. This was a P0 from the Sprint 3 plan and remains the most visible documentation gap.
6. **Re-run chunk experiment with numeric results**. Run the 20-case evaluation at chunk sizes 512, 1024, and 2048. Replace the "Medium / High / Low" labels in `chunk_experiments.md` with actual pass counts. Keep the "Use 1024" conclusion only if the numbers support it. This was also a P0.
7. **Document a full end-to-end dry run** at `docs/Final_Demo/dry_run_notes.md`. Run the full Apr 29 flow on a clean machine (JSONL load, frontend startup, admissions question, academics question, financial aid question, refusal). Capture timing and any glitches.
8. **README refresh** to confirm setup steps still match after the JSONL migration.

Items 5 and 6 are the largest gaps and the most useful to close before the final-deliverables review.
