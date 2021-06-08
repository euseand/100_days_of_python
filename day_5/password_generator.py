import string
import random


pass_len = int(input('Welcome to PyPassword Generator\nHow many letters you want to be in your password?\n'))

chars = string.printable
print(chars)
password = ''.join([random.choice(chars) for _ in range(pass_len)])
print(str(password))