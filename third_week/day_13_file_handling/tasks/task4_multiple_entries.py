# Task 4: Store Multiple Entries
# Run this file using the command: python task4_multiple_entries.py

# Instructions:
# Use a loop to take 3 names from the user.
# Store all 3 names into a new file called "students.txt".

# Concept Explained:
# Combine a `for` loop with file handling.
# Open the file once, and run the loop inside the `with` block.

# ----------------- Write Your Code Below -----------------

print("Enter 3 student names:")

with open("students.txt", "w") as file:
    for i in range(1, 4):
        name = input(f"Student {i}: ")
        file.write(f"{name}\n")

print("\nSaved to students.txt. Let's read it:")

# Verify
with open("students.txt", "r") as file:
    print(file.read())

# ---------------------------------------------------------
# Expected Output (in console):
# Enter 3 student names:
# Student 1: Alice
# Student 2: Bob
# Student 3: Charlie
#
# Saved to students.txt. Let's read it:
# Alice
# Bob
# Charlie
