from fastapi import FastAPI,Request,UploadFile,File,Form

from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

import os
import time

from agents.resume_agent import analyze_resume
from agents.question_agent import generate_questions
from agents.evaluation_agent import evaluate_interview, evaluate_answer, calculate_interview_score

from rag.pdf_loader import load_pdf
from rag.text_splitter import split_documents

from rag.vector_store import create_vector_store,clear_index
from agents.selection_agent import get_selection_result


app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)


questions = []

candidate_answers = []

current_question_index = 0

resume_analysis = ""

interview_completed = False

MAX_QUESTIONS = 5

@app.get("/")
def home(request: Request):

    global interview_completed

    if interview_completed:
        interview_completed = False

    return templates.TemplateResponse(
        request=request,
        name="upload.html",
        context={}
    )


@app.post("/upload")
async def upload_resume(request: Request,resume: UploadFile = File(...)):

    global resume_analysis

    file_path = (f"data/resumes/{resume.filename}")

    with open(file_path, "wb") as file:

        content = await resume.read()

        file.write(content)

    documents = load_pdf(file_path)

    chunks = split_documents(documents)

    clear_index()
    create_vector_store(chunks)
    time.sleep(5)
    resume_analysis = analyze_resume()

    return templates.TemplateResponse(
        request=request,
        name="analysis.html",
        context={
            "analysis": resume_analysis
        }
    )

@app.get("/start-interview")
def start_interview(request: Request):

    global questions
    global current_question_index
    global candidate_answers
    global resume_analysis

    current_question_index = 0

    candidate_answers.clear()

    questions = generate_questions(resume_analysis)

    if len(questions) == 0:

        questions = ["Q1. Tell me about yourself."]

    return templates.TemplateResponse(
        request=request,
        name="interview.html",
        context={
            "question": questions[0],
            "question_number": 1
        }
    )


@app.post("/submit-answer")
def submit_answer(request: Request,answer: str = Form(...)):


    global current_question_index
    global interview_completed

    current_question = questions[current_question_index ]


    candidate_answers.append(
        {
            "question": current_question,
            "answer": answer
        }
    )

    current_question_index += 1


    if current_question_index >= MAX_QUESTIONS:

        interview_completed = True


        for item in candidate_answers:

            evaluation = evaluate_answer(
                item["question"],
                item["answer"]
            )

            item["evaluation"] = evaluation


        overall_score = calculate_interview_score(candidate_answers)

        decision = get_selection_result(overall_score)
        final_result = evaluate_interview( resume_analysis,candidate_answers)

        return templates.TemplateResponse(
            request=request,
            name="result.html",
            context={
                "answers": candidate_answers,
                "final_result": final_result,
                "overall_score": overall_score,
                "decision": decision
            }
        )


    next_question = questions[ current_question_index]

    return templates.TemplateResponse(
        request=request,
        name="interview.html",
        context={
            "question": next_question,
            "question_number":
                current_question_index + 1
        }
    )


@app.get("/reset")
def reset():

    global questions
    global current_question_index
    global candidate_answers
    global interview_completed
    global resume_analysis

    questions = []

    current_question_index = 0

    candidate_answers.clear()

    interview_completed = False

    resume_analysis = ""

    return RedirectResponse(
        url="/",
        status_code=302
    )