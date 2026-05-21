import cards_f

MAX_VALUE = 21

def player_turn(player_cards,dealer_cards,deck):

    while True:
        player_score = calculate_score(player_cards)
        print_both(player_cards,dealer_cards)

        if player_score > MAX_VALUE:
            print("You are busted. You lost!")
            return player_score

        ind = input("Do you want to draw another card?(y/n):  ").lower()
        if ind != "y":
            return player_score
        
        cards_f.draw_card(player_cards,deck)

def dealer_turn(dealer_cards,player_cards,deck):
    cards_f.draw_card(dealer_cards,deck)
    dealer_score = calculate_score(dealer_cards)
    print_both(player_cards,dealer_cards)
    
    while dealer_score < 17:
        print("Dealer must draw another card!\n")
        cards_f.draw_card(dealer_cards,deck)
        dealer_score = calculate_score(dealer_cards)
        print_both(player_cards,dealer_cards)

    return dealer_score

def play_game():
    deck = cards_f.create_deck()
    player_cards = {}
    dealer_cards = {}

    for i in range(2):
        cards_f.draw_card(player_cards,deck)
    cards_f.draw_card(dealer_cards,deck)

    player_score = player_turn(player_cards,dealer_cards,deck)
    
    if player_score <= MAX_VALUE:
        dealer_score = dealer_turn(dealer_cards,player_cards,deck)
        chech_winner(player_score,dealer_score)

def calculate_score(hand):
    score = 0
    for card in hand.values():
        score += card["value"]

    if score > MAX_VALUE:
        for card in hand.values():
            if card["value"] == 11:
                card["value"] = 1
                score -= 10
                break
                
    return score 

def chech_winner(player_score,dealer_score):
    if dealer_score > MAX_VALUE:
        print("Congratulations! You've won, dealer is busted!\n")
    elif player_score > dealer_score:
        print("Congratulations! You won!\n")
    elif player_score == dealer_score:
        print("It's draw!\n")
    else:
        print("You lost!\n")


def print_inline(cards):
    linije_karata = [karta["picture"].splitlines() for karta in cards.values()]

    for i in range(len(linije_karata[0])):
        for karta in linije_karata:
            print(karta[i], end="   ")
        print()

def print_both(player,dealer):
    print_inline(player)
    print_inline(dealer)

