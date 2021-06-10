from constants import QUESTIONS
from classes import Question, Quiz


question_bank = list([Question(content=item['question'], answer=item['correct_answer']) for item in QUESTIONS])

quiz = Quiz(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f'\nYou have completed the quiz.\nYour final score is {quiz.score}/{quiz.question_number}')
