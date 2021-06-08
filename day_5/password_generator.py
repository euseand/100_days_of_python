from utils import generate_password

while True:
    pass_len = int(input('How many chars you want to be in your password?\n(Enter 0 to exit)\n'))
    if pass_len == 0:
        break

    """
    Custom char type numbers

    num_letters = int(input('How many letters you want to be in your password?\n'))
    num_digits = int(input('How many digits you want to be in your password?\n'))
    num_punctuation = int(input('How many punctuation signs you want to be in your password?\n'))

    if num_letters + num_digits + num_punctuation > pass_len or num_letters + num_digits + num_punctuation < pass_len:
        print('\nSum of chars in password must be same as the sum of the char types.\n')
    else:
    """
    password = generate_password(pass_len)

    print(f'\nYour new safe password is {password}')

    inp = input('\nEnter anything to create a new password or 0 to exit.\n')
    if inp == 0:
        break
    else:
        continue