from rag.retriever import get_retriever

from llm.nvidia_llm import get_llm


def analyze_resume():

    retriever = get_retriever()

    docs = retriever.invoke(
        "Extract skills, projects, experience and candidate details."
    )

    context = "\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
    You are an expert Resume Analyzer.

    Resume Context:
    {context}

    Extract only information available in the resume.

    Return EXACTLY in this format:

    Candidate Name:
    Dishant Vekariya

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

    IMPORTANT:
    - Keep each section on a new line.
    - Each skill must be on a separate line.
    - Each project must be on a separate line.
    - Each experience must be on a separate line.
    - Do not return everything in one paragraph.
    - Do not use markdown.
    - Return plain text only.
    """

    llm = get_llm()

    response = llm.invoke(prompt)

    return response.content