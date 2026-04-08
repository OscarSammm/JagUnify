# Sprint 2 Plan — Venture 7: JagUnify

**Sprint Duration:** April 8 – April 14, 2026
**Sprint Goal:** Complete documentation gaps, address retrieval failures, and ensure Oscar contributes meaningfully.
**Final Demo:** April 29, 2026

---

## Context

After Milestone 2, JagUnify has one of the strongest technical implementations: a full RAG pipeline with cross-encoder re-ranking, strict grounding, citation formatting, and a polished React frontend. The main gaps are documentation completeness (`data_sources.md` missing columns, PRD not updated for scope narrowing), two known retrieval failures (TC12 graduate programs, TC17 parking), and a severe contribution imbalance (Oscar has zero commits since Feb 17). Sprint 2 focuses on closing these gaps and expanding the system's coverage.

---

## Sprint 2 Tasks

### P0 — Documentation Fixes (Days 1–2)

| Task | Owner | Description |
|---|---|---|
| Complete data_sources.md | Oscar | Convert from flat file list to table with required columns: source category, source type, date collected, MVP inclusion status. This is a substantial task (377 files to categorize) |
| Update PRD | Dustin | Update PRD to reflect catalog-only scope narrowing. Remove references to "Advising, Financial Aid, Tutoring, IT" from MVP scope. Document the engineering rationale for narrowing |
| Add backup questions to demo script | Christian | Add 3-5 backup demo questions to `mvp_demo_script.md` covering different categories |
| Add go/no-go to status doc | Dustin | Add explicit go/no-go assessment to `milestone2_status.md` |

### P1 — Retrieval Improvements (Days 2–5)

| Task | Owner | Description |
|---|---|---|
| Fix TC12 graduate programs | Ian | Investigate why graduate program listings aren't being retrieved. Check if the data is in the corpus, chunking splits it, or embedding similarity is too low |
| Address TC17 parking | Ian | Determine if parking should be in-scope or explicitly out-of-scope. If in-scope, add parking data. If out-of-scope, tune refusal behavior |
| Expand refusal test cases | Dustin | Add 5 more refusal test cases covering: sports, dining, weather, personal advice, non-TAMUSA queries |
| Chunk size experimentation | Oscar | Test different chunk sizes (512, 1024, 2048) and overlap values. Measure impact on retrieval accuracy for the 20 test cases |

### P2 — Frontend Polish (Days 3–6)

| Task | Owner | Description |
|---|---|---|
| Improve citation UX | Trieu | Add tooltip/popup preview when hovering over citation links (show source snippet without navigating away) |
| Conversation history UI | Trieu | Improve the history list display — add search/filter, clear history button |
| Mobile responsiveness | Christian | Ensure the chat interface works well on mobile devices for demo flexibility |
| Error state handling | Trieu | Add user-friendly error messages for: backend down, timeout, empty response |

### P3 — System Improvements (Days 5–7)

| Task | Owner | Description |
|---|---|---|
| Remove 103MB video from repo | Christian | Move `docs/demo_video.mp4` to external hosting (Google Drive or YouTube). Add link in docs |
| Extract test harness | Ian | Move the 20 evaluation test cases from `generator.py` into a separate `tests/` directory |
| Remove duplicate PRD | Oscar | Remove `PRD.md` from root (keep in `docs/`) |
| Demo rehearsal | All | Full team demo: admissions question, financial aid question, retrieval display, citations, refusal case |

---

## Definition of Done (Sprint 2)

- [ ] `data_sources.md` has all required columns for 377 files
- [ ] PRD reflects catalog-only scope
- [ ] Demo script has backup questions
- [ ] TC12 (graduate programs) either fixed or documented with root cause
- [ ] TC17 (parking) either fixed or explicitly scoped out
- [ ] 103MB video removed from repo
- [ ] Oscar has at least 5 meaningful commits this sprint
- [ ] Each team member has code commits

---

## Contribution Expectations

Ian (19 commits) built the entire RAG pipeline. Trieu (14) built the frontend. **Oscar (team lead) has ZERO commits after Feb 17** — 5 initial setup commits only. This is unacceptable for a team lead. Sprint 2 assigns Oscar substantial tasks (data_sources.md categorization and chunk experimentation). Christian and Dustin should also take on coding tasks beyond documentation.

---

## Remaining Sprints Overview

| Sprint | Dates | Focus |
|---|---|---|
| Sprint 2 (this sprint) | Apr 8–14 | Documentation, retrieval fixes, contribution balance |
| Sprint 3 | Apr 15–21 | Additional data sources, UI polish, demo rehearsal |
| Sprint 4 | Apr 22–28 | Final integration, presentation prep, final deliverables |
| **Final Demo** | **Apr 29** | **Presentation and live demo** |
| Final Deliverables Due | May 3 | All documentation and code finalized |
