import turtle
import pandas as pd

from constants import SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_IMAGE_PATH
from state import StateManager


screen = turtle.Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title('US States Quiz')
screen.addshape(BACKGROUND_IMAGE_PATH)

manager = StateManager()

turtle.shape(BACKGROUND_IMAGE_PATH)

is_game_on = True
while is_game_on:
    answer_state = screen.textinput(title=f'{manager.guessed_states_num}/{len(manager.states)} States Correct',
                                    prompt='Name another state.')
    if answer_state == 'exit':
        to_learn = [state for state in manager.states if state[0].lower() not in manager.guessed_states_list]
        pd.DataFrame(to_learn).to_csv('./states_to_learn.csv')
        break
    if answer_state:
        answer_state = answer_state.lower()
    for state in manager.states:
        if answer_state == state[0].lower():
            if answer_state not in manager.guessed_states_list:
                manager.guess_right(state)
    if manager.guessed_states_num == 50:
        is_game_on = False
