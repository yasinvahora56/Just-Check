# Task 4: Format Output
# Run this file using the command: python task4_format_output.py

# Instructions:
# Fetch data from https://jsonplaceholder.typicode.com/users
# This returns a list of user dictionaries.
# Loop through the list and print out a clean, formatted "contact card" for the first 3 users.

# Concept Explained:
# Extract specific details like Name, Email, and Company Name.
# Use f-strings to format the output nicely.

# ----------------- Write Your Code Below -----------------

import requests

url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)

if response.status_code == 200:
    users = response.json()
    
    print("--- User Contact Cards ---\n")
    
    for user in users[:3]: # Only process the first 3 users
        print(f"Name   : {user['name']}")
        print(f"Email  : {user['email']}")
        
        # The 'company' key contains another dictionary inside it!
        print(f"Company: {user['company']['name']}")
        print("-" * 30)

else:
    print("Failed to fetch data.")

# ---------------------------------------------------------
# Expected Output:
# --- User Contact Cards ---
#
# Name   : Leanne Graham
# Email  : Sincere@april.biz
# Company: Romaguera-Crona
# ------------------------------
# Name   : Ervin Howell
# Email  : Shanna@melissa.tv
# Company: Deckow-Crist
# ------------------------------
# Name   : Clementine Bauch
# Email  : Nathan@yesenia.net
# Company: Romaguera-Jacob
# ------------------------------
