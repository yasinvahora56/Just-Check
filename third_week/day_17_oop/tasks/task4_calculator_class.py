# Task 4: Calculator Class
# Run this file using the command: python task4_calculator_class.py

# Instructions:
# Create a `Calculator` class.
# It should have methods for `add`, `subtract`, `multiply`, and `divide`.
# Each method takes two parameters (besides self) and returns the result.
# Instantiate the class and test all 4 methods.

# Concept Explained:
# A class does not always need an `__init__` method if it doesn't need to store 
# state (data) upon creation. The methods just perform actions.

# ----------------- Write Your Code Below -----------------

class Calculator:
    def add(self, a, b):
        return a + b
        
    def subtract(self, a, b):
        return a - b
        
    def multiply(self, a, b):
        return a * b
        
    def divide(self, a, b):
        if b == 0:
            return "Cannot divide by zero"
        return a / b

# Create the object
calc = Calculator()

# Call the methods
print(f"10 + 5 = {calc.add(10, 5)}")
print(f"10 - 5 = {calc.subtract(10, 5)}")
print(f"10 * 5 = {calc.multiply(10, 5)}")
print(f"10 / 5 = {calc.divide(10, 5)}")

# ---------------------------------------------------------
# Expected Output:
# 10 + 5 = 15
# 10 - 5 = 5
# 10 * 5 = 50
# 10 / 5 = 2.0
