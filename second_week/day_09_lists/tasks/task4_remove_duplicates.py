# Task 4: Remove Duplicates
# Run this file using the command: python task4_remove_duplicates.py

# Instructions:
# Given a list containing duplicate values, create a new list with the duplicate elements removed.
# Input: [1, 2, 2, 3, 4, 4]
# Expected Output: [1, 2, 3, 4]

# Concept Explained:
# Method 1: Using a loop
#   1. Start with an empty list `unique_list = []`.
#   2. Loop through every element in the original list.
#   3. If the element is NOT already in `unique_list`, append it.
#   4. Otherwise (if it's already there), ignore it.

# Method 2: Using set()
#   In Python, a `set` is a data type that only holds UNIQUE values.
#   - Converting a list to a set automatically removes duplicates: `set(original)`
#   - Converting it back to a list gives the clean list: `list(set(original))`
#   Note: set() does not maintain the original order of elements, whereas the loop method does.

# ----------------- Write Your Code Below -----------------

original_list = [1, 2, 2, 3, 4, 4, 5, 1, 3]
print(f"Original List: {original_list}\n")

# --- Method 1: Using a Loop (Preserves Order) ---
unique_list = []
for item in original_list:
    if item not in unique_list:
        unique_list.append(item)

print("--- Method 1 (Loop) ---")
print(f"Clean List: {unique_list}\n")

# --- Method 2: Using set() (Simplest, doesn't guarantee order) ---
clean_set_list = list(set(original_list))
print("--- Method 2 (set) ---")
print(f"Clean List: {clean_set_list}")

# ---------------------------------------------------------
# Expected Output:
# Original List: [1, 2, 2, 3, 4, 4, 5, 1, 3]
# 
# --- Method 1 (Loop) ---
# Clean List: [1, 2, 3, 4, 5]
# 
# --- Method 2 (set) ---
# Clean List: [1, 2, 3, 4, 5]
