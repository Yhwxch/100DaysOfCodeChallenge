import random

# Define lists of characters
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Eazy Level
# password = ""
# for char in range(1, nr_letters + 1):
#     password += random.choice(letters)
# for char in range(1, nr_symbols + 1):
#     password += random.choice(symbols)
# for char in range(1, nr_numbers + 1):
#     password += random.choice(numbers)
# print(password)

# Hard Level
password_list = []

# Generate random letters and append them to the password list
for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

# Generate random symbols and add them to the password list
for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

# Generate random numbers and add them to the password list
for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

print(password_list)

# Shuffle the password list to randomize the characters' order
random.shuffle(password_list)
print(password_list)

# Convert the password list to a string
password = "".join(password_list)

print(f"Your password is: {password}")
