from utils import clear_message, caesar
from constants import LOGO

while True:

    print(LOGO)

    while True:
        action = input('Type "encode" to encrypt, type "decode" to decrypt:\n').lower()
        if action not in {'encode', 'decode'}:
            print('Unnknown action. Please try again.\n')
            continue
        break

    message = list((input('\nType your message:\n').lower()))
    message = clear_message(message)
    print(f'Everything but chars has been removed from message: {"".join(message)}\n')

    while True:
        try:
            shift = int(input('\nType the shift number:\n'))
        except ValueError:
            print('It is not valid integer. Please try again.\n')
            continue
        break

    if action == 'encode':
        print(f'\nHere is the encoded result:\n{caesar(action, message, shift)}')
    elif action == 'decode':
        print(f'\nHere is the decoded result:\n{caesar(action, message, shift)}')

    choice = input('Type "yes" if you want to go again. Otherwise type "no".\n').lower()
    if choice == 'no':
        break
