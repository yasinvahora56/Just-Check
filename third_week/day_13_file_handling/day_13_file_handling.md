# Day 13: File Handling

Welcome to Day 13! Today we learn about **File Handling**. Real-world applications need to save data so it isn't lost when the program closes. We achieve this by reading from and writing to files on our computer.

---

## 1. Opening and Closing Files

To work with a file in Python, you first need to open it using the built-in `open()` function. When you are done, you should always `close()` it.

### Syntax:
```python
file = open("filename.txt", "mode")
# ... do something with the file ...
file.close()
```

---

## 2. File Modes

The "mode" tells Python what you want to do with the file.

| Mode | Name | Description |
| :--- | :--- | :--- |
| `"r"` | **Read** | Default mode. Opens a file for reading. Returns an error if the file doesn't exist. |
| `"w"` | **Write** | Opens a file for writing. **Overwrites** the file if it exists. Creates a new file if it doesn't. |
| `"a"` | **Append** | Opens a file for appending. **Adds** new data to the end of the file. Creates a new file if it doesn't. |

---

## 3. The `with` Statement (Best Practice)

Instead of manually calling `file.close()`, it is highly recommended to use the `with` statement. It automatically closes the file for you, even if an error occurs.

```python
with open("data.txt", "w") as file:
    file.write("Hello World!")
# No need to call file.close() here!
```

---

## 4. Writing to a File (`"w"` mode)

Writing to a file will create the file if it doesn't exist, or **completely overwrite** it if it does.

```python
with open("user.txt", "w") as file:
    file.write("Name: John\n") # \n adds a new line
```

---

## 5. Reading from a File (`"r"` mode)

You can read the entire content of a file, or read it line by line.

```python
# Read entire file
with open("user.txt", "r") as file:
    content = file.read()
    print(content)

# Read line by line (great for large files)
with open("user.txt", "r") as file:
    for line in file:
        print(line.strip()) # strip() removes the hidden newline character
```

---

## 6. Appending to a File (`"a"` mode)

If you want to keep the old data and just add new information at the bottom, use append mode.

```python
with open("user.txt", "a") as file:
    file.write("Name: Rahul\n")
```

---

## Practice Tasks
Navigate to the [tasks/](./tasks/) folder to complete today's assignments:
* [Task 1: Write to File](./tasks/task1_write_file.py)
* [Task 2: Read from File](./tasks/task2_read_file.py)
* [Task 3: Append Data](./tasks/task3_append_data.py)
* [Task 4: Store Multiple Entries](./tasks/task4_multiple_entries.py)
* [Task 5: Simple Logger](./tasks/task5_simple_logger.py)
