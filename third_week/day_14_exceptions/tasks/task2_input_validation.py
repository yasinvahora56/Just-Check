# Task 2: Input Validation
# Run this file using the command: python task2_input_validation.py

# Instructions:
# Ask the user to enter their age.
# If they enter something that isn't a number (like "twenty"), handle it safely.

# Concept Explained:
# `int(input())` will crash with a `ValueError` if the input cannot be converted to an integer.

# ----------------- Write Your Code Below -----------------

try:
    age = int(input("Enter your age: "))
    print(f"You are {age} years old.")
except ValueError:
    print("Error: Please enter a valid numerical age (e.g., 20).")

# ---------------------------------------------------------
# Expected Output (if input is "hello"):
# Enter your age: hello
# Error: Please enter a valid numerical age (e.g., 20).
