# Task 1: Create List
# Run this file using the command: python task1_create_list.py

# Instructions:
# Take 5 numbers from the user one by one, add them to a list, and print the final list.

# Concept Explained:
# - Start with an empty list: `numbers = []`
# - Use a for loop that runs exactly 5 times: `range(5)`
# - In each loop iteration:
#   * Ask the user for a number: `num = int(input(...))`
#   * Append that number to the list: `numbers.append(num)`
# - Print the list at the end.

# ----------------- Write Your Code Below -----------------

numbers = []

print("Please enter 5 numbers:")

for i in range(1, 6):
    num = int(input(f"Enter number {i}: "))
    numbers.append(num)

print("-" * 30)
print(f"Your list of numbers: {numbers}")

# ---------------------------------------------------------
# Expected Output (example run):
# Please enter 5 numbers:
# Enter number 1: 10
# Enter number 2: 25
# Enter number 3: 5
# Enter number 4: 90
# Enter number 5: 20
# ------------------------------
# Your list of numbers: [10, 25, 5, 90, 20]
