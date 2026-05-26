import random
import game_data

score = 0

def print_vs():
    vs_logo = r"""
██╗   ██╗███████╗
██║   ██║██╔════╝
██║   ██║███████╗
╚██╗ ██╔╝╚════██║
 ╚████╔╝ ███████║
  ╚═══╝  ╚══════╝
"""
    print(vs_logo)

def make_pair():
    player_1 = random.choice(game_data.data)
    player_2 = random.choice(game_data.data)
    while player_1 == player_2:
        player_2 = random.choice(game_data.data)

    print(f"Compare A: {player_1['name']}, a {player_1['description']}, from {player_1['country']}\n")
    print_vs()
    print(f"Against B: {player_2['name']}, a {player_2['description']}, from {player_2['country']}\n")

    return player_1, player_2

def check_answer( player_1, player_2, answer ):
    
    global score
    if( answer == 'A'):
        if( player_1['follower_count'] > player_2['follower_count'] ):
            score += 1
            return 1
        else:
            print(f"You're wrong! Current score: {score}\n")
            return 0
    else:
        if( player_2['follower_count'] > player_1['follower_count'] ):
            score += 1
            return 1
        else:
            print(f"You're wrong! Current score: {score}\n")
            return 0


def play_game():

    round_1 = 0
    game_over = 1
    global score
    score = 0

    while game_over == 1:
        if( round_1 == 0 ):
            player_1, player_2 = make_pair()
            round_1 += 1
            answer = input("Who has more followers? Type 'A' or 'B': ").upper()
            game_over = check_answer( player_1, player_2, answer )
        else:
            if( game_over == 1 ):
                print(f"\nYou're right! Current score: {score}\n")
            player_1, player_2 = make_pair()
            answer = input("Who has more followers? Type 'A' or 'B': ").upper()
            game_over = check_answer( player_1, player_2, answer)

            
        



            

    