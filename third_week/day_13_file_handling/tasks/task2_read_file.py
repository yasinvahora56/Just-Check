# Task 2: Read from File
# Run this file using the command: python task2_read_file.py

# Instructions:
# Open the "user.txt" file in read mode ("r").
# Read the contents and print them to the screen.

# Concept Explained:
# "r" mode is used to read existing files. 
# If the file does not exist, Python will throw a FileNotFoundError.
# Ensure you run task1_write_file.py before this one so the file exists!

# ----------------- Write Your Code Below -----------------

print("Reading from user.txt:\n" + "-"*20)

try:
    with open("user.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: The file 'user.txt' was not found. Run task 1 first!")

# ---------------------------------------------------------
# Expected Output (in console):
# Reading from user.txt:
# --------------------
# Name: John
