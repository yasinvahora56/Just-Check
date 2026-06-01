# Task 2: Calculator (Input Based)
# Run this file using the command: python task2_calculator.py

# Instructions:
# Prompt the user to enter two numbers.
# Perform type casting to float or int.
# Print their Sum, Difference, and Product.

# ----------------- Write Your Code Below -----------------

# Taking input and converting to integer
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Calculations
sum_val = num1 + num2
diff_val = num1 - num2
prod_val = num1 * num2

# Outputting results
print("Sum:", sum_val)
print("Difference:", diff_val)
print("Product:", prod_val)

# ---------------------------------------------------------
# Expected Output (for inputs 20 and 10):
# Enter first number: 20
# Enter second number: 10
# Sum: 30
# Difference: 10
# Product: 200
