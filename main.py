from data import MENU, resources, coins

# Access Price
# print(MENU['espresso']['cost'])

# Access Resources
# print(MENU['espresso']['ingredients'])


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
    return resources


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
        resources['money'] = cost
        print("ENOUGH MONEY PROVIDED")
        return True
    elif total > cost:
        resources['money'] = cost
        print(F"You inserted ${total} and price is {cost}. Here is your change: ${total - cost}")
        return True
    else:
        print(F"{beverage} price is ${cost} and you inserted ${total}. Not enough, money has been refunded...")
        return False


while True:
# User Prompt
    while True:
        user_choice = input("What would you like? (espresso/latte/cappuccino):\n").lower()
        if user_choice != "off" and user_choice != "report" and user_choice != "espresso" and user_choice != "latte" and user_choice != "cappuccino":
            print("Please provide a valid input.")
        else:
            break

    # Turn OFF Coffee Machine
    if user_choice == "off":
        print("TURNING OFF...")
        break
    # Display Report on Resources
    elif user_choice == "report":
        display_resources = resource_amount(resources)
        for key in display_resources:
            if key == 'water' or key == 'milk':
                print(F"{key.title()}: {display_resources[key]}ml")
            if key == 'coffee':
                print(F"{key.title()}: {display_resources[key]}g")
            if key == 'money':
                print(F"{key.title()}: ${display_resources[key]}")
    # Display availability of beverage
    elif user_choice == "espresso":
        if is_available("espresso"):
            reduce_resources("espresso")
            if process_coins("espresso"):
                print("Here is your espresso. Enjoy!")

    elif user_choice == "latte":
        if is_available("latte"):
            reduce_resources("latte")

            print("Here is your latte. Enjoy!")

    elif user_choice == "cappuccino":
        if is_available("cappuccino"):
            reduce_resources("cappuccino")

            print("Here is your cappuccino. Enjoy!")



