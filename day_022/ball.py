from turtle import Turtle

from constants import BALL_MOVE_DISTANCE


class Ball(Turtle):
    """Class represents Ball object for the Pong game"""
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.color('white')
        self.penup()
        self.x_move = BALL_MOVE_DISTANCE
        self.y_move = 2*BALL_MOVE_DISTANCE
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_vert(self):
        self.y_move *= -1

    def bounce_hor(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_hor()
        # self.bounce_vert()
