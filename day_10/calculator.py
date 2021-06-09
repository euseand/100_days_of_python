from utils import calculate


result = None

while True:    

    if not result:
        while True:
            try:
                first = float(input('What is the first number?: '))
            except ValueError:
                print('It is not valid integer. Please try again.\n')
                continue
            break

    while True:
        operation = input('+\n-\n*\n/\nPick an operation: ')
        if operation not in {'+', '-', '*', '/'}:
            print('Unknown operation. Please try again.')
            continue
        break

    while True:
        try:
            second = float(input('What is the second numbere?: '))
        except ValueError:
            print('It is not valid integer. Please try again.\n')
            continue
        break

    result = calculate(first, second, operation)
    print(f'{first} {operation} {second} = {result}')

    while True:
        choice = input(f'Type "y" to continue calculating with {result}, or type "n" to start a new calculation. Leave blank to exit.\n').lower()
        if choice not in {'y', 'n', ''}:
            print('Unknown action. Please try again.\n')
            continue
        break
    
    if choice == 'n':
        result = None
    elif choice == 'y':
        continue
    elif choice == '':
        break