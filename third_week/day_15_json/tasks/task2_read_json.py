# Task 2: Read JSON
# Run this file using the command: python task2_read_json.py

# Instructions:
# Read the "student.json" file that you created in Task 1.
# Load the data into a Python dictionary.
# Print the "name" and "marks" keys from the dictionary.

# Concept Explained:
# `json.load(file_object)` reads the file and parses the JSON text back into Python objects (like a dictionary).

# ----------------- Write Your Code Below -----------------

import json

try:
    with open("student.json", "r") as file:
        data = json.load(file)
        
    print("--- Reading JSON Data ---")
    print(f"Name: {data['name']}")
    print(f"Marks: {data['marks']}")

except FileNotFoundError:
    print("Error: 'student.json' not found. Please run task1_write_json.py first.")
except json.JSONDecodeError:
    print("Error: The file is not a valid JSON format.")

# ---------------------------------------------------------
# Expected Output:
# --- Reading JSON Data ---
# Name: John
# Marks: 85
