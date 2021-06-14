from turtle import Screen
from time import sleep

from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, FINISH_LINE


screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.colormode(255)
screen.title('Turtle Crossing')
screen.tracer(0)

player = Player()
cars = CarManager()
score = ScoreBoard()

screen.listen()
screen.onkey(player.move, 'w')

is_game_on = True
while is_game_on:
    screen.update()
    sleep(cars.move_speed)
    cars.create_car()
    cars.move()

    # detect collision with cars
    for car in cars.cars:
        if car.distance(player) < 20:
            score.game_over()
            is_game_on = False

    if player.ycor() >= FINISH_LINE:
        player.reset_position()
        score.increase_score()
        cars.increase_speed()

screen.exitonclick()
