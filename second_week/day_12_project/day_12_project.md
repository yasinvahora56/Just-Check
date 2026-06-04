# Day 12: Mini Project – Contact Manager

Welcome to Day 12! Today is the final day of Week 2. You will combine everything you have learned this week (Loops, Strings, Lists, Dictionaries, and Functions) to build a fully functional **Command Line Interface (CLI) Contact Manager**.

This is a real-world application structure where data is stored in memory while the program runs.

---

## The Project: Contact Manager App

You will build an interactive program that continuously asks the user what they want to do until they choose to exit.

### Core Features

1. **Add Contact**
   - Prompt the user for a `name` and `phone` number.
   - Store this information as a dictionary `{"name": name, "phone": phone}`.
   - Add this dictionary to a global `contacts` list.

2. **View Contacts**
   - Loop through the `contacts` list.
   - Print each contact nicely formatted: `Name - Phone`.
   - If the list is empty, display a message like "No contacts found."

3. **Search Contact**
   - Ask the user for a name to search.
   - Loop through the `contacts` list to find a match (case-insensitive is best!).
   - If found, print the contact details.
   - If not found, print "Contact not found."

4. **Delete Contact**
   - Ask the user for a name to delete.
   - Search the list. If found, remove the dictionary from the list.
   - Print a success message.

5. **Menu Driven Program**
   - Use a `while` loop to keep the program running.
   - Show a menu with options 1 to 5.
   - Option 5 should exit the program.

---

## Program Structure (Modular Design)

Instead of writing all code in one huge block, we will use **Functions** for each feature.

```python
# Global list to store data
contacts = []

def add_contact():
    # Logic to add

def view_contacts():
    # Logic to view

def search_contact():
    # Logic to search

def delete_contact():
    # Logic to delete

# Main Loop
while True:
    print("1. Add Contact")
    # ... print other options
    choice = input("Enter choice: ")
    
    if choice == '1':
        add_contact()
    elif choice == '5':
        break # Exit loop
```

---

## Bonus Enhancements (For stronger students)

If you finish the core project easily, try adding these features:

1. **Store contacts in a file**: So data isn't lost when the program closes (Hint: look up Python `json` module or simple file I/O).
2. **Prevent duplicate entries**: Before adding, check if the name already exists.
3. **Add email field**: Store `"email"` along with name and phone.
4. **Sort contacts**: When viewing, sort the list alphabetically by name.

---

## Deliverables
Navigate to the [tasks/](./tasks/) folder to complete today's assignment:
* [Contact Manager App](./tasks/contact_manager.py)
