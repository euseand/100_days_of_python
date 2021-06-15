import tkinter as tk

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
WHITE = "#ffffff"


class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz

        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = tk.Label(text=f"Score: 0", background=THEME_COLOR, fg=WHITE)
        self.score_label.grid(column=1, row=0)

        self.canvas = tk.Canvas(width=300, height=250, bg=WHITE)
        self.question_text = self.canvas.create_text(150, 120, text="Question goes here", font=("Roboto", 20, "bold"),
                                                     fill=THEME_COLOR, width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=10)

        false_image = tk.PhotoImage(file="./images/false.png")
        self.false_button = tk.Button(image=false_image, highlightthickness=0, command=self.check_false)
        self.false_button.grid(column=0, row=2, pady=10)

        true_image = tk.PhotoImage(file="./images/true.png")
        self.true_button = tk.Button(image=true_image, highlightthickness=0, command=self.check_true)
        self.true_button.grid(column=1, row=2, pady=10)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg=WHITE)
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You've reached the end of the quiz. "
                                                            f"Your score is {self.quiz.score}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def check_true(self):
        self.feedback(self.quiz.check_answer("True"))

    def check_false(self):
        self.feedback(self.quiz.check_answer("False"))

    def feedback(self, is_right):
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if is_right:
            self.canvas.config(bg="green")
            self.window.after(500, self.get_next_question)
        else:
            self.canvas.config(bg="red")
            self.window.after(500, self.get_next_question)
