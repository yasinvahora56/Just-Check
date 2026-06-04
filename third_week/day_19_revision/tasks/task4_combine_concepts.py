# Task 4: Combine Concepts
# Run this file using the command: python task4_combine_concepts.py

# Instructions:
# Build a program that:
# 1. Fetches a list of users from an API (https://jsonplaceholder.typicode.com/users).
# 2. Extracts ONLY their name and email, and saves it into a Python List of Dictionaries.
# 3. Saves that custom list into a JSON file called "contacts.json".
# 4. Handles any internet connection errors gracefully.

# Concept Explained:
# This combines `requests` (API), loops (data extraction), and `json` (file writing).
# This exact workflow is used daily by professional software engineers!

# ----------------- Write Your Code Below -----------------

import requests
import json

def fetch_and_save_contacts():
    url = "https://jsonplaceholder.typicode.com/users"
    
    print("Fetching users from API...")
    try:
        response = requests.get(url, timeout=5)
        
        if response.status_code == 200:
            api_data = response.json()
            
            # Create our own clean list
            clean_contacts = []
            
            # Extract just what we need
            for user in api_data:
                clean_contact = {
                    "name": user["name"],
                    "email": user["email"]
                }
                clean_contacts.append(clean_contact)
                
            # Save to JSON file
            with open("contacts.json", "w") as file:
                json.dump(clean_contacts, file, indent=4)
                
            print(f"Successfully saved {len(clean_contacts)} contacts to contacts.json!")
            
        else:
            print(f"API Error. Status Code: {response.status_code}")
            
    except requests.exceptions.RequestException:
        print("Network Error: Could not connect to the API.")

# Call the function
fetch_and_save_contacts()

# ---------------------------------------------------------
# Expected Output:
# Fetching users from API...
# Successfully saved 10 contacts to contacts.json!
