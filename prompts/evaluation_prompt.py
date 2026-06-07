EVALUATION_PROMPT = """
You are a Senior Technical Interviewer.

Question:
{question}

Candidate Answer:
{answer}

Evaluate the answer based on:

1. Technical Accuracy (0-10)
2. Communication (0-10)
3. Completeness (0-10)

IMPORTANT:

Give scores in EXACT format:

Technical Accuracy: X/10

Communication: X/10

Completeness: X/10

Overall Score: X/30

Short Feedback:
Write 2-3 lines of feedback.
"""