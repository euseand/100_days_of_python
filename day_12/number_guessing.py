from random import randint

from constants import ART


while True:
    print(ART)
    print('Welcome to the Number Guessing Game!\nI am thinking of a number between 1 and 100.')

    
    while True:
        difficulty = input('Chose a difficulty. Type "easy" or "hard": ').lower()
        if difficulty not in {'easy', 'hard'}:
            print('Unknown difficulty. Please try again.')
            continue
        break

    if difficulty == 'easy':
        tries = 10
    if difficulty == 'hard':
        tries = 5

    number = randint(1, 101)
    while True:
        if tries > 0:
            print(f'You have {tries} attempts remaining to guess the number.')
        else:
            print('You have run out of guesses, you lose.')
            break

        try:
            guess = int(input('Make a guess: '))
        except ValueError:
            print('This is not a valid integer number. Please try again.')
            continue

        if guess > number:
            print('Too high.\nGuess again.')
        if guess < number:
            print('Too low.\nGuess again.')
        if guess == number:
            print(f'You got it! The answer was {number}')
            break
        tries -= 1
        
    
    while True:
        end = input('Do you want to play again? Type "y" or "n": ').lower()
        if end not in {'y', 'n'}:
            print('Unknown action. Please try again.\n')
            continue
        break

    if end == 'n':
        break