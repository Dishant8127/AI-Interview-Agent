from langchain_core.prompts import PromptTemplate

from llm.nvidia_llm import get_llm

from prompts.interview_prompt import (
    QUESTION_PROMPT
)

import re


def generate_questions(context):

    prompt = PromptTemplate(
        template=QUESTION_PROMPT,
        input_variables=["context"]
    )

    chain = prompt | get_llm()

    response = chain.invoke(
        {
            "context": context
        }
    )

    text = response.content

    questions = re.findall(
        r"Q\d+\.\s.*",
        text
    )

    return questions