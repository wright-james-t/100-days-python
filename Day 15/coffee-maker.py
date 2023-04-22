# 3 drinks
# resource management (water, milk, coffee)
# coin operated, coin denomination worth
# print report
# check resources are sufficient
import sys

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

coins = {
    "penny": 0.01,
    "nickle": 0.05,
    "dime": 0.10,
    "quarter": 0.25
}

bankRoll = float(0)


def getMoney():
    providedPennies = input("How many pennies would you like to use today? ")
    providedNickles = input("How many nickles would you like to use today? ")
    providedDimes = input("How many dimes would you like to use today? ")
    providedQuarters = input("How many quarters would you like to use today? ")
    try:
        int(providedPennies)
        int(providedNickles)
        int(providedDimes)
        int(providedQuarters)
    except ValueError:
        print("ERROR: Please only use numbers to represent the coins you're paying with.")
        sys.exit(1)
    return providedPennies, providedNickles, providedDimes, providedQuarters


def addMoney(pennies, nickles, dimes, quarters):
    totalPennies = float(pennies) * float(coins["penny"])
    totalNickles = float(nickles) * float(coins["nickle"])
    totalDimes = float(dimes) * float(coins["dime"])
    totalQuarters = float(quarters) * float(coins["quarter"])
    totalMoney = totalPennies + totalNickles + totalDimes + totalQuarters
    totalMoney = "{:.2f}".format(totalMoney)
    return float(totalMoney)


def resourceUpdate(dwink, dwinkIngredients):
    for item in dwinkIngredients:
        resources[item] -= dwinkIngredients[item]


def processTransaction(moneyGiven, drinkCost, drinkChoice):
    if moneyGiven == drinkCost:
        resourceUpdate(drinkChoice, MENU[drinkChoice]['ingredients'])
        print(f"Here is your {drinkChoice} ☕. Thank you!")
    elif moneyGiven > drinkCost:
        changeOwed = moneyGiven - drinkCost
        changeOwed = "{:.2f}".format(changeOwed)
        resourceUpdate(drinkChoice, MENU[drinkChoice]['ingredients'])
        print(
            f"Here is your {drinkChoice} ☕. Your change is {changeOwed}. Thank you!")
    else:
        print("Not enough money inserted.")


def resourceCheck(ingredient_order):
    for item in ingredient_order:
        if ingredient_order[item] >= resources[item]:
            print(f"Sorry, there is not enough {item} to make your drink.")
            return False
    return True


while True:
    drinkChoice = input(
        "What drink would you like today? (Espresso, Latte, or Cappucino): ")
    drinkChoice = drinkChoice.lower()
    if (drinkChoice == 'off'):
        print("Thanks for turning off the machine!")
        break
    elif (drinkChoice == 'report'):
        print(
            f'Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g\nMoney: ${bankRoll}')
    elif (drinkChoice != 'espresso') and (drinkChoice != 'latte') and (drinkChoice != 'cappucino'):
        print(f"{drinkChoice} is not a valid selection.")
    else:
        if not resourceCheck(MENU[drinkChoice]["ingredients"]):
            break
        print(
            f"Great choice! The cost of that drink is: {MENU[drinkChoice]['cost']}")
        drinkCost = float(MENU[drinkChoice]['cost'])
        providedPennies, providedNickles, providedDimes, providedQuarters = getMoney()
        bankRoll += drinkCost
        processTransaction(addMoney(providedPennies, providedNickles,
                           providedDimes, providedQuarters), drinkCost, drinkChoice)