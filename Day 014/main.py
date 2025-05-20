import art
import random
from game_data import data
import os


score = 0
previous_competitor = None

while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    if previous_competitor is None:
        competitor_A = random.choice(data)
    else:
        competitor_A = previous_competitor
    
    competitor_B = random.choice(data)
    while competitor_A == competitor_B:
        competitor_B = random.choice(data)

    print(art.logo)
    if score:
        print(f"You're right! Current score: {score}")

    print(f"Compare A: {competitor_A['name']}, a {competitor_A['description']}, from {competitor_A['country']}")
    print(art.vs)
    print(f"Against B: {competitor_B['name']}, a {competitor_B['description']}, from {competitor_B['country']}")


    competitor_A_followers = competitor_A['follower_count']
    competitor_B_followers = competitor_B['follower_count']
    player_choice = input("Who has more followers? Type 'A' or 'B': ").upper().strip()

    if player_choice == 'A' and competitor_A_followers > competitor_B_followers:
        score +=1
    elif player_choice == 'B' and competitor_B_followers > competitor_A_followers:
        score +=1
    elif player_choice not in ['A', 'B']:
        print('Invalid input. Try again')
        break
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        break

    previous_competitor = competitor_B
