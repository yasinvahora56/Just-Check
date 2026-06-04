# Task 2: Weather API (Simulation using Open-Meteo)
# Run this file using the command: python task2_weather_api.py

# Instructions:
# Fetch the current temperature of London using the free Open-Meteo API.
# URL: https://api.open-meteo.com/v1/forecast?latitude=51.5085&longitude=-0.1257&current_weather=true
# Extract and print the temperature.

# Concept Explained:
# The JSON returned by this API has a nested structure.
# Example: {"current_weather": {"temperature": 15.5, ...}}
# You must access the dictionary step-by-step: data["current_weather"]["temperature"]

# ----------------- Write Your Code Below -----------------

import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=51.5085&longitude=-0.1257&current_weather=true"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    # Accessing nested dictionaries
    current_temp = data["current_weather"]["temperature"]
    
    print(f"Temperature in London: {current_temp}°C")
else:
    print("Failed to fetch weather data.")

# ---------------------------------------------------------
# Expected Output (will vary based on actual live weather):
# Temperature in London: 14.5°C
