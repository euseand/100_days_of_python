from string import ascii_letters, digits, punctuation
from random import choice, shuffle


def generate_password(pass_length: int, num_letters: int, num_digits: int, num_punctuation: int) -> str:
    """Generates a strong password accodring to length and typed chars amount"""

    password = []
    password.extend([choice(ascii_letters) for _ in range(num_letters)])
    password.extend([choice(digits) for _ in range(num_digits)])
    password.extend([choice(punctuation) for _ in range(num_punctuation)])

    shuffle(password)
    password = ''.join(password)

    return password