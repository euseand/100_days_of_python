from random import choice

from constants import STAGES, WORD_LIST

while True:
    word = choice(WORD_LIST)
    blanks = list(['_' for _ in word])

    lives = 6
    while '_' in blanks and lives > 0:
        print(''.join(blanks))
        print(STAGES[lives])
        guess = input('Guess a letter (0 to exit): ')
        print('----------------------------------------------------------------')

        if guess == '0':
            break

        if guess in blanks:
            print(f'You have already guessed {guess}. You want to die or what?\n')

        if guess in word:
            for idx, letter in enumerate(word):
                if letter == guess:
                    blanks[idx] = letter
        else:
            lives -= 1
            print(f'You guessed {guess}. It is not in a word.\n')

    if lives == 0:
        print(STAGES[lives])
        print(f'You have lost. It was the word "{word}"')
    else:
        print(f'You have won. It was the word "{word}"')
    
    choice = input('\nLeave blank to exit or enter something to play again.')
    if not choice:
        break
