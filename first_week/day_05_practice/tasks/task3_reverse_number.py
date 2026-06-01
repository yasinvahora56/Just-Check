# Task 3: Reverse a Number
# Run this file using the command: python task3_reverse_number.py

# 📝 Instructions:
# Accept a multi-digit number (e.g. 1234) from the user and print its reverse (e.g. 4321).

# ----------------- Write Your Code Below -----------------

number = input("Enter a number: ")

# Method 1: Using Python String Slicing (Easy & Powerful!)
reversed_number = number[::-1]
print("Reversed (String Slicing):", reversed_number)

# Method 2 (Bonus): Using Mathematical logic (Loop-based)
num_val = int(number)
rev_val = 0

while num_val > 0:
    last_digit = num_val % 10
    rev_val = (rev_val * 10) + last_digit
    num_val = num_val // 10

print("Reversed (Mathematical):", rev_val)

# ---------------------------------------------------------
# Expected Output:
# Enter a number: 1234
# Reversed (String Slicing): 4321
# Reversed (Mathematical): 4321
