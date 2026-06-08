import coffee
import os
os.system('cls')

def is_res_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > coffee.recources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True
    
def process_coins():
    print("Please insert coins.")
    total  = float( input ( "How many quarters?: ")) * 0.25
    total += float( input ( "How many dimes?:    ")) * 0.1
    total += float( input ( "How many nickles?:  ")) * 0.05 
    total += float( input ( "How many pennies?:  ")) * 0.01

    return total

def is_transaction_successful( money_received, drink_cost ):
    
    if money_received >= drink_cost:
        change = round( money_received - drink_cost, 2 )
        print(f"Here is ${change} in change." )
        coffee.profit += drink_cost
        return True
    else:
        print("Sorry that1s not enough money. Money refunded." )
        return False

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        coffee.recources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")

def main():

    is_on = True

    print("COFFE SHOP")
    while is_on:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        print(choice)
        if choice == "off":
            is_on = False
        elif choice == "report":
            print(f" {coffee.recources['water']}")            
            print(f" {coffee.recources['milk']}")
            print(f" {coffee.recources['coffee']}")            
            print(f"Money: {coffee.profit}")            
        else:
            drink = coffee.coffee_types[choice]
            print(drink)
            if is_res_sufficient(drink["ingredients"]):
                payment = process_coins()
                if( is_transaction_successful( payment, drink["price"] ) ):
                    make_coffee( choice, drink["ingredients"] )




            