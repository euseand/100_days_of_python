from turtle import Turtle

from constants import ALIGNMENT, FONT


class ScoreBoard(Turtle):
    """Class represents Score Board of the Snake game"""
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update()

    def update(self):
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f'Game Over. Your score: {self.score}', align=ALIGNMENT, font=FONT)
