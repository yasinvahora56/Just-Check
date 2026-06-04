# Task 1: Print Numbers 1–100
# Run this file using the command: python task1_print_numbers.py

# Instructions:
# Print every number from 1 to 100 on the same line, separated by a space.
# Use a for loop with range().

# Concept Explained:
# range(1, 101) generates numbers from 1 up to (but not including) 101.
# That means it gives us: 1, 2, 3, ..., 100
# end=" " in print() means "don't go to a new line, put a space instead".

# ----------------- Write Your Code Below -----------------

for i in range(1, 101):
    print(i, end=" ")

print()  # This moves the cursor to a new line at the very end

# ---------------------------------------------------------
# Expected Output:
# 1 2 3 4 5 6 7 ... 98 99 100
