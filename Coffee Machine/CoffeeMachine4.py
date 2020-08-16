# Write your code here
water = 400
milk = 540
coffee_beans = 120
cups = 9
money = 550
disposable_cups = 9
print('''The coffee machine has:
400 of water
540 of milk
120 of coffee beans
9 of disposable cups
550 of money''')
print()
option = input("Write action (buy, fill, take):")

if option == "buy":
    coffee_type = int(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:"))
    if coffee_type == 1:
        water = water - 250
        coffee_beans = coffee_beans - 16
        money = money + 4
        disposable_cups -= 1
    elif coffee_type == 2:
        water = water - 350
        milk = milk - 75
        coffee_beans = coffee_beans - 20
        money = money + 7
        disposable_cups -= 1
    else:
        water = water - 200
        milk = milk - 100
        coffee_beans = coffee_beans - 12
        money = money + 6
        disposable_cups -= 1
    print("The coffee machine has:\n", water,
          "of water\n", milk,
          "of milk\n", coffee_beans,
          "of coffee beans\n", disposable_cups,
          "of disposable cups\n", money,
          "of money")


elif option == "fill":
    add_water = int(input("Write how many ml of water do you want to add:"))
    water += add_water
    add_milk = int(input("Write how many ml of milk do you want to add:"))
    milk += add_milk
    add_coffee_beans = int(input("Write how many grams of coffee beans do you want to add:"))
    coffee_beans += add_coffee_beans
    add_cups = int(input("Write how many disposable cups of coffee do you want to add:"))
    disposable_cups += add_cups
    print(f'''The coffee machine has:
    {water} of water
    {milk} of milk
    {coffee_beans} of coffee beans
    {disposable_cups} of disposable cups
    {money} of money''')


else:
    print(f"I gave you ${money}")
    print()
    money = 0
    print("""The coffee machine has:
    {} of water
    {} of milk
    {} of coffee beans
    {} disposable cups
    {} of money
    """.format(water, milk, coffee_beans, disposable_cups, money))