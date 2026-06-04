# Task 3: Sum of List
# Run this file using the command: python task3_sum_list.py

# Instructions:
# Given a list of numbers, calculate the sum of all elements.
# Write it using two methods:
# Method 1: Using the built-in sum() function.
# Method 2: Manually calculating using a loop.

# Concept Explained:
# - Method 1: sum(list) adds all items inside the list automatically.
# - Method 2: Start a variable `total = 0`.
#   Loop through every number in the list, adding it to `total` one by one.
#   This is the accumulator pattern.

# ----------------- Write Your Code Below -----------------

# Sample list
numbers = [10, 20, 30, 40, 50]
print(f"List: {numbers}\n")

# --- Method 1: Built-in function ---
built_in_sum = sum(numbers)
print("--- Method 1 (Built-in) ---")
print(f"Total = {built_in_sum}\n")

# --- Method 2: Manual Loop ---
total = 0
for num in numbers:
    total += num  # Add each element to total

print("--- Method 2 (Manual Loop) ---")
print(f"Total = {total}")

# ---------------------------------------------------------
# Expected Output:
# List: [10, 20, 30, 40, 50]
# 
# --- Method 1 (Built-in) ---
# Total = 150
# 
# --- Method 2 (Manual Loop) ---
# Total = 150
