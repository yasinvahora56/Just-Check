# Task 1: Grade System
# Run this file using the command: python task1_grade_system.py

# Instructions:
# Take marks as input from the user (out of 100).
# Print grades based on the following:
# Marks >= 90 -> Grade A
# Marks >= 80 -> Grade B
# Marks >= 70 -> Grade C
# Else -> Grade F

# ----------------- Write Your Code Below -----------------

marks = int(input("Enter Marks: "))

if marks >= 90:
  grade = "A"
elif marks >= 80:
  grade = "B"
elif marks >= 70:
  grade = "C"
else:
  grade = "F"

print("Grade:", grade)

# ---------------------------------------------------------
# Expected Output:
# Enter Marks: 85
# Grade: B
