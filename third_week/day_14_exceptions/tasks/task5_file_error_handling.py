# Task 5: File Error Handling
# Run this file using the command: python task5_file_error_handling.py

# Instructions:
# Try to open and read a file called "missing_file.txt".
# Since it does not exist, catch the FileNotFoundError.
# Print "Error: File not found".

# Concept Explained:
# Attempting to read a file that doesn't exist crashes the program.
# Wrapping it in try-except ensures the program handles it gracefully.

# ----------------- Write Your Code Below -----------------

try:
    with open("missing_file.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: File not found")

# ---------------------------------------------------------
# Expected Output:
# Error: File not found
