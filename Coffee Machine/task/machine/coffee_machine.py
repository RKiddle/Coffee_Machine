



# status function
def status():
    print("The coffee machine has:")
    print(f"{water} ml of water")
    print(f"{milk} ml of milk")
    print(f"{coffee} g of coffee beans")
    print(f"{cups} disposable cups")
    print(f"${money} of money")
    return


# buy function
def buy():
    global water
    global milk
    global coffee
    global money
    global cups
    print("What do you want to buy?\n 1 - espresso, 2 - latte, 3 - cappuccino:")
    print("\n or type 'back' to return to the main menu")
    want_buy = input()
    if want_buy == 'back':
        return
    else:
        type_coffee = int(want_buy)
        if type_coffee == 1:
            if water < 250:
                print("Sorry, not enough water!")
                return
            if coffee < 16:
                print("Sorry, not enough coffee!")
                return
            if cups < 1:
                print("Sorry, not enough cups!")
                return
            water -= 250
            coffee -= 16
            money += 4
            cups -= 1
        elif type_coffee == 2:
            if water < 350:
                print("Sorry, not enough water!")
                return
            if coffee < 20:
                print("Sorry, not enough coffee!")
                return
            if milk < 75:
                print("Sorry, not enough milk!")
                return
            if cups < 1:
                print("Sorry, not enough cups!")
                return
            water -= 350
            milk -= 75
            coffee -= 20
            money += 7
            cups -= 1
        elif type_coffee == 3:
            if water < 200:
                print("Sorry, not enough water!")
                return
            if coffee < 12:
                print("Sorry, not enough coffee!")
                return
            if milk < 100:
                print("Sorry, not enough milk!")
                return
            if cups < 1:
                print("Sorry, not enough cups!")
                return
            water -= 200
            milk -= 100
            coffee -= 12
            money += 6
            cups -= 1
    return


#fill function
def fill():
    global water
    global milk
    global coffee
    global money
    global cups
    print("Write how many ml of water you want to add:")
    water += int(input())
    print("Write how many ml of milk you want to add:")
    milk += int(input())
    print("Write how many grams of coffee beans you want to add:")
    coffee += int(input())
    print("Write how many disposable cups you want to add:")
    cups += int(input())
    return


# take function
def take():
    global money
    print(f"I gave you ${money}")
    money = 0
    return

active = True
global water
water = 400
global milk
milk = 540
global coffee
coffee = 120
global cups
cups = 9
global money
money = 550

while active:
    # user's choice
    print("Write action (buy, fill, take, remaining, exit):")
    choice = input()
    if choice == 'buy':
        buy()
    elif choice == 'fill':
        fill()
    elif choice == 'take':
        take()
    elif choice == 'remaining':
        status()
    elif choice == 'exit':
        active = False

