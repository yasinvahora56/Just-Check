# Task 2: Even or Odd
# Run this file using the command: python task2_even_odd.py

# Instructions:
# Read a single number from the user.
# Use comparison and arithmetic operator (specifically modulo '%') to check if the number is Even or Odd.
# Print the outcome.

# ----------------- Write Your Code Below -----------------

number = int(input("Enter number: "))

# If number is fully divisible by 2, remainder (%) is 0 -> Even
if number % 2 == 0:
  print("Even")
else:
  print("Odd")

# ---------------------------------------------------------
# Expected Output:
# Enter number: 7
# Odd
