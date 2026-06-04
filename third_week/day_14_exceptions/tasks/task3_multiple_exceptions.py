# Task 3: Multiple Exceptions
# Run this file using the command: python task3_multiple_exceptions.py

# Instructions:
# Combine input conversion and division in one try block.
# Handle both ValueError (if they don't type a number) 
# AND ZeroDivisionError (if they divide by zero).

# Concept Explained:
# You can have multiple except blocks for a single try block.
# Python checks them from top to bottom.

# ----------------- Write Your Code Below -----------------

try:
    num1 = float(input("Enter numerator: "))
    num2 = float(input("Enter denominator: "))
    
    result = num1 / num2
    print(f"Result: {result}")
    
except ValueError:
    print("Error: Input must be a valid number.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

# ---------------------------------------------------------
# Expected Output (if input is letters):
# Enter numerator: ten
# Error: Input must be a valid number.
