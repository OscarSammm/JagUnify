# Sprint 3 Plan — Venture 7: JagUnify

**Sprint Duration:** April 15 – April 21, 2026
**Sprint Goal:** Close Sprint 2 documentation follow-through gaps, refresh evaluation metrics, and lock down the final demo script (including admissions coverage).
**Final Demo:** April 29, 2026

---

## Context

Sprint 2 delivered strong engineering: the JSONL migration resolved TC12, fixed a request-lock bug, and cleaned up the repo. Contribution balance recovered, with every member committing. The gaps heading into Sprint 3 are documentation follow-through (Go/No-Go left blank, data sources table incomplete, chunk experiment without numbers, new refusal cases not executed) and one outstanding M2 demo gap (no admissions question). Sprint 3 is the last sprint before the final demo week, so anything that does not land this sprint will be a risk going into Sprint 4.

---

## Sprint 3 Tasks

### P0 — Finish What Sprint 2 Started (Days 1–3)

| Task | Owner | Description |
|---|---|---|
| Complete Go/No-Go assessment | Dustin | In `milestone2_status.md`, fill in the four justification bullets (Retrieval, Grounding, Refusal, System Stability) with concrete numbers from the latest evaluation run. Pick GO or NO-GO and record the decision. |
| Consolidate data sources documentation | Oscar | Merge `data_sources.md` and `data_sourcestable.md` into one file. With the JSONL migration, the "377 files" framing is outdated. Document the JSONL record types instead: what categories live in `catalog.jsonl`, how many records per category, which are in MVP scope. |
| Re-run chunk experiment with numbers | Oscar | Run the 20-case evaluation at chunk sizes 512, 1024, and 2048. Record actual pass counts, not qualitative labels. Update `chunk_experiments.md` with the numeric table and a real conclusion. |
| Execute refusal test cases 21–25 | Dustin | Fill in Retrieved Documents, Generated Answer, and Verification Status for the five new refusal cases. If any do not actually refuse, that is a Sprint 3 finding, not a failure. |
| Refresh metrics summary | Ian | Update the Metrics section of `evaluation_test_cases.md` to reflect TC12 passing, TC17 scope reclassification, and the new refusal cases. New numbers for retrieval, grounding, and refusal accuracy. |

### P1 — Demo Readiness (Days 2–5)

| Task | Owner | Description |
|---|---|---|
| Add admissions question to main demo script | Christian | `mvp_demo_script.md` still has no admissions or financial aid question. This was the M2 gap. Add at least one admissions question and one financial aid question to the main demo flow with expected answer and expected citations. |
| Finalize full demo flow | Christian + Ian | Lock in the exact sequence: intro, admissions question, academics question, financial aid question, grade appeal / policy question, refusal case, closing. 5 to 7 minutes total. |
| Dry run demo end to end | All | Full team runs through the demo at least once this sprint. Catch any runtime issues (JSONL index loads, Azure vs OpenAI branch selection, frontend startup) before they show up in Sprint 4. |
| Mobile demo verification | Christian | Confirm mobile demo video is in Google Drive and the link in `demo_video.md` resolves. If the video has not been recorded, record it this week. |

### P2 — Final Polish (Days 3–6)

| Task | Owner | Description |
|---|---|---|
| Citation tooltip or clear deprioritization | Trieu | Either land the citation hover tooltip from Sprint 2 P2, or explicitly remove it from the scope with a one-line note in `mvp_demo_script.md` about why. No in-between. |
| Error-state UX | Trieu | Add user-facing messages for backend-down and timeout cases. One commit, small scope. Matters for demo resilience if the backend stutters on stage. |
| ~~Decide on Azure vs OpenAI for demo~~ | Ian | **Decision made (April 15, 2026): Final demo will run on `main` branch (direct OpenAI, gpt-4o-mini).** The `feature/azure-ai` branch (gpt-4.1-mini) is preserved for enterprise use but will not be used on demo day. Rationale: `main` is fully tested, JSONL-backed, and has no Azure credential dependency risk on demo day. Azure branch is available as a future migration path if the tech department deploys an enterprise Azure environment. |

### P3 — Nice to Have (Days 5–7)

| Task | Owner | Description |
|---|---|---|
| Expand test coverage | Ian | Add 3 to 5 additional test cases covering admissions and financial aid (since these are now demo topics). Bring total to 28 to 30 cases. |
| README refresh | Christian | One pass over the top-level README to make sure setup instructions still match after the JSONL migration. |
| Architecture diagram update | Christian | If the architecture diagram still shows scraped markdown, update it to show the JSONL pipeline. |

---

## Definition of Done (Sprint 3)

- [ ] Go/No-Go assessment filled in with real numbers and a final GO or NO-GO decision — **Dustin**
- [ ] Single consolidated data sources file reflecting the JSONL record structure — **Oscar**
- [ ] Chunk experiment has numeric results against the 20 test cases — **Oscar**
- [ ] Refusal test cases 21–25 executed and marked PASS or FAIL — **Dustin**
- [x] Metrics section in evaluation doc refreshed with current numbers — April 16
- [x] Admissions question in main demo script — April 16
- [ ] Full team has done at least one end-to-end dry run
- [x] Branch decision made (Azure vs OpenAI) and documented — main/OpenAI, April 16

---

## Contribution Expectations

Oscar contributed three commits in Sprint 2, the first real activity since February. Keep that momentum, and this sprint's tasks (data sources consolidation + numeric chunk experiment) are substantial enough to prove re-engagement is sticking. Dustin has two cleanup tasks from work he started in Sprint 2 (Go/No-Go and refusal cases); finish both. Trieu should either land at least one frontend polish item or formally descope. Christian continues as demo owner. Ian's role is smaller this sprint since the JSONL migration already landed the big technical wins, but the branch decision and metrics refresh both need him.

---

## Remaining Sprints Overview

| Sprint | Dates | Focus |
|---|---|---|
| Sprint 3 (this sprint) | Apr 15–21 | Finish Sprint 2 docs, lock demo flow with admissions, numeric evaluation |
| Sprint 4 | Apr 22–28 | Final polish, slide deck, rehearsals, presentation prep |
| **Final Demo** | **Apr 29** | **Presentation and live demo** |
| Final Deliverables Due | May 3 | All documentation and code finalized |

---

## Risk Watch

- **Two active branches** (Azure OpenAI and OpenAI). Pick one before Sprint 4.
- **Stubbed documentation** (Go/No-Go, test cases 21–25). These look complete in the directory listing but are empty inside. Reviewers will notice.
- **Admissions coverage** still missing from main demo script. This has been flagged since M2; it has to land in Sprint 3.
- **Mobile demo** exists as a script but video verification is pending.

---

## Final Demo Day Heads-Up (April 29)

Two weeks out. Rehearse toward this format during Sprint 3 and Sprint 4.

**12 minutes per team, hard cap.** I will cut you off at 12:00 to keep all 8 teams on schedule, so rehearse to 10:30 or 11:00 to leave margin. Suggested split:

1. **About 3 min: overall design.** What the product does, the core pipeline, and the architectural decisions that matter (retrieval strategy, validator or grounding approach, refusal policy). No code walkthroughs.
2. **About 4 min: individual contributions.** Every team member speaks briefly about what they personally owned this semester. Plan what you will say, roughly 45 to 60 seconds each.
3. **About 4 min: live demo of the highlights.** Pick 2 or 3 scenarios from your existing demo script. Required: at least one refusal or failure case and at least one end-to-end grounded answer. Do not spend this time on UI polish.
4. **About 1 min: Q&A**, included in the 12 minutes.

**Running order** is Venture 1 through Venture 8 in order, so JagUnify presents seventh.

**Backup plan:** have a prerecorded screen capture of the working path ready in case the live demo fails. Internet or API hiccups are not an excuse on demo day.

**Slides and runbook:** not due before the presentation, but both are required artifacts in the final deliverables package due May 3. Save them under `docs/Final_Demo/` in your repo.

**Avoid:** narrating code, reading slides verbatim, skipping the refusal case, opening with missing features. Present the version you are proud of.

Rehearse the full 12 minutes end to end at least twice, at least once with a timer.
