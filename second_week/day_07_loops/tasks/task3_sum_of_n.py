# Task 3: Sum of N Numbers
# Run this file using the command: python task3_sum_of_n.py

# Instructions:
# Ask the user for a value of n, then calculate the sum of all numbers from 1 to n.
# Example: if n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15

# Concept Explained:
# - We start a "total" variable at 0 (an empty bucket).
# - Every time the loop runs, we ADD the current number (i) to total.
# - After the loop finishes, total holds the final sum.
# This pattern (starting at 0 and adding) is called an "accumulator pattern".

# Trace through the logic for n=5:
# Before loop: total = 0
# i=1: total = 0 + 1 = 1
# i=2: total = 1 + 2 = 3
# i=3: total = 3 + 3 = 6
# i=4: total = 6 + 4 = 10
# i=5: total = 10 + 5 = 15
# After loop: print 15

# ----------------- Write Your Code Below -----------------

n = int(input("Enter value of n: "))
total = 0  # Accumulator starts at zero

for i in range(1, n + 1):  # range(1, n+1) so that i goes up to n (inclusive)
    total = total + i       # Add each number to total

print(f"Sum = {total}")

# ---------------------------------------------------------
# Expected Output (for input n=5):
# Enter value of n: 5
# Sum = 15
