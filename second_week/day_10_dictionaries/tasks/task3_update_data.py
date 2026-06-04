# Task 3: Update Data
# Run this file using the command: python task3_update_data.py

# Instructions:
# Given a student dictionary, update the student's marks and print the modified dictionary.
# Also, add a new field called "Grade".

# ----------------- Write Your Code Below -----------------

student_record = {
    "Name": "John",
    "Age": 20,
    "Marks": 85.5
}

print(f"Original record: {student_record}")

# Update existing value
student_record["Marks"] = 92.0

# Add new key-value pair
student_record["Grade"] = "A"

print(f"Updated record: {student_record}")

# ---------------------------------------------------------
# Expected Output:
# Original record: {'Name': 'John', 'Age': 20, 'Marks': 85.5}
# Updated record: {'Name': 'John', 'Age': 20, 'Marks': 92.0, 'Grade': 'A'}
