import requests

URL = "https://opentdb.com/api.php?amount=10&difficulty=medium&type=boolean"

question_data = []
for _ in range(10):
    r = requests.get(URL).json().get("results")
    question_data += [{"question": q.get("question"), "answer": q.get("correct_answer")} for q in r]
