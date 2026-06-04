# Task 1: Create Class
# Run this file using the command: python task1_create_class.py

# Instructions:
# Create a class named `Student`.
# Give it an `__init__` method that accepts `name` and `marks` as parameters.
# Assign these parameters to object attributes `self.name` and `self.marks`.

# Concept Explained:
# The class itself does nothing until we create an object from it. 
# It just sets up the "rules" for what a Student should be.

# ----------------- Write Your Code Below -----------------

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

print("Class 'Student' created successfully!")

# ---------------------------------------------------------
# Expected Output:
# Class 'Student' created successfully!
