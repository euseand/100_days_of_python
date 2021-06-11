from turtle import Screen
from time import sleep

from snake import Snake
from food import Food
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(fun=snake.turn_up, key='Up')
screen.onkey(fun=snake.turn_down, key='Down')
screen.onkey(fun=snake.turn_left, key='Left')
screen.onkey(fun=snake.turn_right, key='Right')

is_game_on = True
while is_game_on:
    screen.update()
    snake.move()
    sleep(0.1)

    # detect food collision
    if snake.head.distance(food) < 15:
        snake.extend()
        food.refresh()
        score.increase_score()

    # detect wall collision
    if snake.head.xcor() >= 290 or snake.head.xcor() <= -310 or snake.head.ycor() >= 310 or snake.head.ycor() <= -300:
        is_game_on = False
        score.game_over()
    # detect self collision
    for part in snake.body[1:]:
        if snake.head.distance(part) < 10:
            is_game_on = False
            score.game_over()


screen.exitonclick()
