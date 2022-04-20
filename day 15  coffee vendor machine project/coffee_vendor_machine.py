menu = {
    "espresso": {"ingredients": {"water": 50,"coffee": 18,},"cost": 10,},
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 30,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 50,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def check_resources(menu, resources):
    if prompt == "latte" or prompt == "cappuccino": 
        if resources["water"] < menu["ingredients"]["water"] and resources["milk"] < menu["ingredients"]["milk"] and resources["coffee"] < menu["ingredients"]["coffee"]:
            print("Sorry there is not enough water,milk and coffee.​")
        elif resources["water"] < menu["ingredients"]["water"] and resources["milk"] < menu["ingredients"]["milk"]:
            print("Sorry there is not enough water and milk.​")
        elif resources["water"] < menu["ingredients"]["water"] and resources["coffee"] < menu["ingredients"]["coffee"]:
            print("Sorry there is not enough water and coffee.​")
        elif resources["milk"] < menu["ingredients"]["milk"] and resources["coffee"] < menu["ingredients"]["coffee"]:
            print("Sorry there is not enough milk and cofee.​")
        elif resources["water"] < menu["ingredients"]["water"]:
            print("Sorry there is not enough water.​")
        elif resources["milk"] < menu["ingredients"]["milk"]:
            print("Sorry there is not enough milk.​")
        elif resources["coffee"] < menu["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee.​")
        else:
            print(f"There is enought resources to make {prompt} and the cost is ",menu["cost"])
        
    elif prompt == "espresso":
        if resources["water"] < menu["ingredients"]["water"] and resources["coffee"] < menu["ingredients"]["coffee"]:
            print("Sorry there is not enough water and coffee.​")
        elif resources["water"] < menu["ingredients"]["water"]:
            print("Sorry there is not enough water.​")
        elif resources["coffee"] < menu["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee.​")
        else:
            print(f"There is enought resources to make {prompt}")



def get_report(prompt,resources,money):
        if prompt == "report":
            print("Water : ",resources["water"],"ml")
            print("Milk : ",resources["milk"],"ml")
            print("Coffee : ",resources["coffee"],"ml")
            print("Money :$",money)


def calculate_amount(one, two, five, ten, cost):
    amount = (one * 1) + (two * 2) + (five * 5) + (ten * 10)
    balance = amount - cost
    return balance, amount

def check_transaction(given, balance ,cost):
    if given == cost:
        print("money matched no change")
    elif given > cost:
        print(f"Money is extra , take {balance} change ")
    else:
        print("Sorry that's not enough money. Money refunded")

money = 0

prompt = input("What would you like? (espresso/latte/cappuccino):").lower()
check_resources(menu[prompt], resources)
get_report(prompt,resources,money)

print("please insert coins.")

one_ruppe = int(input("How many one ruppees?: "))
two_ruppe = int(input("How many two ruppees?: "))
five_ruppe = int(input("How many five ruppees?: "))
ten_ruppe = int(input("How many ten ruppees?: "))

coin_calculation = calculate_amount(one_ruppe, two_ruppe, five_ruppe, ten_ruppe, menu[prompt]["cost"])
money = coin_calculation[1]
balance = coin_calculation[0]

check_transaction(money, balance, menu[prompt]["cost"])