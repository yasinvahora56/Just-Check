# Task 3: Method
# Run this file using the command: python task3_method.py

# Instructions:
# Add a method called `display_details` to the `Student` class.
# This method should print the student's name and marks when called.

# Concept Explained:
# A method is just a function inside a class. It MUST have `self` as the first parameter.
# Inside the method, use `self.attribute_name` to access the object's data.

# ----------------- Write Your Code Below -----------------

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")

# Create object
student1 = Student("John", 85)

# Call the method
student1.display_details()

# ---------------------------------------------------------
# Expected Output:
# Name: John
# Marks: 85
