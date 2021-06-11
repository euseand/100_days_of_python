from turtle import Turtle

from constants import SCORE_POSITION, ALIGNMENT, FONT


class ScoreBoard(Turtle):
    """Class represents Score Board of the Turtle Crossing game"""
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(SCORE_POSITION)
        self.update()

    def increase_score(self):
        self.score += 1
        self.update()

    def update(self):
        self.clear()
        self.write(f'Level {self.score}', align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f'Game Over. \nThe final score: {self.score}.', align=ALIGNMENT, font=FONT)
