from langchain_core.prompts import PromptTemplate

from llm.nvidia_llm import get_llm

from prompts.evaluation_prompt import (
    EVALUATION_PROMPT
)

from prompts.final_evaluation_prompt import (
    FINAL_EVALUATION_PROMPT
)

from prompts.introduction_prompt import (
    INTRODUCTION_PROMPT
)

import re


# ---------------------------------
# Question Evaluation
# ---------------------------------

def evaluate_answer(question,answer):

    if "tell me about yourself" in question.lower():

        prompt = PromptTemplate(
            template=INTRODUCTION_PROMPT,
            input_variables=[
                "question",
                "answer"
            ]
        )

    else:

        prompt = PromptTemplate(
            template=EVALUATION_PROMPT,
            input_variables=[
                "question",
                "answer"
            ]
        )

    chain = prompt | get_llm()

    response = chain.invoke(
        {
            "question": question,
            "answer": answer
        }
    )

    return response.content




def generate_final_feedback(
    qa_data
):

    prompt = PromptTemplate(
        template=FINAL_EVALUATION_PROMPT,
        input_variables=[
            "qa_data"
        ]
    )

    chain = prompt | get_llm()

    response = chain.invoke(
        {
            "qa_data": qa_data
        }
    )

    return response.content



def calculate_interview_score(
    candidate_answers
):

    total_score = 0

    total_questions = 0

    for item in candidate_answers:

        evaluation = item["evaluation"]

        match = re.search(
            r"Overall Score:\s*(\d+)/30",
            evaluation
        )

        if match:

            total_score += int(
                match.group(1)
            )

            total_questions += 1

    if total_questions == 0:

        return 0

    average_30 = (
        total_score /
        total_questions
    )

    average_10 = round(
        average_30 / 3,
        2
    )

    return average_10



def evaluate_interview(
    resume_analysis,
    candidate_answers
):

    qa_data = ""

    for item in candidate_answers:

        qa_data += f"""

Question:
{item['question']}

Answer:
{item['answer']}

Evaluation:
{item['evaluation']}

"""

    return generate_final_feedback(
        qa_data
    )