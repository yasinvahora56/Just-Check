# Task 4: Sum of Digits
# Run this file using the command: python task4_sum_of_digits.py

# Instructions:
# Accept a multi-digit number (e.g. 123) and calculate the sum of its individual digits (e.g. 1 + 2 + 3 = 6).

# ----------------- Write Your Code Below -----------------

number_str = input("Enter a number: ")

# Method 1: Using character loop
digit_sum = 0
for char in number_str:
  digit_sum = digit_sum + int(char)

print("Sum of digits (Loop):", digit_sum)

# Method 2 (Bonus): Using Mathematical logic (Modulo & Division)
num_val = int(number_str)
math_sum = 0

while num_val > 0:
  last_digit = num_val % 10
  math_sum = math_sum + last_digit
  num_val = num_val // 10

print("Sum of digits (Mathematical):", math_sum)

# ---------------------------------------------------------
# Expected Output:
# Enter a number: 123
# Sum of digits (Loop): 6
# Sum of digits (Mathematical): 6
