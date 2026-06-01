# Task 5: Swap Two Numbers
# Run this file using the command: python task5_swap_numbers.py

# 📝 Instructions:
# Swap the values of two variables (a and b) without using a third variable.

# ----------------- Write Your Code Below -----------------

a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))

print(f"Before Swapping: a = {a}, b = {b}")

# Pythonic Swapping (No third variable)
a, b = b, a

# Alternative Math Swapping:
# a = a + b
# b = a - b
# a = a - b

print(f"After Swapping: a = {a}, b = {b}")

# ---------------------------------------------------------
# Expected Output (e.g. inputs 10 and 20):
# Enter value for a: 10
# Enter value for b: 20
# Before Swapping: a = 10, b = 20
# After Swapping: a = 20, b = 10
