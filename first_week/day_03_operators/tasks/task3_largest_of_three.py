# Task 3: Largest of 3 Numbers
# Run this file using the command: python task3_largest_of_three.py

# Instructions:
# Accept three numbers from the user and find the largest number using comparison/logical operators.

# ----------------- Write Your Code Below -----------------

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

# Logic to find the largest
if num1 >= num2 and num1 >= num3:
  largest = num1
elif num2 >= num1 and num2 >= num3:
  largest = num2
else:
  largest = num3

print("Largest is", largest)

# ---------------------------------------------------------
# Expected Output (e.g., for inputs 12, 45, 32):
# Enter first number: 12
# Enter second number: 45
# Enter third number: 32
# Largest is 45
