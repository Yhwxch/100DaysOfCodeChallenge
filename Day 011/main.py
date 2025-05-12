import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    """Calculates the score. Returns 0 for Blackjack."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    while 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, dealer_score):
    """Compares scores and returns the game result."""
    if user_score > 21:
        return "You went over 21. Dealer wins."
    if dealer_score > 21:
        return "Dealer went over 21. You win!"
    if user_score == dealer_score:
        return f"Draw! Both scored {user_score}."
    if user_score == 0:
        return "Blackjack! You win!"
    if dealer_score == 0:
        return "Dealer has Blackjack. You lose."
    if user_score > dealer_score:
        return f"You win with {user_score} vs dealer's {dealer_score}!"
    else:
        return f"You lose with {user_score} vs dealer's {dealer_score}."

def play_blackjack():
    user_cards = [deal_card(), deal_card()]
    dealer_cards = [deal_card(), deal_card()]
    is_game_over = False

    while not is_game_over:
        user_score = calculate_score(user_cards)
        dealer_score = calculate_score(dealer_cards)

        print(f"\nYour cards: {user_cards}, current score: {user_score}")
        print(f"Dealer's first card: {dealer_cards[0]}")

        if user_score == 0 or dealer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            choice = input("Type 'y' to get another card, 'n' to pass: ").lower()
            if choice == 'y':
                user_cards.append(deal_card())
                clear_screen()
            else:
                is_game_over = True

    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)

    print("\nFinal Results:")
    print(f"Your cards: {user_cards}, final score: {user_score}")
    print(f"Dealer's cards: {dealer_cards}, final score: {dealer_score}")
    print(compare(user_score, dealer_score))

def main():
    while True:
        clear_screen()
        print("🃏 Welcome to Blackjack! 🃏")
        play_blackjack()
        again = input("\nPlay again? Type 'y' to continue, 'n' to quit: ").lower()
        if again != 'y':
            print("Thanks for playing. Goodbye!")
            break

if __name__ == "__main__":
    main()
