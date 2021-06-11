from turtle import Turtle

from constants import PADDLE_MOVE_DISTANCE, SCREEN_HEIGHT


class Paddle(Turtle):
    """Class represents the paddle of the Pong game"""

    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color('white')
        self.penup()
        self.goto(position)

    def move_up(self):
        new_y = self.ycor() + PADDLE_MOVE_DISTANCE
        if new_y + 50 <= SCREEN_HEIGHT / 2:
            self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - PADDLE_MOVE_DISTANCE
        if new_y - 50 >= -SCREEN_HEIGHT / 2:
            self.goto(self.xcor(), new_y)
