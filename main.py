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
    "water": 1000,
    "milk": 1500,
    "coffee": 500,
}

machine_is_on = True
money = 0

def resource_check(choice, coffee_dictionary):
    global resources

    if choice == "espresso":
        required_milk = 0
    else:
        required_milk = coffee_dictionary['ingredients']['milk']

    if resources['water'] < coffee_dictionary['ingredients']['water']:
        print(f"Sorry, No enough water for {choice}.")
        return False
    elif resources['coffee'] < coffee_dictionary['ingredients']['coffee']:
        print(f"Sorry, No enough coffee for {choice}.")
        return False
    elif resources['milk'] < required_milk:
        print(f"Sorry, No enough milk for {choice}.")
        return False
    else:
        return True


def price_check(choice, coffee_dictionary):
    global money

    print(f"The cost for {choice} is ${coffee_dictionary['cost']}. Please insert Coins.")
    total = float(input("How many pennies?: ")) * 0.01
    total += float(input("How many nickels?: ")) * 0.05
    total += float(input("How many dimes?: ")) * 0.1
    total += float(input("How many quarters?: ")) * 0.25

    print(f"The total amount you have given us for your {choice} is ${round(total, 2)}")

    if total > coffee_dictionary['cost']:
        total = total - coffee_dictionary['cost']
        money += coffee_dictionary['cost']
        print(f"After deducting ${coffee_dictionary['cost']} for your {choice.title()}, here is ${round(total, 2)} in change.")
        return True

    elif total < coffee_dictionary['cost']:
        print(f"Sorry that's not enough money for your {choice.title()}. Money refunded.")
        return False

def make_coffee(choice, coffee_dictionary):

    if choice == "espresso":
        required_milk = 0
    else:
        required_milk = coffee_dictionary['ingredients']['milk']

    resources['water'] = resources['water'] - coffee_dictionary['ingredients']['water']
    resources['coffee'] = resources['coffee'] - coffee_dictionary['ingredients']['coffee']
    resources['milk'] = resources['milk'] - required_milk

    print(f"Please enjoy your {choice.title()}☕.")


while machine_is_on is True:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    coffee_dictionary = {}

    if choice == "off":
        machine_is_on = False

    elif choice == "report":
        print(f"Water: {resources['water']}ml, \nMilk: {resources['milk']}ml, \nCoffee: {resources['coffee']}mg, \nMoney: ${money}")

    else:
        if choice == "espresso":
            coffee_dictionary = MENU['espresso']
        elif choice == "latte":
            coffee_dictionary = MENU['latte']
        elif choice == "cappuccino":
            coffee_dictionary = MENU['cappuccino']

        check = resource_check(choice, coffee_dictionary)

        if check is True:
            amount = price_check(choice, coffee_dictionary)

            if amount is True:
                make_coffee(choice, coffee_dictionary)