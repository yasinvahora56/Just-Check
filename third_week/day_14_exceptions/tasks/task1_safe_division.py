# Task 1: Safe Division
# Run this file using the command: python task1_safe_division.py

# Instructions:
# Ask the user for two numbers (a numerator and a denominator).
# Divide the numerator by the denominator.
# Handle the division by zero error safely.

# Concept Explained:
# If `num2` is 0, Python raises a `ZeroDivisionError`.
# We wrap the division inside a try-except block to catch it.

# ----------------- Write Your Code Below -----------------

try:
    num1 = float(input("Enter numerator: "))
    num2 = float(input("Enter denominator: "))
    
    result = num1 / num2
    print(f"Result: {result}")
    
except ZeroDivisionError:
    print("Error: Cannot divide by zero")

# ---------------------------------------------------------
# Expected Output (if denominator is 0):
# Enter numerator: 10
# Enter denominator: 0
# Error: Cannot divide by zero
