# Getting inputs from the user such as bill amount, tip percentage, and number of people to divide
bill = float(input("What was the total bill? "))
tip_percentage = int(input("How much tip would you like to give? 10, 12, or 15? "))
number_of_people = int(input("How many people to split the bill? "))

# Necessary math operations to calculate the amount per person
tip = bill * tip_percentage / 100
pay_per_person = (bill + tip) / number_of_people
pay_per_person = round(pay_per_person, 2)

# Printing the output
print(f"Each person should pay: {pay_per_person}")
