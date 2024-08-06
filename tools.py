from data import MENU, resources
import os


def clear_console():
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")


def resource_amount(d):
    """The resource_amount() function iterates over dictionary provided as argument and returns key-value pair"""
    total_amount = {}
    for key in d:
        total_amount[key] = d[key]
    return total_amount


def is_available(beverage):
    """The is_available() function checks if beverage can be purchased based on availability of resources. Returns Bool"""
    water = 0
    milk = 0
    coffee = 0

    for key in MENU[beverage]['ingredients']:
        if key == "water":
            water += MENU[beverage]['ingredients']['water']
        if key == "milk":
            milk += MENU[beverage]['ingredients']['milk']
        if key == "coffee":
            coffee += MENU[beverage]['ingredients']['coffee']

    if resources['water'] >= water and resources['milk'] >= milk and resources['coffee'] >= coffee:
        return True
    else:
        if resources['water'] < water:
            print("Sorry, there is not enough water.")
        if resources['milk'] < milk:
            print("Sorry, there is not enough milk.")
        if resources['coffee'] < coffee:
            print("Sorry, there is not enough coffee.")
        return False


def reduce_resources(beverage):
    resources['water'] -= MENU[beverage]['ingredients']['water']
    resources['milk'] -= MENU[beverage]['ingredients']['milk']
    resources['coffee'] -= MENU[beverage]['ingredients']['coffee']


def process_coins(beverage):
    quarters = input("How many quarters?: ")
    try:
        quarters = int(quarters)
        quarters *= 0.25
    except ValueError:
        print("Please provide a valid number")

    dimes = input("How many dimes?: ")
    try:
        dimes = int(dimes)
        dimes *= 0.10
    except ValueError:
        print("Please provide a valid number")

    nickles = input("How many nickles?: ")
    try:
        nickles = int(nickles)
        nickles *= 0.05
    except ValueError:
        print("Please provide a valid number")

    pennies = input("How many pennies?: ")
    try:
        pennies = int(pennies)
        pennies *= 0.01
    except ValueError:
        print("Please provide a valid number")

    total = round((quarters + dimes + nickles + pennies), 2)
    print(total)
    cost = round((MENU[beverage]['cost']), 2)
    print(cost)
    if total == cost:
        resources['money'] += cost
        return True
    elif total > cost:
        resources['money'] += cost
        print(F"You inserted ${total} and price is ${cost}. Returning change: ${round((total - cost), 2)}")
        return True
    else:
        print(F"{beverage} price is ${cost} and you inserted ${total}. Not enough, money has been refunded...")
        return False