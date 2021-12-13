import menu
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
# print(coffee_maker.report())
# coffee_maker.report()
money_machine = MoneyMachine()
# print(money_machine.report())

menuitem = MenuItem("latte", 200, 300, 100, 1.5)
is_no = True
while is_no:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        print("Machine is shut down.")
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        print(drink)
