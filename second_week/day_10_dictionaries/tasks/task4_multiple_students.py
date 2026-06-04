# Task 4: Multiple Students
# Run this file using the command: python task4_multiple_students.py

# Instructions:
# Create a list that stores 3 student dictionaries.
# Each dictionary should have "Name" and "Marks".
# Use a loop to print the name and marks of each student.

# Concept Explained:
# A list can hold multiple dictionary objects.
# We can iterate over the list using a `for` loop. Each element in the list is a dictionary.

# ----------------- Write Your Code Below -----------------

students = [
    {"Name": "John", "Marks": 85},
    {"Name": "Alice", "Marks": 92},
    {"Name": "Bob", "Marks": 78}
]

# Loop through the list
for student in students:
    name = student["Name"]
    marks = student["Marks"]
    print(f"Student: {name}, Marks: {marks}")

# ---------------------------------------------------------
# Expected Output:
# Student: John, Marks: 85
# Student: Alice, Marks: 92
# Student: Bob, Marks: 78
