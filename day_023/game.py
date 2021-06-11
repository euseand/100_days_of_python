from turtle import Screen
from time import sleep

from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard
from constants import SCREEN_WIDTH, SCREEN_HEIGHT


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

    cars.move()

    if player.ycor() == SCREEN_HEIGHT/2:
        player.reset_position()
        score.increase_score()

screen.exitonclick()
