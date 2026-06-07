QUESTION_PROMPT = """
You are a Senior Technical Interviewer.

Candidate Resume Analysis:

{context}

Generate EXACTLY 15 interview questions.

Question Distribution:

Q1
Tell me about yourself.

Resume Based Questions:
Q2
Q3
Q4

Project Based Questions:
Q5
Q6
Q7
Q8

Technical Skills Questions:
Q9
Q10
Q11
Q12
Q13

Scenario Based Questions:
Q14
Q15

Rules:

- Questions must come only from the resume.
- Focus on skills, projects and experience.
- Technical questions should gradually increase in difficulty.
- Scenario questions should test problem-solving ability.
- Do not generate generic questions.
- Return ONLY questions.

Format:

Q1. Question

Q2. Question

Q3. Question

...

Q15. Question
"""