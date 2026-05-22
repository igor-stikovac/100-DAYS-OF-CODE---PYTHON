import random
import os

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def play_game():
    
    game_over = "y"

    while game_over == "y":
        diff = header()
        number = random.randint(1,101)

        if(diff == "e"):
            checking_num(number,EASY_LEVEL_TURNS)
        elif(diff == "h"):
            checking_num(number,HARD_LEVEL_TURNS)
        else:
            print("Difficuly doesn't exist!")

        game_over = input("Do you want to plat another game? ('y'/'n'): ").lower()
        
        
def header():
    os.system('cls')
    print("Welcomt to the Number Guessing Game!\n")
    print("I'm thinking of a number between 1 and 100.\n")
    diff = input("Choose difficulty. Type 'e' (for easy) or 'hard' (for hard): ").lower()

    return diff    
    
def checking_num(number,diff):

    game_over = 1

    for i in range(diff,0,-1):
        print(f"You have {i} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if( guess > number ):
            print("Too high.\nGuess again.")
        elif( guess < number ):
            print("Too low.\nGuess again.")
        else:
            game_over = 0
            print(f"You got it. Congratulations, the answer was {guess}")
            break

    if game_over == 1:
        print("You are out of guesses, better luck next time!\n")
        
    
        
    






