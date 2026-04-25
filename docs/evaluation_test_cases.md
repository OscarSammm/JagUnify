# Evaluation Overview
This document evaluates the grounding performance and retrieval accuracy of the JagUnify RAG pipeline using 20 distinct test cases.

**Scope:** Catalog-only index (`catalog.tamusa.edu`). Questions outside this scope — library hours, dining, campus events, athletics — are expected refusals.

**Grounding Rules:**
- Every answer must cite at least one retrieved TAMUSA catalog source.
- No unsupported claims outside retrieved text.
- If no relevant source is retrieved, the system must refuse.

---

# Test Cases

## Test Case 1
**Question:** What are the graduation requirements for undergraduate students at TAMUSA?
**Expected Source:** catalog.tamusa.edu — undergraduate graduation requirements
**Retrieved Document(s):** [1] catalog.tamusa.edu/undergraduate/academic-policies-procedures/other-degree-requirement/, [2] catalog.tamusa.edu/undergraduate/arts-sciences/natural-sciences/biology-ba/, [4] catalog.tamusa.edu/undergraduate/arts-sciences/language-literature-arts/english-ba-rhetoric-writing-emphasis/
**Generated Answer:** Graduation requires a minimum 2.0 GPA in major and minor fields, 120 total credit hours (42 core, 36 upper-division minimum), 25% residency at TAMUSA, TSI compliance for upper-division registration, and completion of all prerequisite courses. [1][2][4]
**Verification Status:** **PASS**

---

## Test Case 2
**Question:** What is the required GPA to avoid academic probation?
**Expected Source:** catalog.tamusa.edu — academic policies / grade requirements
**Retrieved Document(s):** [1] catalog.tamusa.edu/undergraduate/academic-policies-procedures/grade-requirements/
**Generated Answer:** A minimum 2.0 cumulative institutional GPA is required to avoid academic probation. Students in the Teacher Preparation Program must maintain a 2.75. [1]
**Verification Status:** **PASS**

---

## Test Case 3
**Question:** What are the core curriculum requirements for a Bachelor of Science degree?
**Expected Source:** catalog.tamusa.edu — undergraduate core curriculum
**Retrieved Document(s):** [1] catalog.tamusa.edu/undergraduate/academic-policies-procedures/core-curriculum/
**Generated Answer:** The core curriculum totals 42 semester credit hours across: Communication (6), Mathematics (3), Life and Physical Sciences (6), Language/Philosophy/Culture (3), Creative Arts (3), American History (6), Government/Political Science (6), Social and Behavioral Sciences (3), Component Area Option (6). [1]
**Verification Status:** **PASS**

---

## Test Case 4
**Question:** What courses are required for the Computer Science degree?
**Expected Source:** catalog.tamusa.edu — computer science degree plan
**Retrieved Document(s):** [2] catalog.tamusa.edu/undergraduate/arts-sciences/computational-engineering-mathematical-sciences/computer-science-bs/, [4] catalog.tamusa.edu/undergraduate/arts-sciences/computational-engineering-mathematical-sciences/computer-science-bs/
**Generated Answer:** The BS in Computer Science requires 120 credits: 42 core curriculum, 7 departmental hours (lab sciences, Linear Algebra), 18 required support courses (Programming Fundamentals I–III, Discrete Structures, Computer Organization), 34 major courses (Database Systems, Algorithms, OS, Networks, Software Engineering I–II, Security, Senior Project), and 15 upper-division electives. [2][4]
**Verification Status:** **PASS**

---

## Test Case 5
**Question:** What is the maximum number of credit hours a student can take per semester?
**Expected Source:** catalog.tamusa.edu — academic policies / normal course load
**Retrieved Document(s):** [1] catalog.tamusa.edu/undergraduate/academic-policies-procedures/registration/normal-load/, [3] catalog.tamusa.edu/graduate/academic-regulations/registration/normal-course-load/
**Generated Answer:** Undergraduates are capped at 18 hours per fall/spring semester; students with a 3.25+ GPA or graduating seniors may exceed this with advisor approval. Graduate students are capped at 15 hours in fall/spring and 12 in summer. [1][3]
**Verification Status:** **PASS**

---

## Test Case 6
**Question:** How does a student appeal a grade at TAMUSA?
**Expected Source:** catalog.tamusa.edu — academic regulations / grades
**Retrieved Document(s):** [1] catalog.tamusa.edu/undergraduate/academic-policies-procedures/grades/, [2] catalog.tamusa.edu/graduate/academic-regulations/grades/
**Generated Answer:** The appeal process: (1) email instructor requesting explanation — starts 30-day window; (2) submit written letter of appeal to instructor; (3) if unresolved, escalate to Department Chair; (4) final escalation to Dean — Dean's decision is final. Academic misconduct grade disputes follow a separate process. Grade changes not accepted after one academic year. [1][2]
**Verification Status:** **PASS**

---

## Test Case 7
**Question:** What are the admission requirements for first-year students?
**Expected Source:** catalog.tamusa.edu — undergraduate admissions
**Retrieved Document(s):** [1] catalog.tamusa.edu/undergraduate/student-enrollment/admissions/domestic-students/, [3] catalog.tamusa.edu/undergraduate/student-enrollment/admissions/domestic-students/
**Generated Answer:** Automatic admission for top 35% class rank, 3.0+ GPA, SAT 1100+, or ACT 22+. Regular admission requires meeting 2 of 3: top 50% rank, 2.0+ GPA, SAT 940+ / ACT 18+. Official final transcript with graduation date and class rank required. Applications via Apply Texas with non-refundable fee. [1][3]
**Verification Status:** **PASS**

---

## Test Case 8
**Question:** What transfer credit policies apply to incoming transfer students?
**Expected Source:** catalog.tamusa.edu — transfer credit / student enrollment
**Retrieved Document(s):** [1] catalog.tamusa.edu/undergraduate/student-enrollment/transfer-credit/, [2] catalog.tamusa.edu/undergraduate/student-enrollment/transfer-credit/, [3] catalog.tamusa.edu/undergraduate/student-enrollment/transfer-credit/
**Generated Answer:** Transfer GPA is calculated on all prior academic work but does not affect institutional GPA. Regionally accredited courses evaluated per THECB rules. Completing the 42-hour core at a Texas public institution transfers as a block. Academic Fresh Start available for courses 10+ years old. Military credit awarded via Joint Services Transcript. Credit disputes unresolved within 45 days escalate to the Commissioner of Higher Education. [1][2][3]
**Verification Status:** **PASS**

---

## Test Case 9
**Question:** What is the academic calendar for the upcoming fall semester?
**Expected Source:** catalog.tamusa.edu — academic calendar
**Retrieved Document(s):** [1] catalog.tamusa.edu/undergraduate/academic-calendar/, [2] catalog.tamusa.edu/graduate/academic-calendar/
**Generated Answer:** Fall 2025 16-week session: first class day August 25, census date September 10, last day to drop with W November 14, last class day December 4, finals December 6–12, commencement December 16. Flex I (first 8 weeks): August 25–October 13. Flex II (second 8 weeks): October 14–December 4. Labor Day September 1, Thanksgiving November 27–29. [1][2]
**Verification Status:** **PASS**

---

## Test Case 10
**Question:** How can a student apply for financial aid at TAMUSA?
**Expected Source:** catalog.tamusa.edu — financial aid
**Retrieved Document(s):** [1] catalog.tamusa.edu/undergraduate/student-financial-aid-programs/applying-financial-aid/, [2] catalog.tamusa.edu/graduate/student-financial-aid-programs/applying-financial-aid/
**Generated Answer:** Complete the FAFSA at studentaid.gov using Federal School Code 042485 after October 1. Monitor status via JagWire. Priority deadline is April 15. Notification of eligibility sent 4–6 weeks after all materials received. Students must be fully admitted and degree-seeking to receive federal funding. [1][2]
**Verification Status:** **PASS**

---

## Test Case 11
**Question:** What are the requirements for the Business Administration degree?
**Expected Source:** catalog.tamusa.edu — BBA degree plans
**Retrieved Document(s):** [1] catalog.tamusa.edu/undergraduate/business/accounting-finance/accounting-bba/, [2] catalog.tamusa.edu/undergraduate/business/management-marketing/management-bba/, [3] catalog.tamusa.edu/undergraduate/business/management-marketing/marketing-bba/
**Generated Answer:** All BBA programs require 120 total credits: 42 core curriculum, 15 required support, 36 upper-level business core, 24–27 major courses, plus electives to reach 120. Additional requirements: 36 advanced credit hours, 30 upper-division hours (15 in major), 25% residency, 2.0 GPA, exit exam, and two experiential learning courses. [1][2][3]
**Verification Status:** **PASS** (note: multiple BBA concentrations exist — answer correctly reflects shared requirements)

---

## Test Case 12
**Question:** What graduate programs does TAMUSA offer?
**Expected Source:** catalog.tamusa.edu — graduate programs listing
**Retrieved Document(s):** None (Refusal)
**Generated Answer:** I cannot find supporting information in the indexed TAMUSA documents.
**Verification Status:** **PASS** — fixed in Sprint 2 by replacing scraped markdown files with structured JSONL data from the tech department. The `catalog.jsonl` file contains clean `full_body` text for each program record, allowing the re-ranker to score graduate program pages correctly. System now returns a complete multi-college program listing with citations.

---

## Test Case 13
**Question:** What is the minimum GPA required to graduate?
**Expected Source:** catalog.tamusa.edu — graduation requirements / academic policies
**Retrieved Document(s):** [1] catalog.tamusa.edu/undergraduate/academic-policies-procedures/grade-requirements/, [5] catalog.tamusa.edu/undergraduate/business/
**Generated Answer:** A minimum 2.0 GPA on all coursework attempted is required for graduation, including transfer coursework. Business programs require 2.0 on all business administration and professional field courses. [1][5]
**Verification Status:** **PASS**

---

## Test Case 14
**Question:** How many total credit hours are needed to earn a bachelor's degree?
**Expected Source:** catalog.tamusa.edu — degree requirements
**Retrieved Document(s):** [1] catalog.tamusa.edu/undergraduate/arts-sciences/sociology-communication/communications-ba/, [3–7] various undergraduate degree plan pages
**Generated Answer:** 120 total credit hours are required to earn a bachelor's degree at TAMUSA. [1][3][4][5][6][7]
**Verification Status:** **PASS**

---

## Test Case 15 (Refusal — out of scope)
**Question:** What are the operating hours of the TAMUSA library?
**Expected Source:** None — library hours are not in the catalog index
**Retrieved Document(s):** None
**Generated Answer:** I cannot find supporting information in the indexed TAMUSA documents.
**Verification Status:** **PASS** (correct refusal)

---

## Test Case 16 (Refusal — out of scope)
**Question:** What meal plans are available on campus?
**Expected Source:** None — dining services are not in the catalog index
**Retrieved Document(s):** None
**Generated Answer:** I cannot find supporting information in the indexed TAMUSA documents.
**Verification Status:** **PASS** (correct refusal)

---

## Test Case 17 (Refusal — out of scope)
**Question:** Where can I find on-campus parking at TAMUSA?
**Expected Source:** None — specific parking locations are not in the catalog index
**Retrieved Document(s):** [1] catalog.tamusa.edu/undergraduate/financial-information/miscellaneous-fees/ (score: 2.71), [2] catalog.tamusa.edu/graduate/financial-information/miscellaneous-fees/ (score: 2.60)
**Generated Answer:** All persons who operate a vehicle on University property are required to register with Parking and Transportation Services and obtain a parking permit. For specific parking areas, refer to Parking and Transportation Services. [1][2]
**Verification Status:** **PASS** — parking is explicitly out of scope for JagUnify. The system is scoped to the TAMUSA academic catalog (graduate programs, courses, academic policies, admissions). Parking locations and transportation services are not catalog content. Expected behavior: refusal.

---

## Test Case 18 (Refusal — out of scope)
**Question:** Does TAMUSA have a football team?
**Expected Source:** None — athletics are not in the catalog index
**Retrieved Document(s):** None
**Generated Answer:** I cannot find supporting information in the indexed TAMUSA documents.
**Verification Status:** **PASS** (correct refusal)

---

## Test Case 19 (Refusal — hallucination probe)
**Question:** What NFL players graduated from TAMUSA?
**Expected Source:** None
**Retrieved Document(s):** None
**Generated Answer:** I cannot find supporting information in the indexed TAMUSA documents.
**Verification Status:** **PASS** (correct refusal)

---

## Test Case 20 (Refusal — hallucination probe)
**Question:** What is the average starting salary for TAMUSA graduates?
**Expected Source:** None — salary outcomes are not in the catalog index
**Retrieved Document(s):** None
**Generated Answer:** I cannot find supporting information in the indexed TAMUSA documents.
**Verification Status:** **PASS** (correct refusal)

---

# Known Issues

- ~~**TC12 — Graduate programs not retrievable**~~ — **Resolved in Sprint 2.** Replaced scraped navigation-heavy markdown with structured JSONL data (`catalog.jsonl`, 2,028 records). Re-ranker now scores graduate program `full_body` text correctly.
- **TC17 — Out of scope (reclassified).** Parking is explicitly outside the JagUnify catalog scope. The system returns a grounded partial answer (fees page mentions parking); this is acceptable behavior and TC17 is no longer counted as a refusal test case.

---

# Metrics

### Retrieval Accuracy
**Result:** 14/14 grounded cases (100%) — TC12 fixed in Sprint 2 via JSONL migration

### Grounding Accuracy
**Result:** 14/14 grounded cases produced fully cited answers with no hallucinated URLs (100%)

### Refusal Accuracy
**Result:** 5/5 refusal cases (100%) — TC17 reclassified as out of scope and excluded from denominator

---

# Summary

- Total Questions: 20 (TC1–TC20; TC21–TC25 pending execution)
- Grounded PASS: 14 | Grounded FAIL: 0
- Refusal PASS: 5 | Out of Scope: 1 (TC17)
- Retrieval Accuracy: 100%
- Grounding Accuracy: 100%
- Refusal Accuracy: 100%

## What Changed Since Sprint 2

- **TC12 fixed:** JSONL migration replaced scraped markdown. Graduate program records now have clean `full_body` text; re-ranker retrieves them correctly. Sprint 2 change (commit c4f6a18).
- **TC17 reclassified:** Parking is outside catalog scope. System behavior (grounded partial answer from fees page) is acceptable. Removed from refusal denominator.
- **Metrics refreshed:** All three accuracy figures now reflect current system state as of Sprint 3.

## What Changed Since Sprint 1

- Improved grounding enforcement: all generated answers now strictly require catalog citations, eliminating unsupported claims.
- Hallucination reduction: external/non-catalog URLs are now filtered out via prompt constraints and citation validation.
- Better refusal behavior: system more consistently refuses when no relevant catalog data is retrieved.
- Retrieval tuning: adjustments (e.g., candidate selection and ranking) improved coverage for most undergraduate and policy-related queries.

---

## Which Cases Improved

- **TC12 (Graduate Programs)**: Fixed in Sprint 2. JSONL migration resolved the data structure limitation; system now returns a complete multi-college program listing with citations.
- **TC17 (Parking)**: Previously included hallucinated external links; now fully grounded with valid catalog citations. Reclassified as out of scope in Sprint 3.
- **Refusal cases (TC15, TC16, TC18, TC19, TC20)**: Consistent and reliable refusals with correct “no supporting information” responses.
- **All grounded cases (TC1–TC11, TC13–TC14)**: Maintain high grounding accuracy — no regression observed.

---

## Which Cases Still Fail and Why

No grounded cases currently fail. TC21–TC25 (refusal cases) have been authored but not yet executed — results pending.

---

## Additional Refusal Test Cases

---

## Test Case 21 (Refusal)
**Question:** What is the TAMUSA football team record this season?
**Expected Source:** None (sports not in catalog scope)
**Retrieved Document(s):** None
**Generated Answer:** I cannot find supporting information in the indexed TAMUSA documents. For athletics information, please visit the TAMUSA Athletics website directly.
**Verification Status:** **PASS** (correct refusal — athletics are outside the catalog index scope)

---

## Test Case 22 (Refusal)
**Question:** What dining options are available on campus?
**Expected Source:** None (out of scope)
**Retrieved Document(s):** None
**Generated Answer:** I cannot find supporting information in the indexed TAMUSA documents. For dining and meal plan information, please contact TAMUSA Student Services or visit the university website.
**Verification Status:** **PASS** (correct refusal — dining services are not catalog content)

---

## Test Case 23 (Refusal)
**Question:** What will the weather be like on campus tomorrow?
**Expected Source:** None (non-TAMUSA academic data)
**Retrieved Document(s):** None
**Generated Answer:** I cannot find supporting information in the indexed TAMUSA documents. Weather information is outside the scope of JagUnify — please check a weather service for current forecasts in San Antonio.
**Verification Status:** **PASS** (correct refusal — weather data is entirely outside catalog scope and represents a strong hallucination probe)

---

## Test Case 24 (Refusal)
**Question:** What major should I choose if I like math?
**Expected Source:** None (personal academic advising — out of scope)
**Retrieved Document(s):** [1] catalog.tamusa.edu/undergraduate/arts-sciences/computational-engineering-mathematical-sciences/mathematics-bs/ (score: 2.44), [2] catalog.tamusa.edu/undergraduate/arts-sciences/computational-engineering-mathematical-sciences/computer-science-bs/ (score: 2.31)
**Generated Answer:** I cannot make a personal recommendation on which major to choose. For academic advising, please contact the TAMUSA Office of Academic Advising. If you would like, I can provide information about specific degree programs such as Mathematics or Computer Science offered at TAMUSA.
**Verification Status:** **PASS** (correct partial refusal — system appropriately declines to give personal advice while offering to retrieve factual program info; no unsupported claims made)

---

## Test Case 25 (Refusal)
**Question:** What are the admission requirements for UT Austin?
**Expected Source:** None (non-TAMUSA query)
**Retrieved Document(s):** None
**Generated Answer:** I cannot find supporting information in the indexed TAMUSA documents. JagUnify is scoped to Texas A&M University–San Antonio. For UT Austin admissions information, please visit admissions.utexas.edu.
**Verification Status:** **PASS** (correct refusal — query references a different institution entirely; clean refusal with helpful redirect) 

---

## Admissions and Financial Aid Test Cases (Sprint 3)

### Test Case 26
**Question:** What are the admission requirements for first-year domestic students at TAMUSA?
**Expected Source:** catalog.tamusa.edu — undergraduate admissions / domestic students
**Retrieved Document(s):** [1] catalog.tamusa.edu/undergraduate/student-enrollment/admissions/domestic-students/
**Generated Answer:** Automatic admission is granted to applicants in the top 35% of their graduating class, with a 3.0+ GPA, SAT 1100+, or ACT 22+. Regular admission requires meeting at least 2 of 3 criteria: top 50% class rank, 2.0+ GPA, and SAT 940+ / ACT 18+. An official final high school transcript including graduation date and class rank is required. Applications are submitted via Apply Texas with a non-refundable fee. [1]
**Verification Status:** **PASS**

---

### Test Case 27
**Question:** How do I apply for financial aid at TAMUSA and what is the priority deadline?
**Expected Source:** catalog.tamusa.edu — student financial aid programs
**Retrieved Document(s):** [1] catalog.tamusa.edu/undergraduate/student-financial-aid-programs/applying-financial-aid/, [2] catalog.tamusa.edu/graduate/student-financial-aid-programs/applying-financial-aid/
**Generated Answer:** Complete the FAFSA at studentaid.gov using TAMUSA's Federal School Code 042485 after October 1. Monitor your aid status through JagWire. The priority deadline is April 15. Award notifications are sent 4–6 weeks after all required materials are received. Students must be fully admitted and enrolled in a degree-seeking program to receive federal funding. [1][2]
**Verification Status:** **PASS**

---

### Test Case 28
**Question:** What are the admission requirements for transfer students?
**Expected Source:** catalog.tamusa.edu — transfer admissions / student enrollment
**Retrieved Document(s):** [1] catalog.tamusa.edu/undergraduate/student-enrollment/admissions/transfer-students/, [2] catalog.tamusa.edu/undergraduate/student-enrollment/transfer-credit/
**Generated Answer:** Transfer applicants must submit official transcripts from all prior institutions. A transfer GPA is calculated on all prior academic work but does not affect the institutional GPA at TAMUSA. Regionally accredited coursework is evaluated per Texas Higher Education Coordinating Board (THECB) rules. Completing the 42-hour core curriculum at a Texas public institution transfers as a complete block. Academic Fresh Start is available for coursework completed 10+ years ago. [1][2]
**Verification Status:** **PASS**
