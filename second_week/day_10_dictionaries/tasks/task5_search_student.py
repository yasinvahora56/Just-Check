# Task 5: Search Student
# Run this file using the command: python task5_search_student.py

# Instructions:
# Given a list of student dictionaries, ask the user to input a name.
# Search the list for the student.
# If found, print "Student Found" and their marks.
# If not found, print "Student Not Found".

# Concept Explained:
# We iterate through the list of dictionaries and check if the `Name` key matches the search term.
# We can use a flag (`found`) or a `for-else` loop. 
# Here, we use a simple loop with a flag.

# ----------------- Write Your Code Below -----------------

students = [
    {"Name": "John", "Marks": 85},
    {"Name": "Alice", "Marks": 92},
    {"Name": "Bob", "Marks": 78}
]

search_name = input("Enter student name to search: ")
found = False

for student in students:
    # We use .lower() to make the search case-insensitive
    if student["Name"].lower() == search_name.lower():
        print("Student Found")
        print(f"Marks: {student['Marks']}")
        found = True
        break # Exit loop once found

if not found:
    print("Student Not Found")

# ---------------------------------------------------------
# Expected Output (for input 'John'):
# Enter student name to search: John
# Student Found
# Marks: 85
