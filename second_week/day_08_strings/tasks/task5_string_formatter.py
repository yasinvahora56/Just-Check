# Task 5: String Formatter
# Run this file using the command: python task5_string_formatter.py

# Instructions:
# Ask the user for their name and the city they live in.
# Print a formatted sentence using f-strings.
# Standardize the name to Title Case (e.g., john -> John) and the city to Title Case (e.g., delhi -> Delhi).

# Concept Explained:
# - `.title()` is a string method that capitalizes the first letter of each word
#   and makes all other letters lowercase.
#   Example: "jOHn" -> "John", "new york" -> "New York"
# - We then insert these variables into an f-string:
#   f"My name is {name} and I live in {city}"

# ----------------- Write Your Code Below -----------------

name = input("Enter your name: ")
city = input("Enter your city: ")

# Standardize values using string methods
formatted_name = name.strip().title()
formatted_city = city.strip().title()

# Format the final string
message = f"My name is {formatted_name} and I live in {formatted_city}"

print(message)

# ---------------------------------------------------------
# Expected Output:
# Enter your name: john
# Enter your city: delhi
# My name is John and I live in Delhi
