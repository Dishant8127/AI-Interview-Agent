from langchain_core.prompts import PromptTemplate

from llm.nvidia_llm import get_llm

from prompts.interview_prompt import QUESTION_PROMPT

from agents.resume_agent import analyze_resume


def generate_questions():

    context = analyze_resume()

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

    return response.content