from random import choice


def deal_card(cards):
    return choice(cards) 

def init_game(cards, player, dealer):

    player.append(deal_card(cards))
    player.append(deal_card(cards))
    
    dealer.append(deal_card(cards))
    dealer.append(deal_card(cards))
