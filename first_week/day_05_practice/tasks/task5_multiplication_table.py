# Task 5: Multiplication Table (User Input)
# Run this file using the command: python task5_multiplication_table.py

# Instructions:
# Accept a number from the user and generate its multiplication table up to 10.

# ----------------- Write Your Code Below -----------------

number = int(input("Enter number: "))

print(f"--- Multiplication Table of {number} ---")
for i in range(1, 11):
  result = number * i
  print(f"{number} x {i} = {result}")
