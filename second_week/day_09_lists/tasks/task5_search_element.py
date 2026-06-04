# Task 5: Search Element
# Run this file using the command: python task5_search_element.py

# Instructions:
# Create a program that searches for a specific number in a list.
# 1. Ask the user for a search number.
# 2. Check if the number is in the list.
# 3. Print "Found" or "Not Found".
# 4. Optional: If found, print the index (position) where it was found.

# Concept Explained:
# Method 1: Using the `in` operator (Sleek and Pythonic)
#   - Syntax: `if target in numbers_list:`
#   - This directly returns True or False.

# Method 2: Manual search using a loop (Linear Search)
#   - We loop through the list index-by-index: `range(len(numbers))`
#   - Compare `numbers[i] == target`.
#   - If matches, print and set a flag, then break out of the loop.

# ----------------- Write Your Code Below -----------------

numbers = [12, 45, 78, 23, 56, 89]
print(f"Available numbers: {numbers}")

target = int(input("Enter number to search: "))

# --- Method 1: Using 'in' operator ---
print("\n--- Method 1 (in Operator) ---")
if target in numbers:
    # .index(value) returns the index of the first occurrence of that value
    position = numbers.index(target)
    print(f"Found at index {position}!")
else:
    print("Not Found")

# --- Method 2: Manual Loop (Linear Search) ---
print("\n--- Method 2 (Manual Loop) ---")
found = False
found_index = -1

for i in range(len(numbers)):
    if numbers[i] == target:
        found = True
        found_index = i
        break  # Exit loop immediately since we found it

if found:
    print(f"Found at index {found_index}!")
else:
    print("Not Found")

# ---------------------------------------------------------
# Expected Output (if input is 23):
# Enter number to search: 23
# 
# --- Method 1 (in Operator) ---
# Found at index 3!
# 
# --- Method 2 (Manual Loop) ---
# Found at index 3!
