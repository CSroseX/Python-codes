from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

status= True
while status :
    chosen_drink = input(f"What would you like {menu.get_items()} ? : ").lower()
    if chosen_drink == 'report':
        coffee_maker.report()
        money_machine.report()
    elif chosen_drink == 'off':
        status = False
    else :
        drink = menu.find_drink(chosen_drink)
    if coffee_maker.is_resource_sufficient(drink):
        if money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
