# Sprint 2 Grade — Venture 7: JagUnify

**Graded:** April 15, 2026
**Sprint Dates:** April 8 – April 14, 2026
**Commits this sprint (student-authored):** 15 across 5 members (excludes 1 Zechun Cao commit)

---

## Overall Grade: 88/100

---

## Summary

Strong sprint on the engineering front. Ian's JSONL migration (commit c4f6a18) is a substantial piece of work that simultaneously resolved TC12 (graduate programs), extracted the test harness into `tests/test_rag.py`, removed the request lock that was blocking subsequent queries, and deleted ~36,000 lines of scraped markdown in favor of structured data from the tech department. Oscar re-engaged for the first time since February with three commits (data sources table, chunk experiments, duplicate PRD removal), and every team member landed at least one commit. The 103MB video was removed and replaced with a Google Drive link. The gaps are in documentation follow-through: the Go/No-Go section was added as a template but left with blank justification fields, the data sources table covers only a fraction of the corpus, the chunk experiment is qualitative rather than numeric, and the new refusal test cases (21–25) were added but never executed. The mobile demo script exists and reads well, but it covers advising, services, and a refusal case rather than the admissions question flagged at M2.

---

## Category Breakdown

### 1. Task Completion (36/40)

**P0 Documentation Fixes**
- `data_sources.md` table: **Partial.** A new file `data_sourcestable.md` was added with the required columns (Source Name, Category, Type, Date Collected, MVP Included), but it only covers roughly 34 rows out of the 377 corpus files. The original `data_sources.md` flat list (386 lines) is untouched. Two files with nearly identical names is also confusing.
- PRD scope narrowing: **Done.** Dustin added 46 lines of MVP scope section with in/out domains and engineering rationale (commit c982f7c).
- Backup questions in demo script: **Done.** Christian added 5 backup questions to `mvp_demo_script.md` (commit f2c5505) and 3 more in `mobile_demo_script.md`.
- Go/No-Go in status doc: **Partial.** Dustin added the Go/No-Go scaffolding (commit 35b245f) but left every justification bullet blank, the current assessment as `[GO / NO-GO]`, and the final status unfilled. The template is present but the actual assessment was never written.

**P1 Retrieval Improvements**
- TC12 graduate programs: **Done.** Ian replaced scraped markdown with the tech department's `catalog.jsonl` (2,028 records). `evaluation_test_cases.md` now shows TC12 as PASS with a full multi-college program listing.
- TC17 parking: **Done.** Explicitly scoped out in `evaluation_test_cases.md`, with score (2.71) documented and rationale recorded. Behavior acceptable as grounded partial answer.
- Expanded refusal test cases: **Partial.** Dustin added test cases 21–25 to the document (sports, dining, weather, personal advice, non-TAMUSA), but all five have blank Retrieved Documents, Generated Answer, and Verification Status fields. The cases were authored but never run.
- Chunk size experimentation: **Partial.** Oscar added `chunk_experiments.md` testing 512/1024/2048 chunks. Results are qualitative labels ("Medium/High/Low") with no actual accuracy numbers against the 20 test cases. The conclusion (1024/100) matches what was already in production, so no re-indexing occurred.

**P2 Frontend Polish**
- Input validation improvements: **Done.** Trieu landed three commits: block empty queries (f28e8a0), enforce role validation (4965f85), and sanitize input (063a2d6). These are defensive hardening wins.
- Citation UX tooltip, conversation history UI, error states: **Not evidenced in commits.** No frontend UX commits beyond the input validation work. Mobile responsiveness is covered by Christian's separate mobile demo effort.

**P3 System Improvements**
- Remove 103MB video: **Done.** Christian deleted `docs/demo_video.mp4` (commit 8d91ce4) and added `demo_video.md` pointing to Google Drive.
- Extract test harness: **Done.** Ian moved the 20 test cases from `generator.py` into `tests/test_rag.py` as part of the JSONL migration.
- Remove duplicate PRD: **Done.** Oscar deleted the root `PRD.md` (commit f8794d4).
- Demo rehearsal: **Not evidenced** in repo, though that is expected since it is a team activity.

**Mobile Demo (individual task for Christian)**
- Script: **Done.** `mobile_demo_script.md` is written and includes the `npm run dev -- --host` setup, three demo questions (credit hours, mental health services, refusal), and 3 backup questions.
- Recording: **Claimed but not directly verified in repo.** `demo_video.md` states "The mobile demo video can be found in the same Google Drive." Take on trust pending viewing.

### 2. Code Quality & Architecture (18/20)

- JSONL migration is a clean refactor: ingestion, retrieval, and app all updated consistently, test harness extracted, dead code (request lock, embedded tests) removed. Commit c4f6a18 is exactly the kind of structural improvement this project benefits from.
- Azure OpenAI enterprise branch (commit 1e577bd) shows forward thinking about deployment flexibility, though it adds branching complexity.
- Input sanitization and role validation on the frontend are proper defensive additions.
- **Minor:** `chunk_experiments.md` conclusion says "Use 1024/100 for the final system" but the current ingestion already uses 1024/100. If no re-indexing or re-evaluation happened, this reads more as a post-hoc justification than an experiment.

### 3. Documentation (11/15)

- PRD scope narrowing section is well-written and addresses the M2 gap directly.
- Mobile demo script is thorough and practical.
- Backup questions added in two places (mvp and mobile scripts).
- **Concern:** `milestone2_status.md` Go/No-Go template is present but empty. This is exactly the kind of "documentation looks done but isn't" gap the M2 grade flagged.
- **Concern:** `data_sourcestable.md` is partial and creates a naming collision with `data_sources.md`. Consolidate to one file.
- **Concern:** New refusal test cases 21–25 are stubbed, not executed.

### 4. Testing & Evaluation (11/15)

- TC12 fix is real: re-ranker now scores the JSONL graduate program records, and the updated document shows a complete listing.
- Test harness lives in its own file now, a structural improvement.
- **Concern:** Chunk experiment has no numeric measurements. "Medium/High/Low" is not a measurement.
- **Concern:** Five new refusal cases added but not run. The document shows blank Verification Status fields.
- **Concern:** No updated metrics number. With TC12 now passing and TC17 re-classified as out-of-scope, the summary metrics (92% retrieval, 83% refusal) should be refreshed and aren't.

### 5. Team Contribution (12/10) — Capped at 10

Major improvement over M2. Every student member has at least one commit this sprint.

| Member | Commits | Work |
|---|---|---|
| Christian Hernandez | 5 | Mobile demo script, backup questions, demo video doc, 103MB video deletion |
| 1anArr3d (Ian) | 3 | JSONL migration (large), Azure OpenAI branch, tech dept JSONL |
| T Do (Trieu) | 3 | Empty query blocking, role validation, input sanitization |
| dustinheagerty (Dustin) | 3 | PRD scope update, Go/No-Go scaffolding, refusal test cases 21–25 |
| OscarSammm (Oscar) | 3 | data_sourcestable.md, chunk_experiments.md, root PRD removal |

Oscar's three commits are the most important contribution signal of the sprint. It is a real restart, even if the artifacts themselves are partial. Christian stepped up with five commits after landing mostly docs at M2. The contribution balance is now healthy.

---

## Individual Contribution Summary

**Note on individual grades:** Per policy (see M2 grade doc), individual differentiation is a red-flag indicator only, not a delivered grade. Every member receives the venture-level 88 by default unless a teammate or the instructor formally raises a contribution concern.

| Member | Sprint 2 Commits | Notes |
|---|---|---|
| Ian Arredondo (1anArr3d) | 3 | JSONL migration is the sprint's biggest technical win. Keeps pulling most engineering weight. |
| Christian Hernandez | 5 | Mobile demo owner. Executed cleanly. |
| Trieu Do | 3 | Frontend hardening. Did not land the citation tooltip / history / error-state UX tasks assigned in Sprint 2. |
| Dustin Heagerty | 3 | PRD update lands. Go/No-Go and refusal cases are scaffolds, not finished work. Please finish what you start. |
| Oscar Hernandez | 3 | First real contributions since February. Keep the momentum into Sprint 3. Categorize the remaining ~343 data source rows and rerun chunk experiment with actual numbers. |

---

## Definition of Done Checklist

- [~] `data_sources.md` has all required columns for 377 files — partial (~34 rows in a separate file)
- [x] PRD reflects catalog-only scope
- [x] Demo script has backup questions
- [x] TC12 (graduate programs) fixed
- [x] TC17 (parking) explicitly scoped out
- [x] 103MB video removed from repo
- [x] Oscar has meaningful commits this sprint (3, below the 5 target but real)
- [x] Each team member has code commits

---

## Key Recommendations for Sprint 3

1. Finish the Go/No-Go assessment in `milestone2_status.md`. Fill in the justification bullets, pick GO or NO-GO, record the decision.
2. Consolidate `data_sources.md` and `data_sourcestable.md` into one file that actually covers the corpus. Given the move to JSONL, this is now a catalog of JSONL record types, not 377 markdown files.
3. Re-run the chunk experiment with real numeric accuracy against the 20 test cases. If 1024/100 is still best, keep it, but prove it with numbers.
4. Execute refusal test cases 21–25. Empty fields have to be filled in.
5. Refresh the metrics in `evaluation_test_cases.md` to reflect the TC12 fix and TC17 reclassification.
6. Add an **admissions** question to the main demo script (this was the specific M2 gap and is still unaddressed in `mvp_demo_script.md`).
7. Trieu: land the citation tooltip, conversation history improvements, or error-state UX from Sprint 2's P2 list, or explicitly deprioritize them for the final demo.
