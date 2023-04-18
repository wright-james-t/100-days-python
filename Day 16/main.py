from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
machine = CoffeeMaker()
money = MoneyMachine()

while True:
    drinkChoice = input(f'What drink would you like? {menu.get_items()}: ')
    if(drinkChoice == 'off'):
        print(f"Thank you for turning off the machine!")
        break
    elif(drinkChoice == 'report'):
        machine.report()
        money.report()
    else:
        if(machine.is_resource_sufficient(menu.find_drink(drinkChoice))) and (money.make_payment(menu.find_drink(drinkChoice).cost)):
            machine.make_coffee(menu.find_drink(drinkChoice))