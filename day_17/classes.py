class Question:
    """Class represents quiz questions"""

    def __init__(self, content, answer):
        self.content = content
        self.answer = answer


class Quiz:
    """Class represents quiz"""

    def __init__(self, q_list):
        self.score = 0
        self.question_number = 0
        self.questions_list = q_list

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f'Q.{self.question_number}: {current_question.content} (True/False): ')
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print(f'You got it right!')
        else:
            print(f'That is wrong!\nThe correct answer was {correct_answer}.')
        print(f'Your current score is {self.score}/{self.question_number}')
