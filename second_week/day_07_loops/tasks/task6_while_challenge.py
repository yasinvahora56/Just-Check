# Task 6: While Loop Challenge
# Run this file using the command: python task6_while_challenge.py

# Instructions:
# Keep asking the user to enter a number.
# Stop ONLY when they enter 0.
# Each time they enter a non-zero number, print it back to them.
# At the end, show how many numbers they entered (not counting 0).

# Concept Explained:
# - A while loop is perfect here because we don't know HOW MANY times the user
#   will enter a number before entering 0.
# - The loop condition `number != 0` means: keep going as long as the input is not 0.
# - We use a counter variable to track how many valid numbers were entered.

# How the loop works step by step:
# 1. We set number = -1 (any non-zero value) to enter the loop initially.
# 2. Inside the loop, we ask for input.
# 3. If the input is not 0, we print it and increment the counter.
# 4. If the input IS 0, the while condition becomes False → loop exits.

# ----------------- Write Your Code Below -----------------

count = 0         # Tracks how many numbers were entered
number = -1       # Starting value, just to enter the loop (any non-zero number works)

print("Keep entering numbers. Enter 0 to stop.")
print("-" * 40)

while number != 0:
    number = int(input("Enter a number (0 to stop): "))
    
    if number != 0:
        print(f"  You entered: {number}")
        count += 1   # count += 1 is the same as count = count + 1

print("-" * 40)
print(f"You entered {count} number(s) before stopping.")

# ---------------------------------------------------------
# Expected Output (example run):
# Keep entering numbers. Enter 0 to stop.
# ----------------------------------------
# Enter a number (0 to stop): 7
#   You entered: 7
# Enter a number (0 to stop): 15
#   You entered: 15
# Enter a number (0 to stop): 3
#   You entered: 3
# Enter a number (0 to stop): 0
# ----------------------------------------
# You entered 3 number(s) before stopping.
