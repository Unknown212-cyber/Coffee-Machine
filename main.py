MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

resources['money'] = 0

coffee_off = False

quarters = 0.25
dimes = 0.10
nickles = 0.05
pennies = 0.01


def secret_code(coffee_se):
    global coffee_off
    if coffee_se == 'off':
        coffee_off = True
    elif coffee_se == 'report':
        for items in resources:
            if items == 'water':
                print(f"{items}: {resources[items]}ml")
            elif items == 'milk':
                print(f"{items}: {resources[items]}ml")
            elif items == 'coffee':
                print(f"{items}: {resources[items]}g")
            elif items == 'money':
                print(f"{items}: ${resources[items]}")


def check_drink(drink, menu, res):
    if drink == 'espresso':
        for ingre in resources:
            if ingre == 'water':
                if menu[drink]["ingredients"]["water"] > res[ingre]:
                    return "Sorry there is not enough water."
            elif ingre == 'coffee':
                if menu[drink]["ingredients"]["coffee"] > res[ingre]:
                    return "Sorry there is not enough coffee."
    elif drink == 'latte':
        for ingre in resources:
            if ingre == 'water':
                if menu[drink]["ingredients"]["water"] > res[ingre]:
                    return "Sorry there is not enough water."
            elif ingre == 'milk':
                if menu[drink]["ingredients"]["milk"] > res[ingre]:
                    return "Sorry there is not enough milk."
            elif ingre == 'coffee':
                if menu[drink]["ingredients"]["coffee"] > res[ingre]:
                    return "Sorry there is not enough coffee."
    elif drink == 'cappuccino':
        for ingre in resources:
            if ingre == 'water':
                if menu[drink]["ingredients"]["water"] > res[ingre]:
                    return "Sorry there is not enough water."
            elif ingre == 'milk':
                if menu[drink]["ingredients"]["milk"] > res[ingre]:
                    return "Sorry there is not enough milk."
            elif ingre == 'coffee':
                if menu[drink]["ingredients"]["coffee"] > res[ingre]:
                    return "Sorry there is not enough coffee."
    return 'Ok'


def process_coins(drink, qu, di, ni, pe, menu):
    print("Please insert coins.")
    q = int(input("how many quarters?: "))
    d = int(input("how many dimes?: "))
    n = int(input("how many nickles?: "))
    p = int(input("how many pennies?:"))

    money = (qu*q) + (di*d) + (ni*n) + (pe*p)

    if menu[drink]['cost'] > money:
        return "Sorry that's not enough money. Money refunded."
    elif menu[drink]['cost'] < money:
        change = money - menu[drink]['cost']
        change = "{:.2f}".format(change)
        resources['money'] += menu[drink]['cost']
        return f"Here is ${change} dollars in change."


def make_coffee(drink, menu, res):
    res_water = res['water']
    res_milk = res['milk']
    res_coffee = res['coffee']

    if drink == 'espresso':
        coffee_water = menu[drink]['ingredients']['water']
        coffee_coffee = menu[drink]['ingredients']['coffee']
        res['water'] = res_water - coffee_water
        res['coffee'] = res_coffee - coffee_coffee
    else:
        coffee_water = menu[drink]['ingredients']['water']
        coffee_milk = menu[drink]['ingredients']['milk']
        coffee_coffee = menu[drink]['ingredients']['coffee']
        res['water'] = res_water - coffee_water
        res['milk'] = res_milk - coffee_milk
        res['coffee'] = res_coffee - coffee_coffee

    return f"Here is your {drink}. Enjoy!"


while not coffee_off:
    coffee = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if coffee == 'report' or coffee == 'off':
        secret_code(coffee)
        continue

    if check_drink(coffee, MENU, resources) != 'Ok':
        print(check_drink(coffee, MENU, resources))
        continue

    coins = process_coins(coffee, quarters, dimes, nickles, pennies, MENU)
    print(coins)
    if coins == "Sorry that's not enough money. Money refunded.":
        continue

    print(make_coffee(coffee, MENU, resources))