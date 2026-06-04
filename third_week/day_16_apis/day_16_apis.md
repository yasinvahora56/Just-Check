# Day 16: APIs Using `requests`

Welcome to Day 16! Today we learn how to connect Python to the real world using APIs. 

---

## 1. What is an API?

API stands for **Application Programming Interface**. It allows two software programs to communicate with each other.
Think of an API like a waiter in a restaurant:
- You (the client/Python script) give an order (a Request) to the waiter (the API).
- The waiter takes the order to the kitchen (the Server/Database).
- The waiter brings your food (the Response/Data) back to you.

Most modern APIs return data in **JSON format**! That's why we learned JSON yesterday.

---

## 2. The `requests` Library

Python doesn't come with `requests` built-in, but it is the industry standard for making API calls. You must install it first.

### Installation (Run this in your terminal):
```bash
pip install requests
```

---

## 3. Making a Simple GET Request

To ask a server for data, we use `requests.get(url)`.

```python
import requests

url = "https://api.github.com"
response = requests.get(url)

# Print the Status Code
print(response.status_code)  
# 200 means OK (Success)
# 404 means Not Found
```

---

## 4. Extracting JSON Data

If the request is successful (Status 200), we can extract the JSON data using `.json()`.

```python
import requests

url = "https://jsonplaceholder.typicode.com/users/1"
response = requests.get(url)

if response.status_code == 200:
    data = response.json() # Converts API response into a Python dictionary
    print(f"Name: {data['name']}")
    print(f"Email: {data['email']}")
else:
    print(f"Failed to fetch data. Error code: {response.status_code}")
```

---

## 5. Handling Connection Errors

What if the internet is down or the URL is invalid? The program will crash. We must use `try-except` blocks!

```python
import requests

try:
    response = requests.get("https://invalid-url-that-does-not-exist.com")
except requests.exceptions.RequestException as e:
    print("Error connecting to the API. Check your internet connection or the URL.")
```

---

## Practice Tasks
Navigate to the [tasks/](./tasks/) folder to complete today's assignments:

*(Note: We will use free, public APIs that do not require authentication keys for these tasks)*

* [Task 1: Simple API Call](./tasks/task1_simple_api.py)
* [Task 2: Weather API Simulation](./tasks/task2_weather_api.py)
* [Task 3: News API (Formatting Data)](./tasks/task3_news_api.py)
* [Task 4: Format Output](./tasks/task4_format_output.py)
* [Task 5: Error Handling](./tasks/task5_api_error_handling.py)
