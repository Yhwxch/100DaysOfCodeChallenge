# Iterate over numbers from 1 to 100
for num in range(1, 101):
    # Check if the number is divisible by both 3 and 5
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    # Check if the number is divisible by 3
    elif num % 3 == 0:
        print("Fizz")
    # Check if the number is divisible by 5
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
