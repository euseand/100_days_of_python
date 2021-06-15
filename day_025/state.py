from turtle import Turtle
import pandas as pd

from constants import STATES_DATA_PATH


class StateManager:
    """Class representing the manager for the State objects"""
    def __init__(self):
        self.states = list(zip(pd.read_csv(STATES_DATA_PATH).state.to_list(),
                               pd.read_csv(STATES_DATA_PATH).x.to_list(),
                               pd.read_csv(STATES_DATA_PATH).y.to_list()))
        self.guessed_states_num = 0
        self.guessed_states_list = []

    @staticmethod
    def get_mouse_click_coor(x, y):
        print(x, y)

    def guess_right(self, state):
        print(state)
        self.guessed_states_num += 1
        self.guessed_states_list.append(state[0].lower())
        t = Turtle()
        t.hideturtle()
        t.penup()
        t.goto(state[1], state[2])
        t.write(state[0])
