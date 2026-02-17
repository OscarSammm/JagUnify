# Engineering Spike Plan
## Project: JagUnify – TAMUSA Student Support Chatbot

---

## 1. Riskiest Assumption
The riskiest assumption is that a simple chatbot can reliably provide accurate answers to common TAMUSA student questions using only publicly available university information.

---

## 2. Spike Goal (What “Success” Means)
The spike is successful if we can demonstrate a working chatbot prototype that correctly answers a small set of common student questions within seconds.

---

## 3. Inputs → Outputs

**Inputs:**
- User text questions (e.g., “Who do I contact for advising?”)
- Predefined TAMUSA information (advising, financial aid, tutoring, IT support)

**Outputs:**
- Clear text responses with correct information
- A fallback message when the system cannot answer a question

---

## 4. Demo Plan (2–3 minutes)

- Show the chatbot interface running locally
- Ask 2–3 common TAMUSA-related questions live
- Show correct responses being returned
- Ask one unknown question to demonstrate safe failure behavior

---

## 5. Owners + Tasks

- **Oscar Hernandez (Team Lead):** Spike coordination, chatbot logic, demo presentation
- **Team Members:** Collect TAMUSA information, test questions, validate responses

---

## 6. Exit Criteria (Pass / Fail)

**Pass if:**
- Chatbot answers at least 3 common questions correctly
- Responses are generated within 3 seconds
- System handles unknown questions gracefully

**Fail if:**
- Answers are consistently incorrect
- System crashes or cannot respond
- Demo cannot be completed end-to-end

---

## 7. If It Fails (Plan B)

If the chatbot cannot reliably answer questions, we will fall back to a rule-based or keyword-matching system with predefined responses and direct links to official TAMUSA resources.
