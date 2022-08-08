import random

# Deal two cards to computer and player
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

# Calculate the score function

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)


def compare(u_score, c_score):
    if u_score == c_score:
        return "It's a draw!"
    elif c_score == 0:
        return "Blackjack! Computer wins!"
    elif u_score == 0:
        return "Blackjack! You win!"
    elif c_score > 21:
        return "You win!"
    elif u_score > 21:
        return "You lose."
    elif u_score > c_score:
        return "You win!"
    else:
        return "You lose."



user_cards = []
computer_cards = []
is_game_over = False

for card in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

while not is_game_over:

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f" Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")


    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        another_card = input("Do you want to draw another card? y for yes, n for no:  ").lower()
        if another_card == "y":
            user_cards.append(deal_card())
        else:
            is_game_over = True


while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)


print(compare(user_score, computer_score))