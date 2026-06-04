# Task 2: Access Data
# Run this file using the command: python task2_access_data.py

# Instructions:
# Given a student dictionary, extract and print specific values (Name and Marks).
# Output format should match the expected output.

# ----------------- Write Your Code Below -----------------

student_record = {
    "Name": "John",
    "Age": 20,
    "Marks": 85.5
}

# Accessing values using keys
name = student_record["Name"]
marks = student_record["Marks"]

print(f"Name: {name}")
print(f"Marks: {marks}")

# ---------------------------------------------------------
# Expected Output:
# Name: John
# Marks: 85.5
