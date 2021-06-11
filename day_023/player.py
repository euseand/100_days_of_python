from turtle import Turtle

from constants import PLAYER_STARTING_POSITION, PLAYER_MOVE_DISTANCE, UP


class Player(Turtle):
    """Class represents the Player of the Turtle Crossing game"""

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('red')
        self.shapesize(stretch_wid=1.2, stretch_len=1.2)
        self.penup()
        self.move_speed = 0.1
        self.setheading(UP)
        self.reset_position()

    def move(self):
        self.forward(PLAYER_MOVE_DISTANCE)

    def reset_position(self):
        self.goto(PLAYER_STARTING_POSITION)