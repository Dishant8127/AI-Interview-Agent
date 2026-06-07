FINAL_EVALUATION_PROMPT = """
You are a Senior Technical Interview Panel.

Interview Evaluation Data:

{qa_data}

Create a professional final interview report.

Return EXACT format

PERFORMANCE SUMMARY:

Resume Understanding:
Excellent / Good / Average / Poor

Project Discussion:
Excellent / Good / Average / Poor

Technical Knowledge:
Excellent / Good / Average / Poor

Problem Solving:
Excellent / Good / Average / Poor

Communication Skills:
Excellent / Good / Average / Poor


KEY STRENGTHS:

* Strength 1
* Strength 2
* Strength 3
* Strength 4


AREAS FOR IMPROVEMENT:

* Improvement 1
* Improvement 2
* Improvement 3


RECOMMENDATIONS:

* Recommendation 1
* Recommendation 2
* Recommendation 3


FINAL VERDICT:

Write a 4-5 line final assessment.

Return plain text only.
"""
