from art import logo
from random import randint

print(logo)
print('Welcome to the Number Guessing Game!')

print("I'm thinking of a number between 1 and 100.")
random_number = randint(1, 100)

player_choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower().strip()
if player_choice == 'easy':
    tries = 10
else:
    tries = 5

counter = 1
while True:
    print(f'You have {tries} attempts remaining to guess the number.')
    player_guess = int(input('Make a guess: '))

    if player_guess == random_number:
        print(f'You got it in {counter} tries! The answer was {random_number}.')
        break

    elif player_guess > random_number:
        print('Too high.')
    
    elif player_guess < random_number:
        print('Too low.')
    
    if tries == 1:
        print(f"You've run out of guesses. The answer was {random_number}.")
        break
    
    print('Guess again.')
    tries -= 1
    counter += 1



