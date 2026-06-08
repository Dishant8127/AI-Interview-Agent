
from rag.retriever import get_retriever

from llm.nvidia_llm import get_llm

from langchain_core.prompts import PromptTemplate

from prompts.resume_prompt import RESUME_PROMPT


def analyze_resume():


    retriever = get_retriever()

    docs = retriever.invoke(
        "Extract skills, projects, experience and candidate details."
    )

    context = "\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = PromptTemplate(
        template=RESUME_PROMPT,
        input_variables=["context"]
    )

    chain = prompt | get_llm()

    response = chain.invoke(
        {
            "context": context
        }
    )

    return response.content