# Task 2: Debugging Challenge
# Run this file using the command: python task2_debugging.py

# Instructions:
# The following code has 5 deliberate errors (syntax, logic, and exceptions).
# Find them and fix them so the program runs successfully.
# The goal of the program is to take a list of strings, convert them to integers,
# handle any invalid conversions safely, and print the total sum.

# ----------------- Write Your Code Below -----------------

# BUGGY CODE:
"""
def calculate_total(string_list)
    total = 0
    for item in string_list:
        try
            num = int(item)
            total + num
        except ValueError
            print(f"Skipping invalid item: {item}")
    
    return total

data = ["10", "20", "apple", "30"]
result = calculate_total(data)
print("Total Sum = " + result)
"""

# FIXED CODE:

def calculate_total(string_list): # Fix 1: Added missing colon
    total = 0
    for item in string_list:
        try: # Fix 2: Added missing colon
            num = int(item)
            total += num # Fix 3: Logic error (was total + num, not saving the result)
        except ValueError: # Fix 4: Added missing colon
            print(f"Skipping invalid item: {item}")
    
    return total

data = ["10", "20", "apple", "30"]
result = calculate_total(data)
print(f"Total Sum = {result}") # Fix 5: Used f-string instead of string concatenation with integer

# ---------------------------------------------------------
# Expected Output:
# Skipping invalid item: apple
# Total Sum = 60
