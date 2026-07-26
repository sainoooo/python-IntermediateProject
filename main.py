import menu
Water = 300
Milk = 200
Coffee = 100
Money = 0
def coffeeMachine():
    q = input("What would you like? (espresso/latte/cappuccino): ")
    menuM = menu.MENU
    def drink(q):
        global Money
        global Milk
        global Water
        global Coffee  
        if Water >= menuM[f"{q}"]["ingredients"]["water"] and Coffee >= menuM[f"{q}"]["ingredients"]["coffee"] and Milk >= menuM[f"{q}"]["ingredients"]["milk"]:
            quarter = float(input("How many quarter ?"))
            dimes = float(input("How many dimes ?"))
            nickel = float(input("How many nickel ?"))
            pennies = float(input("How many pennies ?"))
            total = 0.25*quarter + 0.10*dimes + 0.05*nickel + 0.01*pennies

            if total > menuM[f"{q}"]["cost"]:
                change = total - menuM[f"{q}"]["cost"]
                change = round(change,2)
                print(f"Here is ${change} dollars in change")
                Money =+ menuM[f"{q}"]["cost"]
                Water -= menuM[f"{q}"]["ingredients"]["water"]
                Coffee -= menuM[f"{q}"]["ingredients"]["coffee"]
                Milk -= menuM[f"{q}"]["ingredients"]["milk"]
                print(f"Here your {q}! Enjoy!")
                return

            elif total == menuM[f"{q}"]["cost"]:
                Money =+ total
                Water -= menuM[f"{q}"]["ingredients"]["water"]
                Coffee -= menuM[f"{q}"]["ingredients"]["coffee"]
                Milk -= menuM[f"{q}"]["ingredients"]["milk"]
                print(f"Here your {q}! Enjoy!")
                return

            elif total < menuM[f"{q}"]["cost"]:
                print("Sorry! The money it's not enough")
                return
        else:
            print("The resoures are not enogh !")
            return
    if q == "off":
        exit()
    elif q == "report":
        print(f"Water : {Water}ml\nMilk : {Milk}\nCoffee : {Coffee}\nMoney : {Money}")
    elif q == "espresso" or q == "latte" or q == "cappuccino" :
        drink(q = f"{q}")


while True:
    coffeeMachine()
















