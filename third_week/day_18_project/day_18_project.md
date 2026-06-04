# Day 18: Mini Project – To-Do List App

Welcome to Day 18! Today you will build a real-world application: a **Command Line To-Do List App**. 
This project combines logic, file handling, and JSON to create an app that saves your tasks permanently.

---

## The Project: To-Do List Application

You will build an interactive program that continuously asks the user what they want to do until they choose to exit. Crucially, the tasks must be saved to a `tasks.json` file so they are not lost when the program closes.

### Core Features

1. **Add Task**
   - Prompt the user for a task description.
   - Store it as a dictionary: `{"task": "Buy groceries", "completed": False}`.
   - Add it to the main list and save to the JSON file.

2. **View Tasks**
   - Read from the JSON file.
   - Loop through the list and print tasks nicely.
   - Example format: `1. [ ] Buy groceries` (if incomplete) or `2. [X] Study Python` (if complete).

3. **Mark Complete**
   - Ask the user for the task number to mark as complete.
   - Update the dictionary's `"completed"` status to `True`.
   - Save the updated list back to the JSON file.

4. **Delete Task**
   - Ask the user for the task number to delete.
   - Remove it from the list.
   - Save the updated list back to the JSON file.

5. **Persistent Storage**
   - When the program starts, it should try to load existing tasks from `tasks.json`.
   - If the file doesn't exist yet, it should start with an empty list.

---

## Program Structure

We will use functions to keep the code modular and clean.

```python
import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    # Try to load tasks from file, return [] if file doesn't exist

def save_tasks(tasks):
    # Save the tasks list to the JSON file

def add_task(tasks):
    # Ask for input, append to tasks, call save_tasks()

def view_tasks(tasks):
    # Loop and print tasks nicely

def mark_complete(tasks):
    # Update a task's status, call save_tasks()

def delete_task(tasks):
    # Remove a task by index, call save_tasks()

def main():
    # Load tasks once at the start
    tasks = load_tasks()
    
    # Run the menu loop
    while True:
        # Show menu
        # Get choice
        # Call appropriate function
```

---

## Bonus Features (For stronger students)

If you finish the core project easily, try adding these features:

1. **Priority levels**: Add a `"priority": "High"` key when creating a task. Sort tasks by priority when viewing.
2. **Due dates**: Ask for a date and store it `"due": "2026-10-15"`.
3. **Search task**: Add an option to search for a specific word in tasks.
4. **Prevent duplicates**: Don't allow the user to add the exact same task twice.

---

## Deliverables
Navigate to the [tasks/](./tasks/) folder to complete today's assignment:
* [To-Do List App](./tasks/todo_app.py)
