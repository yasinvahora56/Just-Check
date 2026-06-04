# Task 4: Retry System
# Run this file using the command: python task4_retry_system.py

# Instructions:
# Create a robust input system using a while loop.
# Keep asking the user to enter their age until they enter a valid integer.
# If they enter something invalid, catch the error, show a message, and let the loop repeat.

# Concept Explained:
# We combine a `while True` loop with a `try-except` block.
# If `int(input())` succeeds, we use `break` to exit the loop.
# If it fails, the `except` block catches it and the loop repeats.

# ----------------- Write Your Code Below -----------------

while True:
    try:
        age = int(input("Enter your age: "))
        break # This line only runs if the line above succeeds!
    except ValueError:
        print("Invalid input. Please enter numbers only.")

print(f"Thank you. Your age is {age}.")

# ---------------------------------------------------------
# Expected Output:
# Enter your age: ten
# Invalid input. Please enter numbers only.
# Enter your age: 10
# Thank you. Your age is 10.
