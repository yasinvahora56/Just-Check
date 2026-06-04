# Task 2: Function for Even/Odd
# Run this file using the command: python task2_even_odd.py

# Instructions:
# Write a function called `check_even_odd` that takes a number as a parameter.
# The function should RETURN "Even" if the number is even, and "Odd" if it is odd.
# Call the function and print the returned value.

# Concept Explained:
# We use the modulus operator `%` to check for even/odd.
# `num % 2 == 0` means even.
# Instead of printing inside the function, we use `return`.

# ----------------- Write Your Code Below -----------------

def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Call the function and store the result
result1 = check_even_odd(10)
print(f"10 is {result1}")

result2 = check_even_odd(7)
print(f"7 is {result2}")

# ---------------------------------------------------------
# Expected Output:
# 10 is Even
# 7 is Odd
