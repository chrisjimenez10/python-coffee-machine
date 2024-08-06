from data import MENU, resources


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


