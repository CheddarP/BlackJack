import random
from art import logo

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(hand):
    if sum(hand) == 21 and len(hand) == 2:
        return 0
    if sum(hand) > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)
    return sum(hand)

def compare(user_score, computer_score):
    if computer_score == user_score:
        return "It's a Draw :|\n"
    elif computer_score == 0:
        return "Cpu Wins!\n"
    elif user_score == 0:
        return "You win!!!\n"
    elif user_score > 21:
        return "You went over. You lose!\n"
    elif computer_score > 21:
        return "Cpu went over. You Win!!!\n"
    elif user_score > computer_score:
        return "You Win!!!\n"
    else:
        return "You lose\n"

def play_game():
    print(logo)

    game_over = False
    your_cards = []
    cpu_cards = []
    your_score = 0
    cpu_score = 0

    for i in range(2):
        your_cards.append(deal_card())
        cpu_cards.append(deal_card())

    your_score = calculate_score(your_cards)
    cpu_score = calculate_score(cpu_cards)

    print(f"\nYour cards {your_cards}, current score: {calculate_score(your_cards)}")
    print(f"Computer's first card: {cpu_cards[0]}")

    while not game_over:

        if your_score == 0 or cpu_score == 0 or your_score > 21:
            game_over = True
            your_score = calculate_score(your_cards)

        else:
            next_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if next_card == 'y':
                your_cards.append(deal_card())
                your_score = calculate_score(your_cards)
                print(f"Your cards {your_cards}, current score: {calculate_score(your_cards)}")
                print(f"Computer's first card: {cpu_cards[0]}")

            else:
                game_over = True

    while cpu_score != 0 and cpu_score < 17:
        cpu_cards.append(deal_card())
        cpu_score = calculate_score(cpu_cards)

    print(f"Your final hand: {your_cards}, final score: {calculate_score(your_cards)}")
    print(f"Computer's final hand: {cpu_cards}, final score: {calculate_score(cpu_cards)}")
    print(compare(your_score, cpu_score))

while input("Do you want to play a game of BlackJack? Type 'y' or 'n': ").lower() == 'y':
    play_game()

print("Come back next time for some more fun! :)")