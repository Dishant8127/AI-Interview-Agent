INTRODUCTION_PROMPT = """
You are a Senior HR Interviewer.

Question:
{question}

Candidate Answer:
{answer}

Evaluate the answer based on:

1. Communication (0-10)
2. Confidence (0-10)
3. Completeness (0-10)

IMPORTANT:

Communication: X/10

Confidence: X/10

Completeness: X/10

Overall Score: X/30

Short Feedback:
Write 2-3 lines of feedback.
"""