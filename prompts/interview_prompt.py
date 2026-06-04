QUESTION_PROMPT = """
You are a senior technical interviewer.

Based on the candidate's resume context below:

{context}

Generate:

1. 5 Easy Questions
2. 5 Medium Questions
3. 5 Hard Questions

Rules:

- Questions must be based only on candidate skills.
- Ask practical interview questions.
- Focus on projects and technologies.
- Do not generate generic questions.

Output format:

EASY:
1.
2.

MEDIUM:
1.
2.

HARD:
1.
2.
"""