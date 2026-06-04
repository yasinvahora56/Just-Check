# Task 1: Write JSON File
# Run this file using the command: python task1_write_json.py

# Instructions:
# Create a Python dictionary representing a student: {"name": "John", "marks": 85}.
# Use the json module to write this dictionary into a file named "student.json".

# Concept Explained:
# `json.dump(data, file_object)` takes your Python dictionary and writes it to a file.
# We use `indent=4` to format the JSON nicely, making it human-readable.

# ----------------- Write Your Code Below -----------------

import json

student_dict = {
    "name": "John",
    "marks": 85
}

# Open file in write mode
with open("student.json", "w") as file:
    # Dump the dictionary into the file
    json.dump(student_dict, file, indent=4)

print("Data successfully saved to student.json!")

# ---------------------------------------------------------
# Expected Output (in console):
# Data successfully saved to student.json!

# Expected file content (student.json):
# {
#     "name": "John",
#     "marks": 85
# }
