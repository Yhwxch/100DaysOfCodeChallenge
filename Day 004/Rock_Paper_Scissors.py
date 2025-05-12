import random

# Define the images for rock, paper, and scissors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.(___)
'''

# Store the game images in a list
game_images = [rock, paper, scissors]

# Get the user's choice
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

# Validate the user's choice
if user_choice >= 3 or user_choice < 0:
    print("Invalid choice. Try again.")
else:
    # Print the user's choice
    print("You chose:")
    print(game_images[user_choice])

    # Generate a random choice for the computer
    computer_choice = random.randint(0, 2)

    # Print the computer's choice
    print("Computer chose:")
    print(game_images[computer_choice])

    # Determine the outcome of the game
    if user_choice == computer_choice:
        print("It's a draw!")
    elif (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
        print("You win!")
    else:
        print("You lose!")
