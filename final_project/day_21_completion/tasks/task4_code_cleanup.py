# Task 4: Code Cleanup
# This is a reading/concept task!

# Instructions:
# Read the guidelines below to understand how to clean up code before presenting it.

"""
What is Code Cleanup (Refactoring)?
Refactoring is the process of restructuring existing computer code without changing its external behavior.
It improves the nonfunctional attributes of the software.

Checklist before you submit your Final Project:

1. Remove Dead Code:
   Delete any `print("test")` statements you used for debugging.
   Remove unused variables or functions that you wrote but never ended up calling.

2. Variable Naming:
   Are your names clear? `x` and `y` are bad. `expense_amount` and `user_choice` are good.
   Use snake_case for variables and functions in Python (e.g., `calculate_total`).

3. Comments:
   Don't comment the obvious:
   # Adds 1 to i
   i = i + 1  <-- BAD COMMENT

   Explain WHY, not WHAT:
   # We add 1 because the list index starts at 0, but users count from 1
   user_display_index = array_index + 1  <-- GOOD COMMENT

4. DRY Principle (Don't Repeat Yourself):
   If you wrote the exact same file-saving code in 3 different places, 
   move it into a single `save_data()` function and call that function 3 times instead.
"""
print("Read the guidelines in this file to understand Code Cleanup!")
