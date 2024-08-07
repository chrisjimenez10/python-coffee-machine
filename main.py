from data import resources
from tools import resource_amount, is_available, reduce_resources, process_coins, clear_console


def coffee_machine():
    """The coffee_machine() function initiates the program to purchase coffee beverages"""
    while True:

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

        # Logic for dispensing beverage selected by user
        elif user_choice == "espresso":
            if is_available("espresso"):
                if process_coins("espresso"):
                    reduce_resources("espresso")
                    print("Here is your espresso. Enjoy!")

        elif user_choice == "latte":
            if is_available("latte"):
                if process_coins("latte"):
                    reduce_resources("latte")
                    print("Here is your latte. Enjoy!")

        elif user_choice == "cappuccino":
            if is_available("cappuccino"):
                if process_coins("cappuccino"):
                    reduce_resources("cappuccino")
                    print("Here is your cappuccino. Enjoy!")


coffee_machine()