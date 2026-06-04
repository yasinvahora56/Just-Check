# Task 2: Object Creation
# Run this file using the command: python task2_object_creation.py

# Instructions:
# Using the `Student` class from Task 1, create two different student objects.
# Print the name and marks of both students to prove they store different data.

# ----------------- Write Your Code Below -----------------

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

# Creating Objects (Instances)
student1 = Student("John", 85)
student2 = Student("Alice", 92)

print("--- Student 1 ---")
print(f"Name: {student1.name}")
print(f"Marks: {student1.marks}")

print("\n--- Student 2 ---")
print(f"Name: {student2.name}")
print(f"Marks: {student2.marks}")

# ---------------------------------------------------------
# Expected Output:
# --- Student 1 ---
# Name: John
# Marks: 85
#
# --- Student 2 ---
# Name: Alice
# Marks: 92
