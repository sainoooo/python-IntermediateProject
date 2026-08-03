import money_machine
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
is_on = True
while is_on:
    q = input("hi! what do you need today? espresso,latte,cappuccino:  ")
    if q == "report":
        CoffeeMaker().report()
        MoneyMachine().report()
    elif q == "espresso" or q == "latte" or q == "cappuccino":
        drink = Menu().find_drink(q)
        if CoffeeMaker().is_resource_sufficient(drink):
            if MoneyMachine().make_payment(drink.cost):
                CoffeeMaker().make_coffee(drink)
    else:
        is_on = False






