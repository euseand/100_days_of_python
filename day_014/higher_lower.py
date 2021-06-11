from random import choice
from os import system

from constants import DATA


while True:
    print('Welcome to the Higher Lower Game!\n')

    score = 0
    while True:
        first = choice(DATA)
        second = choice(DATA)
        if first == second:
            continue

        print(f'\nCompare A: {first["name"]}, a {first["description"]}, from {first["country"]}')
        print(f'Compare B: {second["name"]}, a {second["description"]}, from {second["country"]}')

        while True:
            guess = input('\nWho has more followers? Type "A" or "B": ').lower()
            if guess not in {'a', 'b'}:
                print('Unknown action. Please try again.\n')
                continue
            break

        if first["follower_count"] > second["follower_count"] and guess == 'a' or \
                first["follower_count"] < second["follower_count"] and guess == 'b':
            score += 1
            system('clear')
            print(f'\nThat is right. Score: {score}')
            continue
        else:
            system('clear')
            print(f'\nSorry, that is wrong. Final score: {score}')
            break

    while True:
        end = input('Do you want to play again? Type "y" or "n": ').lower()
        if end not in {'y', 'n'}:
            print('Unknown action. Please try again.\n')
            continue
        break

    if end == 'n':
        break
