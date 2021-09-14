MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0
machine_on = True

def check_resources(drink_ingredients):
    for item in drink_ingredients:
        if drink_ingredients[item] >= resources[item]:
            print(f"Not enough {item}")
            return False
    return True

def coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def good_transaction(payment_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    global profit
    if payment_received >= drink_cost:
        change = round(payment_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        profit += drink_cost
        return True
    else:
        print("Not enough funds")
        return False

def make_drink(drink_name, ingredients):
    """Deduct the required ingredients from the resources."""
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")

while machine_on:
    choice = input("Choose between espresso/latte/cappuccino: ")

    if choice == "off":
        machine_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if check_resources(drink["ingredients"]):
            payment = coins()
            if good_transaction(payment, drink["cost"]):
                make_drink(choice, drink["ingredients"])
