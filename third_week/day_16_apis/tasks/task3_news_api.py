# Task 3: News API (Formatting Data)
# Run this file using the command: python task3_news_api.py

# Instructions:
# Fetch sample data from a free dummy JSON API that acts like a news feed.
# URL: https://jsonplaceholder.typicode.com/posts
# The API returns a LIST of dictionaries.
# Loop through the list and print the titles of the first 5 posts.

# Concept Explained:
# Not all APIs return a single dictionary `{}`. Some return a list `[]`.
# We use standard list slicing `[:5]` to get only the first 5 items, 
# then loop through them.

# ----------------- Write Your Code Below -----------------

import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

if response.status_code == 200:
    posts = response.json() # This is a LIST of dictionaries
    
    print("--- Top 5 Latest Headlines ---")
    
    # Loop through the first 5 items using slicing
    for index, post in enumerate(posts[:5], start=1):
        # post["title"] accesses the title key of the current dictionary
        print(f"{index}. {post['title'].title()}")
else:
    print("Failed to fetch news data.")

# ---------------------------------------------------------
# Expected Output:
# --- Top 5 Latest Headlines ---
# 1. Sunt Aut Facere Repellat Provident Occaecati Excepturi Optio Reprehenderit
# 2. Qui Est Esse
# 3. Ea Molestias Quasi Exercitationem Repellat Qui Ipsa Sit Aut
# 4. Eum Et Est Occaecati
# 5. Nesciunt Quas Odio
