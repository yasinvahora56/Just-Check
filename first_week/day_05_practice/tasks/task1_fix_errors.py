# Task 1: Fix Errors
# Run this file using the command: python task1_fix_errors.py

# Instructions:
# The following program has syntax, type, and logical errors. 
# Fix all the errors so that the program runs and displays correct outputs.

# --- BUGGY PROGRAM (Commented out) ---
# value = input("Enter a number: ")
# if value = 10
# print("Value is ten")
# else:
# print("Value is " + value + 5)

# ----------------- Write Your Fixed Code Below -----------------

value_str = input("Enter a number: ")
value = int(value_str) # Conversion to integer is required for math!

if value == 10: # Fixed: use double equals '==' for comparison & added trailing colon ':'
  print("Value is ten") # Fixed: Indentation
else:
  print("Value is", value + 5) # Fixed: Indentation and comma separation for mixing strings and integers
