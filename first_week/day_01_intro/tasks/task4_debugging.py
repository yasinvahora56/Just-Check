# Task 4: Debugging Challenge
# Run this file using the command: python task4_debugging.py

# 📝 Instructions:
# Identify and fix the errors in the following two lines of code:
#
# BUGGY LINE 1: print("Hello)
# Error: SyntaxError: unterminated string literal (Missing closing quote)
#
# BUGGY LINE 2: print(10 + "20")
# Error: TypeError: unsupported operand type(s) for +: 'int' and 'str' (Cannot add a number to text directly)

# ----------------- Write Your Fixed Code Below -----------------

# Line 1 Fixed: Added the closing double quotes
print("Hello")

# Line 2 Fixed: Converted string "20" to integer 20, or removed quotes to make it a number
print(10 + 20)

# ---------------------------------------------------------
# Expected Output:
# Hello
# 30
