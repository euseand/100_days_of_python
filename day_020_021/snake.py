from turtle import Turtle

from constants import STARTING_POSITIONS, MOVE_DISTANCE, UP, DOWN, LEFT, RIGHT


class Snake:
    """Class represents Snake from the Snake game"""

    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]
        self.tail = self.body[-1]

    def add_part(self, position):
        snake_part = Turtle(shape='square')
        snake_part.color('white')
        snake_part.penup()
        snake_part.goto(position)
        self.body.append(snake_part)

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_part(position)

    def extend(self):
        self.add_part(self.tail.position())

    def move(self):
        for part_number in range(len(self.body) - 1, 0, -1):
            new_x = self.body[part_number - 1].xcor()
            new_y = self.body[part_number - 1].ycor()
            self.body[part_number].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def turn_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def turn_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
