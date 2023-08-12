from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import time

work = True
menu = Menu()
make = CoffeeMaker()
money = MoneyMachine()


def welcome():
    logo = ''' .
                            `:.
                              `:.
                      .:'     ,::
                     .:'      ;:'
                     ::      ;:'
                      :    .:'
                       `.  :.
              _________________________
             : _ _ _ _ _ _ _ _ _ _ _ _ :
         ,---:".".".".".".".".".".".".":
        : ,'"`::.:.:.:.:.:.:.:.:.:.:.::'
        `.`.  `:-===-===-===-===-===-:'
          `.`-._:                   :
            `-.__`.               ,' met.
        ,--------`"`-------------'--------.
         `"--.__                   __.--"'
                `""-------------""'
    '''

    print(logo)
    print("Welcome to hat coffeeshop")
    print(f"Our drinks are: {menu.get_items().strip('/').split('/')}")


def choose():
    global work
    choice = input("What would you like to drink? ").lower()
    if choice == "off":
        work = False
        print("Good bye! Shutting down in 3 seconds...")
        time.sleep(3)
        return
    elif choice == "report":
        make.report()
        print("next action in 5 seconds...")
        time.sleep(5)
        return
    item = menu.find_drink(choice)
    if item in menu.menu:
        if make.is_resource_sufficient(item):
            cost = item.cost
            print(f"the price is {cost}")
            payment_successful = money.make_payment(cost)
            if payment_successful:
                make.make_coffee(item)
                print("next order in 5 seconds...")
                time.sleep(5)
            else:
                time.sleep(3)


while work:
    welcome()
    choose()