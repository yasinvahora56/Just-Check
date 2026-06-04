# Task 2: Find Max and Min
# Run this file using the command: python task2_max_min.py

# Instructions:
# Given a list of numbers, find the maximum (largest) and minimum (smallest) value in it.
# Write it using two methods:
# Method 1: Python's built-in functions max() and min().
# Method 2: Manually finding max and min using loops (critical for logic building!).

# Concept Explained:
# Manual Logic:
#   1. Assume the first number in the list is both the largest and smallest.
#      `largest = numbers[0]`
#      `smallest = numbers[0]`
#   2. Loop through all numbers in the list.
#   3. If you find a number greater than `largest`, update `largest`.
#   4. If you find a number smaller than `smallest`, update `smallest`.

# ----------------- Write Your Code Below -----------------

# Sample list
numbers = [45, 10, 89, 3, 56, 90, 12]
print(f"List: {numbers}\n")

# --- Method 1: Using Built-in Functions ---
built_in_max = max(numbers)
built_in_min = min(numbers)
print("--- Method 1 (Built-in) ---")
print(f"Max = {built_in_max}")
print(f"Min = {built_in_min}\n")

# --- Method 2: Manual Logic with Loops ---
# Initialize largest and smallest with the first element
largest = numbers[0]
smallest = numbers[0]

# Loop through the list to compare
for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print("--- Method 2 (Manual Loop) ---")
print(f"Max = {largest}")
print(f"Min = {smallest}")

# ---------------------------------------------------------
# Expected Output:
# List: [45, 10, 89, 3, 56, 90, 12]
# 
# --- Method 1 (Built-in) ---
# Max = 90
# Min = 3
# 
# --- Method 2 (Manual Loop) ---
# Max = 90
# Min = 3
