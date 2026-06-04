# Task 2: Multiplication Table
# Run this file using the command: python task2_multiplication_table.py

# Instructions:
# Ask the user to enter a number, then print its full multiplication table from 1 to 10.
# Use a for loop.

# Concept Explained:
# - We use int(input()) to get the number as an integer.
# - range(1, 11) gives us 1, 2, 3, ..., 10
# - On each iteration, we multiply the user's number by the loop variable i
# - f-strings let us embed variables inside strings: f"{num} x {i} = {num * i}"

# ----------------- Write Your Code Below -----------------

num = int(input("Enter number: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# ---------------------------------------------------------
# Expected Output (for input 5):
# Enter number: 5
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# 5 x 4 = 20
# 5 x 5 = 25
# 5 x 6 = 30
# 5 x 7 = 35
# 5 x 8 = 40
# 5 x 9 = 45
# 5 x 10 = 50
