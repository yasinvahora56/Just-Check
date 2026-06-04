# Task 4: Reusable Calculator
# Run this file using the command: python task4_reusable_calculator.py

# Instructions:
# Create 4 separate functions: `add`, `subtract`, `multiply`, and `divide`.
# Each function should take two parameters and return the result.
# Take two numbers from the user and call all 4 functions to display results.

# ----------------- Write Your Code Below -----------------

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"Addition: {add(num1, num2)}")
print(f"Subtraction: {subtract(num1, num2)}")
print(f"Multiplication: {multiply(num1, num2)}")
print(f"Division: {divide(num1, num2)}")

# ---------------------------------------------------------
# Expected Output (for 10 and 5):
# Enter first number: 10
# Enter second number: 5
# Addition: 15.0
# Subtraction: 5.0
# Multiplication: 50.0
# Division: 2.0
