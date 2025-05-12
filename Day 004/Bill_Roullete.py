import random

# Get a list of names from the user
names_string = input("Give me everybody's names, separated by a comma: ")
names = names_string.split(", ")

# Count the number of names
num = len(names)

# Generate a random index to select a name from the list
random_index = random.randint(0, num - 1)

# Print the selected name who will buy the meal
print(f"{names[random_index]} is going to buy the meal today!")
