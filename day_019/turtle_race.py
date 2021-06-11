from turtle import Turtle, Screen
from random import randint


scr = Screen()
scr.setup(width=500, height=400)

race = False
user_bet = scr.textinput(title='Make a bet on a turtle.', prompt='Enter a color: ')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
turts = []

y_cord = 90

for _ in range(6):
    turt = Turtle(shape='turtle')
    turt.color(colors[_])
    turt.penup()
    turt.goto(x=-240, y=y_cord)
    y_cord -= 30
    turts.append(turt)

if user_bet:
    race = True

while race:
    for turt in turts:
        dist = randint(0, 10)
        turt.forward(dist)
        if turt.xcor() > 210:
            win = turt.pencolor()
            if win == user_bet:
                print(f'You have won! The {win} turt is first!')
            else:
                print(f'You have lost! The {win} turt is first!')
            race = False


scr.exitonclick()
