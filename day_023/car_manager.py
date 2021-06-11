from turtle import Turtle
from random import randint

from constants import SCREEN_WIDTH, SCREEN_HEIGHT, CAR_MOVE_DISTANCE


class CarManager:
    def __init__(self):
        self.cars = []
        for _ in range(100):
            self.create_car()
            self.move_speed = 0.1

    def create_car(self):
        car = Turtle()
        car.shape('square')
        car.penup()
        car.shapesize(stretch_len=2, stretch_wid=1)
        car.setheading(180)
        random_color = (randint(1, 255), randint(1, 255), randint(1, 255))
        car.color(random_color)
        random_position = (randint(-SCREEN_WIDTH/2, SCREEN_WIDTH/2+50),
                           randint(-SCREEN_HEIGHT/2+70, SCREEN_HEIGHT/2-70))
        car.goto(random_position)
        self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.forward(CAR_MOVE_DISTANCE)
