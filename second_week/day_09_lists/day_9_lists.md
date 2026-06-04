# Day 9: Lists

Welcome to Day 9! Today we learn about **Lists**. A list is Python's built-in way to store a collection of items in a single variable. Lists are ordered, changeable (mutable), and allow duplicate values.

---

## 1. Creating and Accessing Lists

A list is created by placing items inside square brackets `[]`, separated by commas.

```python
# Lists can store any data type (and even mixed types)
fruits = ["apple", "banana", "cherry"]
numbers = [10, 20, 30, 40, 50]
mixed_list = ["John", 25, 85.5, True]
empty_list = []
```

### List Indexing:
Just like strings, lists use **zero-based indexing** to access elements.

```
List:    ["apple", "banana", "cherry"]
Index:       0         1         2
Negative:   -3        -2        -1
```

```python
fruits = ["apple", "banana", "cherry"]

print(fruits[0])   # 'apple'
print(fruits[2])   # 'cherry'
print(fruits[-1])  # 'cherry' (last element)
```

---

## 2. Modifying Lists (Lists are Mutable)

Unlike strings, you can change individual items in a list directly.

```python
fruits = ["apple", "banana", "cherry"]
fruits[1] = "blueberry"  # Change index 1 from 'banana' to 'blueberry'
print(fruits)  # ['apple', 'blueberry', 'cherry']
```

---

## 3. Common List Operations and Methods

Python has several built-in methods to manipulate lists.

### Adding Elements:
- `append(item)`: Adds an element to the **end** of the list.
- `insert(index, item)`: Adds an element at a **specific position**.

```python
numbers = [1, 2, 3]

numbers.append(4)
print(numbers)  # [1, 2, 3, 4]

numbers.insert(1, 99)  # Insert 99 at index 1
print(numbers)  # [1, 99, 2, 3, 4]
```

### Removing Elements:
- `remove(value)`: Removes the **first occurrence** of a specific value.
- `pop(index)`: Removes and returns the element at the **given index** (or the last one if no index is given).
- `clear()`: Removes **all** elements.

```python
fruits = ["apple", "banana", "cherry", "banana"]

fruits.remove("banana")  # Removes the first 'banana'
print(fruits)  # ['apple', 'cherry', 'banana']

popped_item = fruits.pop(1)  # Removes 'cherry' at index 1
print(popped_item)  # 'cherry'
print(fruits)  # ['apple', 'banana']
```

### Other Helpful Operations:
- `len(list)`: Get the size of the list.
- `in`: Check if an item exists in the list.
- `sort()`: Sorts the list in ascending order.
- `reverse()`: Reverses the elements of the list in-place.

```python
nums = [40, 10, 30, 20]
print(len(nums))  # 4
print(50 in nums)  # False (50 is not in list)

nums.sort()
print(nums)  # [10, 20, 30, 40]

nums.reverse()
print(nums)  # [40, 30, 20, 10]
```

---

## 4. Looping Through a List

There are two main ways to loop through a list:

### Method 1: Iterating directly through items (Preferred)
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

### Method 2: Iterating through indices using `range()` and `len()`
Use this if you need to know the index number of each item.
```python
fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
    print(f"Index {i} has {fruits[i]}")
```

---

## 5. List Slicing
Slicing works exactly the same way as strings.
```python
nums = [0, 1, 2, 3, 4, 5]
print(nums[1:4])  # [1, 2, 3] (index 1 to 3)
print(nums[:3])   # [0, 1, 2] (start to index 2)
print(nums[3:])   # [3, 4, 5] (index 3 to end)
```

---

## Practice Tasks
Navigate to the [tasks/](./tasks/) folder to complete today's assignments:
* [Task 1: Create List](./tasks/task1_create_list.py)
* [Task 2: Find Max and Min](./tasks/task2_max_min.py)
* [Task 3: Sum of List](./tasks/task3_sum_list.py)
* [Task 4: Remove Duplicates](./tasks/task4_remove_duplicates.py)
* [Task 5: Search Element](./tasks/task5_search_element.py)
