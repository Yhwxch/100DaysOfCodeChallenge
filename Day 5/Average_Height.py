# Prompt the user to input a list of student heights
student_heights = input("Input a list of student heights: ").split()

# Convert the input heights from strings to integers
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

# Initialize variables to calculate the sum and count of heights
sum_of_heights = 0
count_of_heights = 0

# Calculate the sum of heights and count the number of heights
for height in student_heights:
    sum_of_heights += height
    count_of_heights += 1

# Calculate the average height
average_height = sum_of_heights / count_of_heights

# Print the rounded average height
print(round(average_height))
