# Evaluation Test Cases – Milestone 1  
Project: JagUnify – Grounded TAMUSA Information Assistant  
Date: 3/5/2026

---

# Evaluation Overview

This document evaluates grounding performance of the RAG pipeline.

Each test case includes:
- User Question
- Expected Source Document(s)
- Retrieved Document(s)
- Generated Answer
- Verification Status (Pass/Fail)

Grounding Rules:
- Every answer must cite at least one retrieved TAMUSA source.
- No unsupported claims outside retrieved text.
- If no relevant source is retrieved, system must refuse.

---

# Test Cases

---

## Test Case 1
**Question:** What are the admissions requirements for freshman students at TAMUSA?  
**Expected Source:** TAMUSA Undergraduate Admissions Page  
**Retrieved Document(s):** [To be filled after run]  
**Generated Answer:** [To be filled after run]  
**Verification Status:** [Pass/Fail]

---

## Test Case 2
**Question:** What is the deadline to apply for fall semester admission?  
**Expected Source:** TAMUSA Admissions Deadlines Page  
**Retrieved Document(s):**  
**Generated Answer:**  
**Verification Status:**  

---

## Test Case 3
**Question:** Where is the Office of the Registrar located?  
**Expected Source:** TAMUSA Registrar Contact Page  
**Retrieved Document(s):**  
**Generated Answer:**  
**Verification Status:**  

---

## Test Case 4
**Question:** What are the operating hours of the TAMUSA library?  
**Expected Source:** TAMUSA Library Hours Page  
**Retrieved Document(s):**  
**Generated Answer:**  
**Verification Status:**  

---

## Test Case 5
**Question:** How can students apply for financial aid?  
**Expected Source:** TAMUSA Financial Aid Page  
**Retrieved Document(s):**  
**Generated Answer:**  
**Verification Status:**  

---

## Test Case 6
**Question:** What majors are offered at TAMUSA?  
**Expected Source:** TAMUSA Academic Programs Page  
**Retrieved Document(s):**  
**Generated Answer:**  
**Verification Status:**  

---

## Test Case 7
**Question:** What GPA is required for academic probation?  
**Expected Source:** TAMUSA Academic Standing Policy  
**Retrieved Document(s):**  
**Generated Answer:**  
**Verification Status:**  

---

## Test Case 8
**Question:** How do I register for classes?  
**Expected Source:** TAMUSA Registration Guide  
**Retrieved Document(s):**  
**Generated Answer:**  
**Verification Status:**  

---

## Test Case 9
**Question:** Where can students find tutoring services?  
**Expected Source:** TAMUSA Student Success Center Page  
**Retrieved Document(s):**  
**Generated Answer:**  
**Verification Status:**  

---

## Test Case 10
**Question:** What documents are required for transfer students?  
**Expected Source:** TAMUSA Transfer Admissions Page  
**Retrieved Document(s):**  
**Generated Answer:**  
**Verification Status:**  

---

## Test Case 11
**Question:** What is the campus address?  
**Expected Source:** TAMUSA Contact Page  
**Retrieved Document(s):**  
**Generated Answer:**  
**Verification Status:**  

---

## Test Case 12
**Question:** What meal plans are available on campus?  
**Expected Source:** TAMUSA Dining Services Page  
**Retrieved Document(s):**  
**Generated Answer:**  
**Verification Status:**  

---

## Test Case 13
**Question:** How can students request official transcripts?  
**Expected Source:** TAMUSA Registrar Transcript Request Page  
**Retrieved Document(s):**  
**Generated Answer:**  
**Verification Status:**  

---

## Test Case 14
**Question:** What are the graduation requirements for undergraduates?  
**Expected Source:** TAMUSA Undergraduate Catalog  
**Retrieved Document(s):**  
**Generated Answer:**  
**Verification Status:**  

---

## Test Case 15
**Question:** Does TAMUSA offer online degree programs?  
**Expected Source:** TAMUSA Online Programs Page  
**Retrieved Document(s):**  
**Generated Answer:**  
**Verification Status:**  

---

## Test Case 16
**Question:** How do students appeal a grade?  
**Expected Source:** TAMUSA Grade Appeal Policy  
**Retrieved Document(s):**  
**Generated Answer:**  
**Verification Status:**  

---

## Test Case 17
**Question:** What health services are available on campus?  
**Expected Source:** TAMUSA Student Health Services Page  
**Retrieved Document(s):**  
**Generated Answer:**  
**Verification Status:**  

---

## Test Case 18
**Question:** What is the maximum credit load per semester?  
**Expected Source:** TAMUSA Academic Policies Page  
**Retrieved Document(s):**  
**Generated Answer:**  
**Verification Status:**  

---

## Test Case 19 (Refusal Case)
**Question:** What NFL players graduated from TAMUSA?  
**Expected Source:** None (Not in official TAMUSA academic documents)  
**Retrieved Document(s):**  
**Generated Answer:**  
**Verification Status:**  

Expected Behavior:
System should refuse:
"I cannot find supporting information in the indexed TAMUSA documents."

---

## Test Case 20 (Refusal Case)
**Question:** What is the average salary of TAMUSA graduates five years after graduation?  
**Expected Source:** None (if not in indexed documents)  
**Retrieved Document(s):**  
**Generated Answer:**  
**Verification Status:**  

Expected Behavior:
System should refuse if no indexed source supports it.

---

# Metrics

After running all 20 test cases:

### Retrieval Accuracy
Definition:
Percentage of test cases where the correct source document was retrieved in top-k results.

Formula:
(# Correct Retrievals / 20) × 100

Result:
[Insert %]

---

### Grounding Accuracy
Definition:
Percentage of answers fully supported by retrieved text (no hallucinated claims).

Formula:
(# Fully Grounded Answers / 20) × 100

Result:
[Insert %]

---

### Refusal Accuracy
Definition:
Percentage of refusal cases correctly refused when no supporting document exists.

Formula:
(# Correct Refusals / # Refusal Cases) × 100

Result:
[Insert %]

---

# Summary

- Total Questions: 20
- Retrieval Accuracy: ___%
- Grounding Accuracy: ___%
- Refusal Accuracy: ___%
