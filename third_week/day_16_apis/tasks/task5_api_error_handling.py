# Task 5: Error Handling in API
# Run this file using the command: python task5_api_error_handling.py

# Instructions:
# Try to fetch data from an invalid API endpoint: https://invalid-url-example.com/api
# Wrap your code in a try-except block.
# Catch `requests.exceptions.RequestException`.
# Print a user-friendly error message if it fails.

# Concept Explained:
# In real applications, networks fail. You must NEVER let a `requests.get()` crash 
# your program. Always wrap network calls in try-except blocks.

# ----------------- Write Your Code Below -----------------

import requests

url = "https://invalid-url-example.com/api"

print(f"Attempting to connect to: {url}")

try:
    # timeout=5 ensures the program doesn't hang forever if the site is slow
    response = requests.get(url, timeout=5)
    
    if response.status_code == 200:
        print("Success! Data fetched.")
    else:
        print(f"Server returned error code: {response.status_code}")
        
except requests.exceptions.RequestException as e:
    # This catches ANY error related to the requests library (ConnectionError, Timeout, etc.)
    print("Error fetching data. Please check your internet connection or the URL.")

# ---------------------------------------------------------
# Expected Output:
# Attempting to connect to: https://invalid-url-example.com/api
# Error fetching data. Please check your internet connection or the URL.
