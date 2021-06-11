from random import choice


def deal_card(cards):
    """Return randomly generated card from existing card list"""
    return choice(cards)


def init_game(cards, player, dealer):
    """Deal two initial cards to each player"""
    for _ in range(2):
        player.append(deal_card(cards))
        dealer.append(deal_card(cards))
