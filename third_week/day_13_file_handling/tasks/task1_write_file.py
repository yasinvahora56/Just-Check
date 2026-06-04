# Task 1: Write to File
# Run this file using the command: python task1_write_file.py

# Instructions:
# Open a file named "user.txt" in write mode ("w").
# Ask the user for their name and write "Name: [User's Name]" into the file.
# Print a success message after writing.

# Concept Explained:
# "w" mode will create the file in the current directory if it doesn't exist.
# It will completely overwrite any existing content in that file.

# ----------------- Write Your Code Below -----------------

name = input("Enter your name: ")

with open("user.txt", "w") as file:
    file.write(f"Name: {name}\n")

print("Data saved to user.txt successfully!")

# ---------------------------------------------------------
# Expected Output (in console):
# Enter your name: John
# Data saved to user.txt successfully!

# Expected Content in user.txt:
# Name: John
