from data import MENU
from data import resources

coffee_type = input("What would you like? (espresso, latte, cappuccino):  ").lower()
print("Please insert coins.")

def coffee(amount):
    if amount >= MENU[coffee_type]["cost"]:

        if resources["water"] <= MENU[coffee_type]["ingredients"]["water"] or \
                resources["milk"] <= MENU[coffee_type]["ingredients"]["milk"] or \
                resources["coffee"] <= MENU[coffee_type]["ingredients"]["coffee"]:
            return f"Sorry, there isn't enough supplies to make your {coffee_type}"
        change = amount - MENU[coffee_type]["cost"]
        resources["money"] += MENU[coffee_type]["cost"]
        resources["water"] = resources["water"] - MENU[coffee_type]["ingredients"]["water"]
        resources["milk"] = resources["milk"] - MENU[coffee_type]["ingredients"]["milk"]
        resources["coffee"] = resources["coffee"] - MENU[coffee_type]["ingredients"]["coffee"]
        return f"Here is your change: {round(change, 2)}. Enjoy your {coffee_type}!"
    else:
        return "Sorry. You didn't provide enough money. Here is your refund."

while coffee_type != "off":
    if coffee_type == "report":
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: {resources['money']}")
    else:
        quarters = int(input("How many quarters?:  "))
        dimes = int(input("How many dimes?:  "))
        nickels = int(input("How many nickels?:  "))
        pennies = int(input("How many pennies?:  "))
        total_money = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
        print(coffee(total_money))

    coffee_type = input("What would you like? (espresso, latte, cappuccino):  ").lower()

    if coffee_type == "off":
        import os
        clear = lambda: os.system('cls')
        clear()
    else:
        print("Please insert coins.")
