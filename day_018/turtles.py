from turtle import Turtle, Screen


turt = Turtle()
scr = Screen()


def move_forward():
    turt.forward(10)


def move_backward():
    turt.back(10)


def turn_left():
    curr = turt.heading()
    turt.setheading(curr + 10)


def turn_right():
    curr = turt.heading()
    turt.setheading(curr - 10)


def clear():
    turt.clear()
    turt.penup()
    turt.home()
    turt.pendown()

scr.listen()
scr.onkey(key='Up', fun=move_forward)
scr.onkey(key='Down', fun=move_backward)
scr.onkey(key='Left', fun=turn_left)
scr.onkey(key='Right', fun=turn_right)
scr.onkey(key='space', fun=clear)


scr.exitonclick()
