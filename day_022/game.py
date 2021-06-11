from turtle import Screen
from time import sleep

from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, \
    RIGHT_PADDLE_STARTING_POSITION, LEFT_PADDLE_STARTING_POSITION

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor('black')
screen.title('Pong Game')
screen.tracer(0)

l_player = Paddle(LEFT_PADDLE_STARTING_POSITION)
r_player = Paddle(RIGHT_PADDLE_STARTING_POSITION)
ball = Ball()
score = ScoreBoard()

screen.listen()
screen.onkey(l_player.move_up, 'w')
screen.onkey(l_player.move_down, 's')
screen.onkey(r_player.move_up, 'Up')
screen.onkey(r_player.move_down, 'Down')

is_game_on = True
while is_game_on:
    screen.update()
    sleep(ball.move_speed)
    ball.move()

    # detect collision with floor and ceiling
    if ball.ycor() + 40 > SCREEN_HEIGHT/2 or ball.ycor() - 40 < -SCREEN_HEIGHT/2:
        ball.bounce_vert()

    # detect collision with paddles
    if ball.distance(l_player) < 50 and ball.xcor() - 20 > l_player.xcor():
        ball.bounce_hor()
        ball.bounce_vert()
    elif ball.distance(r_player) < 50 and ball.xcor() < r_player.xcor():
        ball.bounce_hor()
        ball.bounce_vert()

    # detect paddle misses
    if ball.xcor() - 40 < -SCREEN_WIDTH/2:
        score.increase_score('right')
        ball.reset_position()
    elif ball.xcor() + 40 > SCREEN_WIDTH/2:
        score.increase_score('left')
        ball.reset_position()

    # detect game over
    if score.left_player_score > 2 or score.right_player_score > 2:
        score.game_over()
        is_game_on = False

screen.exitonclick()
