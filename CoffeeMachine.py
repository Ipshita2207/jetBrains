
output = 1
water = 400
milk = 540
beans = 120
cups = 9
money = 550


def coffee_machine(action):
    global water, milk, beans, cups, money
    if action == "buy":
        coffee_type = (input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino,  back - to main menu::"))
        if coffee_type == "back":
            return 1
        else:
            coffee_type = int(coffee_type)
        enough_water = check_water(coffee_type)
        enough_milk = check_milk(coffee_type)
        enough_beans = check_beans(coffee_type)
        
        # Check for enough water, milk, beans and cups
        if (enough_water + enough_milk + enough_beans) == 3 and cups > 0:
            if coffee_type == 1:
                water = water - 250
                beans = beans - 16
                money = money + 4
                cups -= 1
                print("I have enough resources, making you a coffee!")

                return 1
            elif coffee_type == 2:
                water = water - 350
                milk = milk - 75
                beans = beans - 20
                money = money + 7
                cups -= 1
                print("I have enough resources, making you a coffee!")
                #print()
                return 1
            else:
                water = water - 200
                milk = milk - 100
                beans = beans - 12
                money = money + 6
                cups -= 1
                print("I have enough resources, making you a coffee!")
                #print()
                return 1

        elif not enough_water:
            print("Sorry, not enough water!")
            return 1
        elif not enough_milk:
            print("Sorry, not enough milk!")
            return 1
        elif not enough_beans:
            print("Sorry, not enough coffee beans!")
            return 1
        elif cups == 0:
            print("Sorry, not enough cups!")
            return 1

    elif action == "fill":
        add_water = int(input("Write how many ml of water do you want to add:"))
        water += add_water
        add_milk = int(input("Write how many ml of milk do you want to add:"))
        milk += add_milk
        add_beans = int(input("Write how many grams of coffee beans do you want to add:"))
        beans += add_beans
        add_cups = int(input("Write how many disposable cups of coffee do you want to add:"))
        cups += add_cups
        return 1
    elif action == "take":
        print(f"I gave you ${money}")
        #print()
        money = 0
        return 1

    elif action == "remaining":
        print(f'''The coffee machine has:
                    {water} of water
                    {milk} of milk
                    {beans} of coffee beans
                    {cups} of disposable cups
                    ${money} of money''')
        return 1

    else:
        return 0

def check_water(coffee_type):
    if coffee_type == 1:
        if water >=250:
            return 1
        else:
            return 0
    elif coffee_type == 2:
        if water >=350:
            return 1
        else:
            return 0
    elif coffee_type == 3:
        if water >=200:
            return 1
        else:
            return 0
def check_milk(coffee_type):
    if coffee_type == 2:
        if milk >= 75:
            return 1
        else:
            return 0
    elif coffee_type == 3:
        if milk >= 100:
            return 1
        else:
            return 0
    else:
        return 1

def check_beans(coffee_type):
    if coffee_type == 1:
        if beans >= 16:
            return 1
        else:
            return 0
    elif coffee_type == 2:
        if beans >= 20:
            return 1
        else:
            return 0
    elif coffee_type == 3:
        if beans >= 12:
            return 1
        else:
            return 0

while output != 0:
    print()
    choice = input("Write action (buy, fill, take, remaining, exit):")
    output = coffee_machine(choice)