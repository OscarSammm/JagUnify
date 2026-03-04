# Product Requirements Document (PRD) – Lite
## Project: JagUnify – TAMUSA Student Support Assistant

**Definition:** JagUnify is a grounded Texas A&M University-San Antonio (TAMUSA) campus information assistant that provides students with reliable, AI-generated answers backed by verifiable citations.

---

## A. Problem Definition
* **Fragmented Information:** TAMUSA students often struggle to find accurate information regarding advising, financial aid, and campus services because data is scattered across multiple websites, leading to frustration and wasted time.
* **The Danger of Hallucination:** In a university setting, inaccurate information regarding deadlines or policies can lead to financial penalties or academic delays; therefore, standard AI "hallucinations" are strictly unacceptable.
* **The Necessity of Grounding:** To maintain institutional trust, the assistant must be "grounded," meaning it only generates responses based on verified, official documents rather than general training data.

---

## B. Target Users
* **TAMUSA Students:** Primarily freshmen, transfer, and first-generation students who require centralized access to campus resources.
* **Faculty & Staff (Optional):** University employees needing a quick reference for official policies, tutoring schedules, or IT support procedures.

---

## C. Grounding Requirement (Non-Negotiable)
To ensure the integrity of the information provided, JagUnify must adhere to the following strict operational rules:
* **Mandatory Citations:** Every generated answer must cite at least one retrieved TAMUSA document.
* **Information Boundaries:** Answers must not include any information that is not explicitly present in the retrieved sources.
* **Safe Failure:** If no relevant source is retrieved from the index, the system must strictly refuse to answer and inform the user that information is unavailable.

---

## D. MVP Scope (April 5 Demo)
The Minimum Viable Product for the April 5 demonstration will consist of an end-to-end pipeline including:
* **User Question Input:** A text-based interface where students can submit inquiries.
* **Document Retrieval:** A retrieval engine that pulls relevant context from indexed TAMUSA documents (Advising, Financial Aid, Tutoring, and IT).
* **Answer Generation:** An LLM-driven response grounded in the retrieved text.
* **Inline Citations:** Automatic generation of citations (e.g., [1], [2]) within the response text.
* **Source Preview:** A "Sources Used" section displaying snippets or links to the documents used to generate the answer.

---

## E. Acceptance Criteria (Testable)
The system will be deemed successful for Milestone 1 if it meets the following benchmarks:
* **100% Citation Rate:** Every successful answer includes at least one verifiable citation.
* **Zero Out-of-Bounds Claims:** No claims are made that cannot be supported by the retrieved text snippets.
* **Refusal Accuracy:** The system correctly refuses to answer 100% of "out-of-scope" questions (e.g., "Is there pizza available?").
* **Performance Latency:** Retrieval and generation must complete within an acceptable limit (under 3 seconds) to ensure a positive user experience.