# Day 15: JSON Handling

Welcome to Day 15! Today we learn about **JSON** (JavaScript Object Notation). 

Even though it has "JavaScript" in the name, JSON is the universal language of the internet. It is the standard format for storing and exchanging data between different systems (like a Python backend and a React frontend).

---

## 1. What is JSON?

JSON looks exactly like Python dictionaries and lists. 
* Objects `{}` in JSON are like Dictionaries in Python.
* Arrays `[]` in JSON are like Lists in Python.

### Example JSON Data:
```json
{
  "name": "John",
  "age": 20,
  "skills": ["Python", "SQL"]
}
```

---

## 2. The `json` Module

Python has a built-in module called `json` to handle JSON data. You must import it before using it.

```python
import json
```

There are 4 main functions you need to know:
1. `json.dump()`: Write Python data to a JSON **file**.
2. `json.load()`: Read JSON data from a **file** into Python.
3. `json.dumps()`: Convert Python data into a JSON **string** (the 's' stands for string).
4. `json.loads()`: Convert a JSON **string** into Python data.

---

## 3. Writing to a JSON File (`json.dump()`)

You can take a Python dictionary or list and save it directly as a `.json` file.

```python
import json

student_data = {
    "name": "John",
    "marks": 85
}

# Open file in write mode and dump the dictionary into it
with open("student.json", "w") as file:
    json.dump(student_data, file, indent=4) 
    # indent=4 makes the file easily readable (pretty-print)
```

---

## 4. Reading from a JSON File (`json.load()`)

You can read a `.json` file back into a Python dictionary or list.

```python
import json

with open("student.json", "r") as file:
    # Read the file and convert JSON back into a Python dictionary
    data = json.load(file)

print(data["name"])  # Output: John
print(data["marks"]) # Output: 85
```

---

## 5. Working with Strings (`dumps` and `loads`)

Sometimes you don't save to a file, but receive JSON as a string (like from an API).

### Convert String to Python Dictionary:
```python
import json

json_string = '{"name": "Alice", "age": 25}'
python_dict = json.loads(json_string)

print(python_dict["name"]) # Output: Alice
```

### Convert Python Dictionary to String:
```python
import json

python_dict = {"name": "Alice", "age": 25}
json_string = json.dumps(python_dict)

print(json_string) # Output: {"name": "Alice", "age": 25}
```

---

## Practice Tasks
Navigate to the [tasks/](./tasks/) folder to complete today's assignments:
* [Task 1: Write JSON File](./tasks/task1_write_json.py)
* [Task 2: Read JSON File](./tasks/task2_read_json.py)
* [Task 3: Multiple Records](./tasks/task3_multiple_records.py)
* [Task 4: Update JSON](./tasks/task4_update_json.py)
* [Task 5: Search in JSON](./tasks/task5_search_json.py)
