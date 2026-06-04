# Task 5: Search in JSON
# Run this file using the command: python task5_search_json.py

# Instructions:
# 1. Read the "students_list.json" file.
# 2. Ask the user for a student name to search.
# 3. Search through the loaded JSON data.
# 4. Print "Student Found" and their marks, or "Not found".

# Concept Explained:
# Once JSON data is loaded via `json.load()`, it behaves exactly like normal 
# Python lists and dictionaries. You can use standard loops to search through it!

# ----------------- Write Your Code Below -----------------

import json

try:
    with open("students_list.json", "r") as file:
        students = json.load(file)
        
    search_name = input("Enter student name to search: ")
    found = False
    
    for student in students:
        if student["name"].lower() == search_name.lower():
            print("\nStudent Found!")
            print(f"Marks: {student['marks']}")
            found = True
            break
            
    if not found:
        print("\nStudent not found.")

except FileNotFoundError:
    print("Error: 'students_list.json' not found. Run task 3 first.")

# ---------------------------------------------------------
# Expected Output (if input is Alice):
# Enter student name to search: Alice
# 
# Student Found!
# Marks: 92
