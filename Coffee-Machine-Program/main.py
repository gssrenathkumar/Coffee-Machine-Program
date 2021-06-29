from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
while True:
    choice = input("What would you like? (latte/espresso/cappuccino/):")

    if choice == "report":
        coffee_maker.report()
    elif choice == "off":
        print("Turning Off....")
        break
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) is True:
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)



