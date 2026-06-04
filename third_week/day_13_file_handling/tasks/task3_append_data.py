# Task 3: Append Data
# Run this file using the command: python task3_append_data.py

# Instructions:
# Open "user.txt" in append mode ("a").
# Ask for another name and add it to the file without deleting the old name.

# Concept Explained:
# "a" mode keeps the existing data and adds the new string to the very end of the file.
# Always remember to add \n (newline character) so the new data starts on a new line!

# ----------------- Write Your Code Below -----------------

new_name = input("Enter another name: ")

with open("user.txt", "a") as file:
    file.write(f"Name: {new_name}\n")

print("Data appended to user.txt successfully!")

# Let's read it back to verify
print("\nCurrent file contents:")
try:
    with open("user.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    pass

# ---------------------------------------------------------
# Expected Output (in console):
# Enter another name: Rahul
# Data appended to user.txt successfully!
#
# Current file contents:
# Name: John
# Name: Rahul
