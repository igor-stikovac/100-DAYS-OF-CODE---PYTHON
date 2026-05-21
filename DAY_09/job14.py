import os
os.system('cls')
ponude = {
}
print("Welcome to the secret auction program.")
more = "y"
highest_bidder = ""
while more == "y":
    name = input("What is your name?: ")
    bid = int(input("What`s your bid?: "))
    ponude[name] = bid
    more = input("Are there any other bidders? Type `y` or `n`.\n")
    if highest_bidder == "":
        highest_bidder = name
    else:
        if ponude[name] > ponude[highest_bidder]:
            highest_bidder = name
    os.system('cls')

print(f"The winner is {highest_bidder} with a bid of ${ponude[highest_bidder]}.")

    
    