# 📜 Mastering Python Lists 🚀

## 📌 Introduction

This guide covers **Python lists**, including:

📋 **Creating Lists** – Different ways to define lists.\
🔄 **Looping Through Lists** – Iterating over list elements efficiently.\
📦 **Nested Lists** – Handling lists inside lists.\
⚙️ **List Operations** – Accessing, modifying, and manipulating lists.

---

## 📋 Creating Lists – Different Types of Lists

Python lists can store multiple data types and structures:

```python
# Basic List of Numbers
my_list = [1, 2, 3, 4, 5]  
print(my_list)
```

**Output:**

```
[1, 2, 3, 4, 5]
```

```python
# List of Strings
fruits = ['apple', 'banana', 'cherry']  
print(fruits)
```

**Output:**

```
['apple', 'banana', 'cherry']
```

```python
# Mixed Data Type List
diverse_list = [42, 'hello', 3.14, True]  
print(diverse_list)
```

**Output:**

```
[42, 'hello', 3.14, True]
```

```python
# Empty List
empty_list = []  
print(empty_list)
```

**Output:**

```
[]
```

---

## 🔄 Looping Through Lists – Iterating Efficiently

### 🎯 Using `enumerate()` – Getting Index & Value

```python
my_list = [10, 20, 30]

for index, value in enumerate(my_list):
    print(f"INDEX: {index}, VALUE: {value}\n")
```

**Output:**

```
INDEX: 0, VALUE: 10
INDEX: 1, VALUE: 20
INDEX: 2, VALUE: 30
```

---

### 🔨 Using a Simple `for` Loop

```python
string_list = ['apple', 'banana', 'cherry']

for item in string_list:
    print(f"FRUIT: {item}\n")
```

**Output:**

```
FRUIT: apple
FRUIT: banana
FRUIT: cherry
```

---

## 📦 Nested Lists – Lists Inside Lists

Lists can contain other lists, forming **multi-dimensional structures**.

```python
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  
print(nested_list[2][1])
```

**Output:**

```
8
```

---

## ⚙️ List Operations – Manipulating Lists

### 🔍 Accessing Elements by Index

```python
print(my_list[2])
```

**Output:**

```
30
```

### 🔎 Checking if an Element Exists

```python
print(3 in my_list)
```

**Output:**

```
False
```

### ✂️ Slicing Lists

```python
print(my_list[1:3])
```

**Output:**

```
[20, 30]
```

### 🔄 Modifying Elements

```python
my_list[0] = 99
print(my_list)
```

**Output:**

```
[99, 20, 30]
```

### ➕ Adding Elements

```python
my_list.append(6)  
print(my_list)
```

**Output:**

```
[99, 20, 30, 6]
```

```python
my_list.extend([7, 8, 9])  
print(my_list)
```

**Output:**

```
[99, 20, 30, 6, 7, 8, 9]
```

```python
my_list.insert(2, 100)  
print(my_list)
```

**Output:**

```
[99, 20, 100, 30, 6, 7, 8, 9]
```

### ❌ Removing Elements

```python
my_list.remove(30)  # If 30 exists in the list
print(my_list)
```

```python
del my_list[1]  
print(my_list)
```

**Output:**

```
[99, 100, 6, 7, 8, 9]
```

```python
my_list.clear()  
print(my_list)
```

**Output:**

```
[]
```

### 🔢 Finding Elements

```python
my_list = [10, 20, 30, 40, 50]
print(my_list.index(30))
```

**Output:**

```
2
```

### 🔃 Reversing & Sorting

```python
my_list.reverse()
print(my_list)
```

**Output:**

```
[50, 40, 30, 20, 10]
```

```python
my_list.sort()
print(my_list)
```

**Output:**

```
[10, 20, 30, 40, 50]
```

```python
my_list.sort(reverse=True)
print(my_list)
```

**Output:**

```
[50, 40, 30, 20, 10]
```

---

## 🎯 List Comprehension – Efficient List Creation

List comprehensions provide a **concise way** to create lists.

```python
squares = [x**2 for x in range(10)]  
print(squares)
```

**Output:**

```
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

⚡ This is **faster** and **more readable** than traditional loops.

---

## ✨ Summary

🎯 **Lists store multiple data types** dynamically.\
🔄 **Looping techniques** like `enumerate()` improve efficiency.\
📦 **Nested lists** allow multi-dimensional structures.\
⚙️ **List operations** include slicing, modifying, and sorting.\
🚀 **List comprehension** simplifies list creation.

🔥 **Happy Coding!** 🐍✨

