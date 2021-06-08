from random import randint
from constants import ROCK, PAPER, SCISSORS

print_choices = [ROCK, PAPER, SCISSORS]
while True:
    player = int(input('What do you choose? Type 0 for rock, 1 for paper, 2 for scissors. 3 to exit game.\n'))
    if player == 3:
        break
    computer = randint(0, 2)
    print(print_choices[player])

    print('Computer move:\n')
    print(print_choices[computer])

    if player == 0 and computer == 1 or player == 1 and computer == 2 or player == 2 and computer == 0:
        print('You lose')
    elif player == computer:
        print('It is a draw.')
    else:
        print('You win')
