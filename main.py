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

    if resources['water'] > water and resources['milk'] > milk and resources['coffee'] > coffee:
        return True
    else:
        return False


def reduce_resources(beverage):
    resources['water'] -= MENU[beverage]['ingredients']['water']
    resources['milk'] -= MENU[beverage]['ingredients']['milk']
    resources['coffee'] -= MENU[beverage]['ingredients']['coffee']
    return resources

# User Prompt
user_choice = input("What would you like? (espresso/latte/cappuccino):\n").lower()

# Turn OFF Coffee Machine
if user_choice == "off":
    print("TURNING OFF...")
# Display Report on Resources
elif user_choice == "report":
    display_resources = resource_amount(resources)
    for key in display_resources:
        if key == 'water' or key == 'milk':
            print(F"{key.title()}: {display_resources[key]}ml")
        if key == 'coffee':
            print(F"{key.title()}: {display_resources[key]}g")
# Display availability of beverage
elif user_choice == "espresso":
    if is_available("espresso"):
        print(reduce_resources("espresso"))
    else:
        print("NOT ENOUGH RESOURCES")
elif user_choice == "latte":
    if is_available("latte"):
        print(reduce_resources("latte"))
    else:
        print("NOT ENOUGH RESOURCES")
elif user_choice == "cappuccino":
    if is_available("cappuccino"):
        print(reduce_resources("cappuccino"))
    else:
        print("NOT ENOUGH RESOURCES")


