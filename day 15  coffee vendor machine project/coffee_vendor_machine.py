from art import logo
import os
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
    "water": 0,
    "milk": 0,
    "coffee": 0,
    "money" : 0,
}

def check_resources(menu, resources):
    global no_resource
    if prompt == "latte" or prompt == "cappuccino": 
        if resources["water"] < menu["ingredients"]["water"] and resources["milk"] < menu["ingredients"]["milk"] and resources["coffee"] < menu["ingredients"]["coffee"]:
            print("Sorry there is not enough water,milk and coffee.​")
            no_resource = True
        elif resources["water"] < menu["ingredients"]["water"] and resources["milk"] < menu["ingredients"]["milk"]:
            print("Sorry there is not enough water and milk.​")
            no_resource = True
        elif resources["water"] < menu["ingredients"]["water"] and resources["coffee"] < menu["ingredients"]["coffee"]:
            print("Sorry there is not enough water and coffee.​")
            no_resource = True
        elif resources["milk"] < menu["ingredients"]["milk"] and resources["coffee"] < menu["ingredients"]["coffee"]:
            print("Sorry there is not enough milk and cofee.")
            no_resource = True
        elif resources["water"] < menu["ingredients"]["water"]:
            print("Sorry there is not enough water.")
            no_resource = True
        elif resources["milk"] < menu["ingredients"]["milk"]:
            print("Sorry there is not enough milk.")
            no_resource = True
        elif resources["coffee"] < menu["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee​")
            no_resource = True
        else:
            print(f"There is enought resources to make {prompt} and the cost is ",menu["cost"])
    elif prompt == "espresso":
        if resources["water"] < menu["ingredients"]["water"] and resources["coffee"] < menu["ingredients"]["coffee"]:
            print("Sorry there is not enough water and coffee.")
            no_resource = True
        elif resources["water"] < menu["ingredients"]["water"]:
            print("Sorry there is not enough water.")
            no_resource = True
        elif resources["coffee"] < menu["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee.")
            no_resource = True
        else:
            print(f"There is enought resources to make {prompt} and the cost is ",menu["cost"])



def get_report(prompt,resources):
    global no_resource
    if prompt == "report":
        print("Water : ",resources["water"],"ml")
        print("Milk : ",resources["milk"],"ml")
        print("Coffee : ",resources["coffee"],"ml")
        print("Money :$",resources["money"])
    sufficent_resource = input("Is there is enought resource to make coffee 'yes or 'no': ").lower()
    if sufficent_resource == 'no':
        no_resource = True
    else:
        no_resource = False




def calculate_amount(one, two, five, ten, cost):
    amount = (one * 1) + (two * 2) + (five * 5) + (ten * 10)
    balance = amount - cost
    return balance, amount



def check_transaction_withoutchange(given, cost, transaction1):
    if given == cost:
        transaction1 = True
        return transaction1
    else:
        return False


def check_transaction_withchange(given, cost, transaction2):
    if given > cost:
        transaction2 = True
        return transaction2
    else:
        return False


def check_transaction_fail(given, cost, transaction3):
    if given < cost:
        transaction3 = True
        return transaction3
    else:
        return False

no_resource = False
get_coffee = True
machine_off = False
while machine_off == False:
    while get_coffee == True:
        print(logo)
        prompt = input("What would you like? (espresso/latte/cappuccino) or Type report to check resource:").lower()
        os.system('clear')
        print(logo)
        if prompt != 'report':
            check_resources(menu[prompt], resources)
        else:
            get_report(prompt,resources)
        if no_resource == True:
            break
        else:
            if prompt != 'espresso':
              if prompt != 'latte':
                if prompt != 'cappuccino':
                    prompt = input("What would you like? (espresso/latte/cappuccino):").lower()
                    os.system('clear')
                    print(logo)
                    if prompt != 'report':
                        check_resources(menu[prompt], resources)
                    else:
                        get_report(prompt,resources)
        if no_resource == True:
            break
        print("please insert coins.")

        one_ruppe = int(input("How many one ruppees?: "))
        two_ruppe = int(input("How many two ruppees?: "))
        five_ruppe = int(input("How many five ruppees?: "))
        ten_ruppe = int(input("How many ten ruppees?: "))

        coin_calculation = calculate_amount(one_ruppe, two_ruppe, five_ruppe, ten_ruppe, menu[prompt]["cost"])
        money = coin_calculation[1]
        balance = coin_calculation[0]
        transaction_success_withoutchange = False
        transaction_success_withchange = False
        transaction_fail = False

        transaction_success_withoutchange = check_transaction_withoutchange(money, menu[prompt]["cost"], transaction_success_withoutchange)

        transaction_success_withchange = check_transaction_withchange(money, menu[prompt]["cost"], transaction_success_withchange)

        transaction_fail = check_transaction_fail(money, menu[prompt]["cost"], transaction_fail)
        if transaction_success_withchange == True:
            print(f"Transaction Successfull With change {balance} to return")
            if prompt == "espresso":
                resources = {
                    "water" : resources["water"] - menu[prompt]["ingredients"]["water"],
                    "milk" : resources["milk"],
                    "coffee" : resources["coffee"] - menu[prompt]["ingredients"]["coffee"],
                    "money" : resources["money"] + (money - balance) ,
                }
                print("Here is your espresoo. Enjoy!")
            elif prompt == "latte":
                resources = {
                    "water" : resources["water"] - menu[prompt]["ingredients"]["water"],
                    "milk" : resources["milk"] - menu[prompt]["ingredients"]["milk"],
                    "coffee" : resources["coffee"] - menu[prompt]["ingredients"]["coffee"],
                    "money" : resources["money"] + (money - balance) ,
                }
                print("Here is your Lattee. Enjoy!")
            elif prompt == "cappuccino":
                resources = {
                    "water" : resources["water"] - menu[prompt]["ingredients"]["water"],
                    "milk" : resources["milk"] - menu[prompt]["ingredients"]["milk"],
                    "coffee" : resources["coffee"] - menu[prompt]["ingredients"]["coffee"],
                    "money" : resources["money"] + (money - balance) ,
                }
                print("Here is your cappuccino. Enjoy!")
            
        elif transaction_success_withoutchange == True: 
            print("Transaction Successfull,With No change to return")
            if prompt == "espresso":
                print(prompt)
                resources = {
                    "water" : resources["water"] - menu[prompt]["ingredients"]["water"],
                    "milk" : resources["milk"],
                    "coffee" : resources["coffee"] - menu[prompt]["ingredients"]["coffee"],
                    "money" : resources["money"] + money,
                }
                print("Here is your espresoo. Enjoy!")
            elif prompt == "latte":
                resources = {
                    "water" : resources["water"] - menu[prompt]["ingredients"]["water"],
                    "milk" : resources["milk"] - menu[prompt]["ingredients"]["milk"],
                    "coffee" : resources["coffee"] - menu[prompt]["ingredients"]["coffee"],
                    "money" : resources["money"] + money,
                }
                print("Here is your Lattee. Enjoy!")
            elif prompt == "cappuccino":
                resources = {
                    "water" : resources["water"] - menu[prompt]["ingredients"]["water"],
                    "milk" : resources["milk"] - menu[prompt]["ingredients"]["milk"],
                    "coffee" : resources["coffee"] - menu[prompt]["ingredients"]["coffee"],
                    "money" :resources["money"] + money,
                }
                print("Here is your Lattee. Enjoy!")
        else:
            print("Sorry that's not enough money. Money refunded")
            break
    if no_resource == True:
        fill_resource = input("Do you wish to fill resource 'Yes' Or 'No': ").lower()
        bank = resources["money"]
        while fill_resource == "yes":
            resources["water"] = resources["water"] + int(input("Please fill the water,your machine can hold maximum of 800 ml: "))
            resources["milk"] = resources["milk"] + int(input("Please fill the milk,your machine can hold maximum of 700 ml: "))
            resources["coffee"] = resources["coffee"] + int(input("Please fill the coffee powder, powder box capacity is maximum of 500 g: "))
            print(f"Do You wish to collect saved money Rs {bank} ")
            choice = input("Do you wish to collect money 'yes' or 'no: ").lower()
            if choice == 'yes':
                money_collection = int(input(f"if yes enter the amount you wish to collect, '0' to collect all amount left: "))
                if money_collection == 0:
                    resources["money"] = 0
                else:
                    resources["money"] = bank - money_collection
            else:
                resources["money"] = bank
            os.system('clear')

            get_coffee = True
            no_resource = False
            fill_resource = "stop"

