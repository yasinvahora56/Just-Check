# Day 10: Dictionaries

Welcome to Day 10! Today we learn about **Dictionaries**. Dictionaries are used to store data values in key-value pairs. They are unordered (in Python 3.7+, they maintain insertion order), changeable (mutable), and do not allow duplicate keys.

Think of a dictionary like a real-world dictionary: you search for a **word (Key)** to find its **meaning (Value)**.

---

## 1. What is a Dictionary?

In Python, dictionaries are written inside curly braces `{}`. Each pair consists of a key and a value, separated by a colon `:`.

### Syntax:
```python
student = {
    "name": "John",
    "age": 20,
    "marks": 85
}
```
* **Keys**: Must be unique and immutable (usually strings or numbers).
* **Values**: Can be of any data type (strings, integers, floats, lists, or even other dictionaries) and can have duplicates.

---

## 2. Accessing and Updating Dictionaries

### Accessing Values:
You can access values by using the key inside square brackets `[]` or using the `.get()` method.

```python
student = {"name": "John", "age": 20, "marks": 85}

print(student["name"])  # John
print(student["marks"]) # 85

# Using .get() (safer because it returns None instead of raising an error if the key doesn't exist)
print(student.get("age"))        # 20
print(student.get("gender"))     # None
print(student.get("gender", "N/A")) # 'N/A' (allows a custom default value)
```

### Modifying and Adding Values:
You can update an existing value or add a new key-value pair using square brackets.

```python
student = {"name": "John", "age": 20, "marks": 85}

# Update age
student["age"] = 21

# Add a new key-value pair (city)
student["city"] = "Delhi"

print(student)
# Output: {'name': 'John', 'age': 21, 'marks': 85, 'city': 'Delhi'}
```

### Removing Items:
- `pop(key)`: Removes the key and returns its value.
- `del`: Removes a key-value pair.
- `clear()`: Empties the entire dictionary.

```python
student = {"name": "John", "age": 20, "marks": 85}

student.pop("age")  # Removes the key "age"
print(student)      # {'name': 'John', 'marks': 85}

del student["marks"]
print(student)      # {'name': 'John'}
```

---

## 3. Looping Through Dictionaries

You can iterate through keys, values, or key-value pairs.

```python
student = {"name": "John", "age": 20, "marks": 85}

# 1. Loop through keys (default behavior)
for key in student:
    print(key, "->", student[key])

# 2. Loop through values directly using .values()
for value in student.values():
    print(value)

# 3. Loop through key-value pairs using .items() (Recommended!)
for key, value in student.items():
    print(f"Key: {key} | Value: {value}")
```

---

## 4. Complex Structures: Dictionaries and Lists

In real applications, you often combine lists and dictionaries:
* **A List of Dictionaries**: Great for storing multiple student records.
* **A Dictionary of Lists**: Great for storing multiple attributes (like a student with a list of subjects).

### Example: A List of Dictionaries
```python
students_list = [
    {"name": "John", "age": 20, "marks": 85},
    {"name": "Alice", "age": 19, "marks": 92},
    {"name": "Bob", "age": 21, "marks": 78}
]

# Print the second student's name
print(students_list[1]["name"])  # Alice

# Loop through all students
for s in students_list:
    print(f"Student: {s['name']} scored {s['marks']}%")
```

---

## Practice Tasks
Navigate to the [tasks/](./tasks/) folder to complete today's assignments:
* [Task 1: Create Student Record](./tasks/task1_student_record.py)
* [Task 2: Access Data](./tasks/task2_access_data.py)
* [Task 3: Update Data](./tasks/task3_update_data.py)
* [Task 4: Multiple Students](./tasks/task4_multiple_students.py)
* [Task 5: Search Student](./tasks/task5_search_student.py)
