# Day 17: Object-Oriented Programming (OOP) Basics

Welcome to Day 17! Today we learn about **OOP**. Object-Oriented Programming is a paradigm (a way of writing code) that allows us to model real-world things as **Objects**.

---

## 1. Classes and Objects

*   **Class**: A blueprint or template. It defines the properties and behaviors that a certain type of object should have. (e.g., A blueprint for a Car).
*   **Object**: An instance built from that blueprint. (e.g., A specific Red Toyota Corolla).

### Syntax:
```python
class Student:
    # Class body goes here
    pass

# Creating an object (an instance of the class)
student1 = Student()
```

---

## 2. The `__init__` Method (The Constructor)

The `__init__` method is a special function that runs automatically every time you create a new object. It is used to initialize the object's attributes (variables).

```python
class Student:
    # The __init__ method
    def __init__(self, name, marks):
        self.name = name   # Attribute
        self.marks = marks # Attribute

# Creating objects
student1 = Student("John", 85)
student2 = Student("Alice", 92)

# Accessing attributes
print(student1.name)  # Output: John
print(student2.marks) # Output: 92
```

> **What is `self`?** 
> `self` refers to the specific object being created or used. When we say `self.name = name`, it means "Set THIS specific student's name to the name passed in".

---

## 3. Methods (Functions inside a Class)

Methods are simply functions that belong to a class. They define what an object can *do*. 
The first parameter of any method in a class must always be `self`.

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    # A method to display details
    def display_details(self):
        print(f"Student Name: {self.name}")
        print(f"Marks Scored: {self.marks}")

    # A method with logic
    def check_pass_fail(self):
        if self.marks >= 40:
            return "Pass"
        else:
            return "Fail"

student1 = Student("John", 85)

# Calling methods
student1.display_details()
print(f"Result: {student1.check_pass_fail()}")
```

---

## 4. Why Use OOP?

1.  **Organization**: Groups related data (attributes) and behaviors (methods) together.
2.  **Reusability**: You can create 100 student objects easily from one `Student` class.
3.  **Real-World Modeling**: It maps perfectly to how we think about things in real life (A Bank Account has a balance, and you can deposit or withdraw from it).

---

## Practice Tasks
Navigate to the [tasks/](./tasks/) folder to complete today's assignments:
* [Task 1: Create Class](./tasks/task1_create_class.py)
* [Task 2: Object Creation](./tasks/task2_object_creation.py)
* [Task 3: Method](./tasks/task3_method.py)
* [Task 4: Calculator Class](./tasks/task4_calculator_class.py)
* [Task 5: Bank Account Challenge](./tasks/task5_bank_account.py)
