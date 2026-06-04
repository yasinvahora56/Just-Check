# Task 3: Grade Function
# Run this file using the command: python task3_grade_function.py

# Instructions:
# Write a function called `get_grade` that takes `marks` as a parameter.
# The function should return a grade based on the following:
# >= 90 : A
# >= 80 : B
# >= 70 : C
# < 70  : F
# Call the function for marks: 95, 82, and 65. Print the results.

# ----------------- Write Your Code Below -----------------

def get_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    else:
        return "F"

print(f"Marks 95 -> Grade: {get_grade(95)}")
print(f"Marks 82 -> Grade: {get_grade(82)}")
print(f"Marks 65 -> Grade: {get_grade(65)}")

# ---------------------------------------------------------
# Expected Output:
# Marks 95 -> Grade: A
# Marks 82 -> Grade: B
# Marks 65 -> Grade: F
