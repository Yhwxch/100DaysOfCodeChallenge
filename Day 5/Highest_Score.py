# Prompt the user to input a list of student scores
student_scores = input("Input a list of student scores: ").split()

# Convert the input scores from strings to integers
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Print the list of student scores
print(student_scores)

# Initialize a variable to track the highest score
highest_score = 0

# Find the highest score in the list
for score in student_scores:
    if score > highest_score:
        highest_score = score

# Print the highest score
print(f"The highest score in the class is: {highest_score}")
