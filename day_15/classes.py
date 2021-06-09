class CoffeeDrink:
    """Class represents a coffee drink"""

    def __init__(self, water, milk, coffee, price):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.price = price


class CoffeeMachine:
    """Class represents a coffee machine"""

    def __init__(self, water, milk, coffee, money):
        self.coffee = coffee
        self.water = water
        self.milk = milk
        self.money = money

    def report(self):
        return self.water, self.milk, self.coffee, self.money

    def add_money(self, coins):
        coins_to_values = {
            'pennies': 0.01,
            'nickels': 0.05,
            'dimes': 0.1,
            'quarters': 0.25,
        }
        value = sum([coins_to_values[key] * value for key, value in coins.items()])
        self.money += value
        return value

    def serve_drink(self, drink):
        self.water -= drink.water
        self.milk -= drink.milk
        self.coffee -= drink.coffee

    def give_change(self, amount):
        self.money -= amount
