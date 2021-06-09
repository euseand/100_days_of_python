from exceptions import NotEnoughWater, NotEnoughMilk, NotEnoughCoffee


def insert_coins():
    """Function to retrieve coins and arrange them to the dict"""

    pennies, nickels, dimes, quarters = 0, 0, 0, 0

    while True:
        try:
            pennies = int(input('How many pennies?: '))
            break
        except ValueError:
            print('This is not a valid integer number. Please try again.')
            continue

    while True:
        try:
            nickels = int(input('How many nickels?: '))
            break
        except ValueError:
            print('This is not a valid integer number. Please try again.')
            continue

    while True:
        try:
            dimes = int(input('How many dimes?: '))
            break
        except ValueError:
            print('This is not a valid integer number. Please try again.')
            continue

    while True:
        try:
            quarters = int(input('How many quarters?: '))
            break
        except ValueError:
            print('This is not a valid integer number. Please try again.')
            continue

    coins = {
        'pennies': pennies,
        'nickels': nickels,
        'dimes': dimes,
        'quarters': quarters,
    }

    return coins


def check_resources(machine, drink):
    if machine.water < drink.water:
        raise NotEnoughWater
    elif machine.milk < drink.milk:
        raise NotEnoughMilk
    elif machine.coffee < drink.coffee:
        raise NotEnoughCoffee


def process_request(machine, drink):
    while True:
        print(f'Drink price: {drink.price}')
        print(f'Money inserted: {0}')
        print('Please insert coins.')
        inserted_coins = insert_coins()
        money_inserted = machine.add_money(inserted_coins)
        print(f'Money inserted: {money_inserted}')

        if money_inserted >= drink.price:
            machine.serve_drink(drink)
            print('Here you go.')
            if money_inserted > drink.price:
                change = money_inserted - drink.price
                machine.give_change(change)
                print(f'Take your change: {change}')
            return
        else:
            print('Not enough money. Please insert more coins.')
            continue
