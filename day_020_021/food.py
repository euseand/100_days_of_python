from turtle import Turtle
from random import randint


class Food(Turtle):
    """Class represents Food objects from the Snake game"""
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.75, stretch_wid=0.75)
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        rand_x, rand_y = randint(-280, 280), randint(-270, 270)
        self.goto(rand_x, rand_y)
