# TODO 1  print report of resources.
# TODO 2  Check resouces sufficient to make drink order.
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
is_on = True

def process_coin():
    """Return the total calculated from coins inserted"""
    print("Please insert coins")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def isResourcesSufficient(order) :
    """Return true when order can be made, False if ingredient are insufficient"""
    for item in order:
        if order[item] >= resources[item]:
            print(f"Sorry there is not enough {item} .")
            return False
    return True

def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted or False money is insufficient"""
    if(money_received >= drink_cost):
        change =  round(money_received - drink_cost,2)
        print(f"Here is ${change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money Refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resouces"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}☕")
while is_on:
    choice = input("What Would you like ? (espresso/latte/cappuccino):")
    if choice == 'OFF':
        is_on = False
    elif choice == 'report':
        print(f"Water : {resources['water']}ml")
        print(f"Milk : {resources['milk']}ml")
        print(f"Coffee : {resources['coffee']}76g")
        print(f"Money : ${profit}")

    else:
        drink = MENU[choice]
        if isResourcesSufficient((drink['ingredients'])):
            payment = process_coin()
            if is_transaction_successful(payment,drink['cost']):
                make_coffee(choice,drink['ingredients'])



