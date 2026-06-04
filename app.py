from agents.resume_agent import analyze_resume
from agents.question_agent import generate_questions

print("\n" + "=" * 60)
print("RESUME ANALYSIS")
print("=" * 60)

analysis = analyze_resume()

print(analysis)

print("\n" + "=" * 60)
print("INTERVIEW QUESTIONS")
print("=" * 60)

questions = generate_questions()

print(questions)

print("=" * 60)