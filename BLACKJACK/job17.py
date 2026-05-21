import header
import game

ind = input("Do you want to play a game of Blackjack? (y/n): ")
while ind.lower() == "y":
    game.play_game()
    ind = input("Game is over! Do you want to play again? (y/n): ")
