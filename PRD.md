# Product Requirements Document (PRD)
## Project: JagUnify – TAMUSA Student Support Chatbot

---

## 1. Problem + Target Users

TAMUSA students often struggle to find accurate information about advising, financial aid, tutoring, IT support, and campus services because information is scattered across multiple websites. This leads to wasted time, confusion, and frustration, especially for new and first-generation students. JagUnify targets TAMUSA students who need quick, reliable answers to common university-related questions in one centralized place. This problem matters because access to clear information directly affects student success and retention.

---

## 2. Goal / Success Metrics

- The chatbot answers at least **80% of common student questions correctly** during testing.
- Students can retrieve needed information in **under 30 seconds** per question.
- Reduce repeated or misdirected student inquiries by providing clear responses.
- Positive user feedback from a small pilot group (average rating of 4/5 or higher).

---

## 3. MVP User Stories

- As a TAMUSA student, I want to ask questions about advising so that I know who to contact.
- As a student, I want to ask about financial aid deadlines so that I don’t miss important dates.
- As a student, I want to find tutoring resources so that I can improve my academic performance.
- As a student, I want to ask IT-related questions so that I can resolve technical issues quickly.
- As a student, I want clear answers written in simple language so that information is easy to understand.
- As a user, I want the chatbot to tell me when it doesn’t know an answer so that I am not misled.

---

## 4. MVP Scope vs. Non-Goals

### Must-Have Features
- Text-based chatbot interface
- Answers based on official TAMUSA information
- Coverage of advising, financial aid, tutoring, and IT support
- Basic error handling for unknown questions

### Nice-to-Have Features (Optional)
- Links to official TAMUSA web pages
- Improved response phrasing
- Expanded campus service coverage

### Explicit Non-Goals
- No user accounts or authentication
- No personalized recommendations
- No advanced AI training or fine-tuning
- No production deployment

---

## 5. Acceptance Criteria

- Users can submit a question and receive a relevant response end-to-end.
- The chatbot produces an answer within **3 seconds**.
- The system correctly handles unknown or unclear questions.
- The chatbot fails safely by informing the user when information is unavailable.
- All responses are readable and concise.

---

## 6. Assumptions + Constraints

### Assumptions
- Official TAMUSA information is publicly available.
- Users will ask common, repetitive questions.

### Constraints
- Limited development time before Milestone 2.
- No access to private university databases.
- Must use low-cost or free technologies.
- Must respect privacy and avoid collecting personal data.
