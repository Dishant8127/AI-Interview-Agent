from rag.retriever import get_retriever
from llm.nvidia_llm import get_llm


def analyze_resume():

    retriever = get_retriever()

    docs = retriever.invoke(
        "Extract Skills, Projects, and Experience from the candidate's resume."
    )

    context = "\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
    You are an expert Resume Analyzer.

    Your task is to analyze the resume and extract only the information available in the resume.

    Resume Context:
    {context}

    Instructions:
    1. Extract all technical skills.
    2. Extract all project names.
    3. Extract work experience details.
    4. Do not add any information that is not present in the resume.
    5. Return the response in the exact format below.

    Format:

    Skills:
    - Skill 1
    - Skill 2
    - Skill 3

    Projects:
    - Project 1
    - Project 2
    - Project 3

    Experience:
    - Experience 1
    - Experience 2

    Answer:
    """


    llm = get_llm()

    response = llm.invoke(prompt)

    return response.content