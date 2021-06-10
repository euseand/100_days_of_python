from utils import init_game, deal_card

while True:

    while True:
        start = input('Do you want to play a game of Blackjack? Type "y" or "n".: ').lower()
        if start not in {'y', 'n'}:
            print('Unknown action. Please try again.\n')
            continue
        break

    if start == 'n':
        break
    
    player = []
    dealer = []
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    init_game(cards, player, dealer)

    print(f'\nYour hand is {player} = {sum(player)}\n')
    print(f'Dealer hand is {dealer} = {sum(dealer)}')
    
    while sum(player) < 21:
        while True:
            choice = input('\nDo you want to have another card? Type "y" to deal another or "n" to stop.: ').lower()
            if choice not in {'y', 'n'}:
                print('Unknown action. Please try again.\n')
                continue
            break
        if choice == 'y':
            new_card = deal_card(cards)
            if new_card == 11 and sum(player) + new_card > 21:
                new_card = 1
            player.append(new_card)
            print(f'\nYour hand is {player} = {sum(player)}')
        if choice == 'n':
            break

    if sum(player) == 21:
        print('You got 21! Lucky one! Game is over.\n')
        continue    
    elif sum(player) > 21:
        print('\nYou have overdrawn! Better luck next time. Game is over. \n')
        continue

    while sum(dealer) < 21:        
        new_card = deal_card(cards)
        if sum(dealer) + new_card <= 21:
            print(f'\nDealer is taking another card.')
            dealer.append(new_card)
            print(f'Dealer hand is {dealer} = {sum(dealer)}')
        else:
            break

    if sum(dealer) == 21:
        print('Dealer got 21! Better luck next time! Game is over.\n')
        continue

    if sum(player) > sum(dealer):        
        print(f'\nYou have got {sum(player)} points. Dealer has {sum(dealer)}. You win!\n')
        continue
    else:
        print(f'\nYou have got {sum(player)} points. Dealer has {sum(dealer)}. You lose!\n')
        continue
