from string import ascii_lowercase


def caesar(action, message, shift):
    if action == 'decode':
        shift *= -1
    for idx, letter in enumerate(message):
        pos = ascii_lowercase.index(letter)
        new_pos = (pos + shift) % len(ascii_lowercase)
        message[idx] = ascii_lowercase[new_pos]
    return ''.join(message)


def clear_message(message):
    return list([char for char in message if char in ascii_lowercase])
