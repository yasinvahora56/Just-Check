# Task 4: Password Validator
# Run this file using the command: python task4_password_validator.py

# Instructions:
# Check if a password entered by a user is valid based on two conditions:
# 1. It must have at least 8 characters (using len()).
# 2. It must contain at least one digit (0-9).

# Concept Explained:
# - len(password) gives the total characters in the password string.
# - To check for a digit:
#   We can loop through each character in the password.
#   For each character, check if it is a digit using the `.isdigit()` method.
#   Or check if the character is in "0123456789".
# - We use a boolean flag (e.g., `has_digit`) initialized to `False`.
#   If any character is a digit, we set the flag to `True` and break the loop.

# ----------------- Write Your Code Below -----------------

password = input("Enter password: ")

# Check condition 1: Length
has_min_length = len(password) >= 8

# Check condition 2: Contains a digit
has_digit = False
for char in password:
    if char.isdigit():
        has_digit = True
        break  # Found a digit, no need to keep checking!

# Final validation check
if has_min_length and has_digit:
    print("Valid Password")
else:
    print("Invalid Password")
    # Helpful feedback for the user:
    if not has_min_length:
        print("  - Password must be at least 8 characters long.")
    if not has_digit:
        print("  - Password must contain at least one number.")

# ---------------------------------------------------------
# Expected Output (example runs):
# Enter password: secure
# Invalid Password
#   - Password must be at least 8 characters long.
#   - Password must contain at least one number.

# Enter password: securepassword99
# Valid Password
