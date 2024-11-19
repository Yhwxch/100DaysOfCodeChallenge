import os

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 != 0:
        return n1 / n2
    return 'invalid'

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

def calculator():
    while True: 
        num1 = float(input('What is the first number: '))

        while True:
            print("Available operations:")
            for symbol in operations:
                print(symbol)

            operation = input('What is the operation: ')
            if operation not in operations:
                print("Invalid operation. Please choose from the available operations.")
                continue

            num2 = float(input('What is the second number: '))

            answer = operations[operation](num1, num2)

            if answer == 'invalid':
                print("Division by zero is not allowed. Try again.")
                continue

            os.system('cls' if os.name == 'nt' else 'clear') 
            print(f'{num1} {operation} {num2} = {answer}')

            choice = input(f"Type 'y' to continue calculating with {answer}, or 'n' to start a new calculation: ").lower()
            if choice == 'n':
                break
            elif choice == 'y':
                num1 = answer
            else:
                print("Invalid choice. Starting a new calculation.")
                break

calculator()
