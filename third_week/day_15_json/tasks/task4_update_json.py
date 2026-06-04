# Task 4: Update JSON
# Run this file using the command: python task4_update_json.py

# Instructions:
# 1. Read the "student.json" file.
# 2. Modify the student's marks from 85 to 95.
# 3. Add a new key called "grade" with the value "A".
# 4. Write the updated dictionary back to "student.json".

# Concept Explained:
# You cannot directly "edit" a file on disk line-by-line easily.
# The standard way to update JSON is: Read it -> Modify Python object -> Overwrite file.

# ----------------- Write Your Code Below -----------------

import json

try:
    # Step 1: Read the existing data
    with open("student.json", "r") as file:
        student = json.load(file)
        
    print(f"Original: {student}")
    
    # Step 2 & 3: Modify the Python dictionary
    student["marks"] = 95
    student["grade"] = "A"
    
    # Step 4: Write it back (overwriting the file)
    with open("student.json", "w") as file:
        json.dump(student, file, indent=4)
        
    print(f"Updated: {student}")
    print("Updates saved successfully!")

except FileNotFoundError:
    print("Error: Run task1_write_json.py first to create the file.")

# ---------------------------------------------------------
# Expected Output:
# Original: {'name': 'John', 'marks': 85}
# Updated: {'name': 'John', 'marks': 95, 'grade': 'A'}
# Updates saved successfully!
