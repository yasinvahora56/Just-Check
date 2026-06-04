# Task 4: Factorial
# Run this file using the command: python task4_factorial.py

# Instructions:
# Take a number from the user and compute its factorial.
# Factorial of 5 = 5 * 4 * 3 * 2 * 1 = 120
# Factorial of 0 = 1 (by mathematical definition)

# Concept Explained:
# - Factorial means: multiply the number by every integer below it down to 1.
# - We use a "product accumulator" — similar to the sum accumulator, but we:
#     * Start at 1 (NOT 0, because multiplying by 0 would give 0!)
#     * Multiply instead of adding.
# - We loop from 1 up to n (inclusive), multiplying result each time.

# Trace through for n=5:
# Before loop: result = 1
# i=1: result = 1 * 1 = 1
# i=2: result = 1 * 2 = 2
# i=3: result = 2 * 3 = 6
# i=4: result = 6 * 4 = 24
# i=5: result = 24 * 5 = 120
# After loop: print 120

# ----------------- Write Your Code Below -----------------

n = int(input("Enter a number: "))
result = 1  # Accumulator must start at 1 for multiplication!

for i in range(1, n + 1):
    result = result * i

print(f"Factorial = {result}")

# ---------------------------------------------------------
# Expected Output (for input 5):
# Enter a number: 5
# Factorial = 120
