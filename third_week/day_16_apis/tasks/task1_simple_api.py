# Task 1: Simple API Call
# Run this file using the command: python task1_simple_api.py

# Instructions:
# Make a GET request to the public PokeAPI to get data about the Pokemon 'pikachu'.
# URL: https://pokeapi.co/api/v2/pokemon/pikachu
# Print the name and the weight of the Pokemon.

# Concept Explained:
# 1. Use requests.get(url) to fetch data.
# 2. Check response.status_code == 200.
# 3. Use response.json() to convert the JSON string into a Python dictionary.
# 4. Access the dictionary keys like normal.

# ----------------- Write Your Code Below -----------------

import requests

url = "https://pokeapi.co/api/v2/pokemon/pikachu"

print("Fetching data from PokeAPI...")
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f"\nPokemon Name: {data['name'].title()}")
    print(f"Weight: {data['weight']} hectograms")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")

# ---------------------------------------------------------
# Expected Output:
# Fetching data from PokeAPI...
#
# Pokemon Name: Pikachu
# Weight: 60 hectograms
