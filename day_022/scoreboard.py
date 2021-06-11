from turtle import Turtle

from constants import ALIGNMENT, FONT


class ScoreBoard(Turtle):
    """Class represents Score Board of the Snake game"""
    def __init__(self):
        super().__init__()
        self.left_player_score = 0
        self.right_player_score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 220)
        self.update()

    def increase_score(self, player):
        if player == 'right':
            self.right_player_score += 1
        elif player == 'left':
            self.left_player_score += 1
        self.update()

    def update(self):
        self.clear()
        self.write(f'{self.left_player_score} : {self.right_player_score}', align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        if self.right_player_score > self.left_player_score:
            self.write(
                f'Game Over. Right player wins.\nThe final score: {self.left_player_score} : {self.right_player_score}',
                align=ALIGNMENT, font=FONT)
        elif self.left_player_score > self.right_player_score:
            self.write(
                f'Game Over. Left player wins\nThe final score: {self.left_player_score} : {self.right_player_score}',
                align=ALIGNMENT, font=FONT)
        else:
            self.write(
                f'Game Over. It is a draw.\nThe final score: {self.left_player_score} : {self.right_player_score}',
                align=ALIGNMENT, font=FONT)
