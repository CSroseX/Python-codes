####        COFFEE MACHINE project        ####
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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}



amt_got=0
def process_coins():
    '''Firstly, asks amounts of coins . then calculates the amt_got'''
    print("\nPlease insert coins\n")
    quaters = int(input("How many quaters? : $"))
    dime = int(input("How many dimes? : $"))
    nickles = int(input("How many nikles? : $"))
    pennies = int(input("How many pennies? : $"))

    global amt_got
    amt_got = quaters*0.25 + dime*0.1 + nickles*0.05 + pennies*0.01
    return amt_got

def check_resources(choice):
    '''Checks whether required resources meet available resources, if yes, then prepares, if no, then no'''
    global MENU,resources
    chosen_drink = MENU[choice]['ingredients']
    for ingredients,quantity in chosen_drink.items():
        if resources[ingredients] <quantity:
            print("not enough resources . Apologies . ")
            break
        else:
            print("Resouces available , preparing ...")
            deduct_resources(choice)
            break

def deduct_resources(choice):
    '''Deducts the ingredient quantities from the resources'''
    ingredients = MENU[choice]['ingredients']
    for ingredient, quantity in ingredients.items():
        resources[ingredient] -= quantity


change= 0
def transaction(amt_got,choice):
    '''calculates the change if funds are sufficient otherwise refunds the money'''
    global change,status,profit
    if amt_got >= MENU[choice]['cost']:
        change = amt_got - MENU[choice]['cost']
        profit = MENU[choice]['cost']
        print(f"Here's the change = ${change}")
    else :
        print("Not enough Funds, refunding ...")
        status = False


status = True
while status :
    choice = input("\nWhat would you like ? (espresso $1.5 /latte $2.5 /cappuccino $3.0) : ").lower()
    

    if choice == 'report':  
        print("Resources")
        for item,quantity in resources.items():
            print(f"{item} : {quantity}")
        status  = False

    elif choice =='espresso':
        check_resources(choice)
        amt_got = process_coins()
        change = transaction(amt_got,choice)

    elif choice =='latte':
        check_resources(choice)
        amt_got = process_coins()
        change = transaction(amt_got,choice)

    elif choice =='cappuccino':
        check_resources(choice)
        amt_got = process_coins()
        change = transaction(amt_got,choice)



    #if choice is 'off' , then end the loop
    elif choice == 'off':
        status = False


