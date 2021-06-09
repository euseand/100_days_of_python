from classes import CoffeeDrink, CoffeeMachine
from utils import check_resources, process_request
from exceptions import NotEnoughWater, NotEnoughMilk, NotEnoughCoffee


machine = CoffeeMachine(water=300, milk=200, coffee=100, money=0)
drinks = {
    'espresso': CoffeeDrink(water=50, coffee=18, milk=0, price=2.50),
    'latte': CoffeeDrink(water=200, coffee=24, milk=150, price=3.50),
    'cappuccino': CoffeeDrink(water=250, coffee=24, milk=100, price=3.00),
}

while True:

    while True:
        request = input('What would you like?(espresso/latte/cappuccino/report/exit): ').lower()
        if request not in {'espresso', 'latte', 'cappuccino', 'report', 'exit'}:
            print('\nUnknown action. Please try again.\n')
            continue
        break

    if request == 'report':
        water, milk, coffee, money = machine.report()
        print(f'Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}')
        continue
    elif request == 'exit':
        break
    else:
        drink = drinks[request]

    try:
        check_resources(machine, drink)
    except NotEnoughWater:
        print('Not enough water in machine. Please choose another drink.')
    except NotEnoughMilk:
        print('Not enough milk in machine. Please choose another drink.')
    except NotEnoughCoffee:
        print('Not enough coffee in machine. Please choose another drink.')

    process_request(machine, drink)