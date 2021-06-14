from turtle import Turtle
from random import randint

from constants import SCREEN_WIDTH, SCREEN_HEIGHT, CAR_MOVE_DISTANCE, CAR_MOVE_INCREMENT


class CarManager:
    def __init__(self):
        self.cars = []
        #for _ in range(100):
        #    self.create_car()
        self.move_speed = 0.1
        self.move_distance = CAR_MOVE_DISTANCE

    def create_car(self):
        random_chance = randint(1, 6)
        if random_chance == 1:
            car = Turtle('square')
            car.penup()
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.setheading(180)
            random_color = (randint(1, 255), randint(1, 255), randint(1, 255))
            car.color(random_color)
            rand_x = randint(SCREEN_WIDTH/2, SCREEN_WIDTH/2+50)
            rand_y = randint(-SCREEN_HEIGHT/2+70, SCREEN_HEIGHT/2-70)
            car.goto(rand_x, rand_y)
            self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.forward(self.move_distance)

    def increase_speed(self):
        self.move_distance += CAR_MOVE_INCREMENT

    def reset_cars(self):
        for car in self.cars:
            car.visible(0)
