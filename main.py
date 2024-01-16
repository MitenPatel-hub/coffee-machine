class CoffeeMachine:
    def __init__(self):
        from menu import Menu
        from coffee_maker import CoffeeMaker
        from money_machine import MoneyMachine
        self.machine_menu = Menu()
        self.coffee_maker = CoffeeMaker()
        self.money_machine = MoneyMachine()
        self.machine_on = True

    def sell_coffee(self):
        while self.machine_on:
            drink_choice = input(f"What would you like? ({self.machine_menu.get_items()}): ").lower()
            if drink_choice == "report":
                self.coffee_maker.report()
                self.money_machine.report()
            elif drink_choice == "off":
                return False
            else:
                drink = self.machine_menu.find_drink(drink_choice)
                if self.coffee_maker.is_resource_sufficient(drink) and self.money_machine.make_payment(drink.cost):
                    self.coffee_maker.make_coffee(drink)


coffee_machine = CoffeeMachine()
coffee_machine.sell_coffee()
