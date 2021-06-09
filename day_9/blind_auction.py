from os import system


print('Welcome to the secret auction program.')
bids = dict()
while True:
    name = input('What is your name?: ')
    bid = int(input('What is your bid?: $'))
    bids[name] = bid
    
    while True:
        choice = input('Are there any other bidders? Type "yes" or "no".\n').lower()
        if choice not in {'yes', 'no'}:
            print('Unknown action. Please try again.\n')
            continue
        break
    
    if choice == 'no':
       highest = max(bids, key=bids.get)
       print(f'The winner is {highest} with the bid of {bids[highest]}')
       break
    else:
        system('clear')