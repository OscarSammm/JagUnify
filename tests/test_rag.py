import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from retrieval import load_index
from generator import jag_query_engine
from citation_formatter import format_citations

TEST_CASES = [
    # Grounded — catalog-scoped academic advising questions
    (1,  "What are the graduation requirements for undergraduate students at TAMUSA?"),
    (2,  "What is the required GPA to avoid academic probation?"),
    (3,  "What are the core curriculum requirements for a Bachelor of Science degree?"),
    (4,  "What courses are required for the Computer Science degree?"),
    (5,  "What is the maximum number of credit hours a student can take per semester?"),
    (6,  "How does a student appeal a grade at TAMUSA?"),
    (7,  "What are the admission requirements for first-year students?"),
    (8,  "What transfer credit policies apply to incoming transfer students?"),
    (9,  "What is the academic calendar for the upcoming fall semester?"),
    (10, "How can a student apply for financial aid at TAMUSA?"),
    (11, "What are the requirements for the Business Administration degree?"),
    (12, "What graduate programs does TAMUSA offer?"),
    (13, "What is the minimum GPA required to graduate?"),
    (14, "How many total credit hours are needed to earn a bachelor's degree?"),
    # Refusal — out of scope
    (15, "What are the operating hours of the TAMUSA library?"),
    (16, "What meal plans are available on campus?"),
    (17, "Where can I find on-campus parking at TAMUSA?"),
    (18, "Does TAMUSA have a football team?"),
    (19, "What NFL players graduated from TAMUSA?"),
    (20, "What is the average starting salary for TAMUSA graduates?"),
]

if __name__ == "__main__":
    index = load_index()
    engine = jag_query_engine(index)

    for num, question in TEST_CASES:
        print(f"\n{'='*60}")
        print(f"TEST CASE {num}")
        print(f"Question: {question}")

        response = engine.query(question)
        result = format_citations(response)

        print(f"Answer: {result['answer']}")

        if result['sources']:
            print("Sources:")
            for src in result['sources']:
                score_str = f" (score: {src['score']})" if src['score'] is not None else ""
                print(f"  [{src['id']}] {src['url']}{score_str}")
                print(f"       {src['snippet']}")
        else:
            print("Sources: None (Refusal)")

    print(f"\n{'='*60}")
    print("All test cases complete.")
