from string import ascii_letters, digits, punctuation
from random import choice, shuffle, randint


def generate_password(pass_length: int) -> str:
    """Generates a strong password accodring to length and typed chars amount"""

    num_letters, num_digits = randint(10, 15), randint(10, 15)
    num_punctuation = pass_length - num_letters - num_digits

    password = []
    password.extend([choice(ascii_letters) for _ in range(num_letters)])
    password.extend([choice(digits) for _ in range(num_digits)])
    password.extend([choice(punctuation) for _ in range(num_punctuation)])

    shuffle(password)
    password = ''.join(password)

    return password
