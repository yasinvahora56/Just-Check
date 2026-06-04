# Task 3: Multiple Records
# Run this file using the command: python task3_multiple_records.py

# Instructions:
# Create a Python list containing dictionaries for three different students.
# Save this list to a new file called "students_list.json".
# Then, read the file back and print it.

# Concept Explained:
# JSON arrays map directly to Python lists. 
# We can save an entire list of complex dictionaries into a single file easily!

# ----------------- Write Your Code Below -----------------

import json

# Python List containing multiple Dictionaries
students = [
    {"name": "John", "marks": 85},
    {"name": "Alice", "marks": 92},
    {"name": "Bob", "marks": 78}
]

# Write to JSON
with open("students_list.json", "w") as file:
    json.dump(students, file, indent=4)
print("Saved 3 students to students_list.json")

# Read back from JSON
print("\n--- Reading Data Back ---")
with open("students_list.json", "r") as file:
    loaded_data = json.load(file)
    
# Loop through the list we just loaded
for student in loaded_data:
    print(f"{student['name']} scored {student['marks']}")

# ---------------------------------------------------------
# Expected Output:
# Saved 3 students to students_list.json
# 
# --- Reading Data Back ---
# John scored 85
# Alice scored 92
# Bob scored 78
