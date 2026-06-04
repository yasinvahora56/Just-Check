# Task 5: Pattern Printing
# Run this file using the command: python task5_pattern.py

# Instructions:
# Print a right-angled triangle of stars.
# Row 1 has 1 star, Row 2 has 2 stars, ... Row 5 has 5 stars.

# Concept Explained:
# This uses a NESTED loop approach — but we can do it simply with a single loop!
# - The outer loop variable `i` represents the current row number (1, 2, 3, 4, 5).
# - On each row, we need to print exactly `i` stars.
# - We use the string multiplication trick: "*" * i → repeats the star i times.
#   Example: "*" * 3 gives "***"

# Method 1: Using string multiplication (clean & simple)
print("--- Method 1: String Multiplication ---")
for i in range(1, 6):
    print("*" * i)

print()  # Blank line between methods

# Method 2: Using a nested loop (shows the concept step by step)
print("--- Method 2: Nested Loop ---")
for i in range(1, 6):       # Outer loop: row number
    for j in range(i):      # Inner loop: runs i times for row i
        print("*", end="")  # Print star without newline
    print()                 # After inner loop, move to next line

# ---------------------------------------------------------
# Expected Output:
# *
# **
# ***
# ****
# *****
