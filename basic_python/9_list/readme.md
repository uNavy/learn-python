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

🖥️ **Output:**

```
[1, 2, 3, 4, 5]
```

```python
# List of Strings
fruits = ['apple', 'banana', 'cherry']  
print(fruits)
```

🖥️ **Output:**

```
['apple', 'banana', 'cherry']
```

```python
# Mixed Data Type List
diverse_list = [42, 'hello', 3.14, True]  
print(diverse_list)
```

🖥️ **Output:**

```
[42, 'hello', 3.14, True]
```

```python
# Empty List
empty_list = []  
print(empty_list)
```

🖥️ **Output:**

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

🖥️ **Output:**

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

🖥️ **Output:**

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

🖥️ **Output:**

```
8
```

---

## ⚙️ List Operations – Manipulating Lists

### 🔍 Accessing Elements by Index

```python
print(my_list[2])
```

🖥️ **Output:**

```
30
```

### 🔎 Checking if an Element Exists

```python
print(3 in my_list)
```

🖥️ **Output:**

```
False
```

### ✂️ Slicing Lists

```python
print(my_list[1:3])
```

🖥️ **Output:**

```
[20, 30]
```

### 🔄 Modifying Elements

```python
my_list[0] = 99
print(my_list)
```

🖥️ **Output:**

```
[99, 20, 30]
```

### ➕ Adding Elements

```python
my_list.append(6)  
print(my_list)
```

🖥️ **Output:**

```
[99, 20, 30, 6]
```

```python
my_list.extend([7, 8, 9])  
print(my_list)
```

🖥️ **Output:**

```
[99, 20, 30, 6, 7, 8, 9]
```

```python
my_list.insert(2, 100)  
print(my_list)
```

🖥️ **Output:**

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

🖥️ **Output:**

```
[99, 100, 6, 7, 8, 9]
```

```python
my_list.clear()  
print(my_list)
```

🖥️ **Output:**

```
[]
```

### 🔢 Finding Elements

```python
my_list = [10, 20, 30, 40, 50]
print(my_list.index(30))
```

🖥️ **Output:**

```
2
```

### 🔃 Reversing & Sorting

```python
my_list.reverse()
print(my_list)
```

🖥️ **Output:**

```
[50, 40, 30, 20, 10]
```

```python
my_list.sort()
print(my_list)
```

🖥️ **Output:**

```
[10, 20, 30, 40, 50]
```

```python
my_list.sort(reverse=True)
print(my_list)
```

🖥️ **Output:**

```
[50, 40, 30, 20, 10]
```

---

# 🎯 List Comprehension – Efficient List Creation

List comprehensions provide a **concise and efficient** way to create lists in Python. They allow for compact and readable code, making them preferable over traditional loops.

### 🚀 Simple List Comprehension
A basic example of list comprehension:

```python
squares = [x**2 for x in range(10)]  # Generate squares from 0 to 9
print(squares)
```

**Output:**
```
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```
This is more **efficient** and **readable** compared to using a standard `for` loop.

### 🔥 More Examples of List Comprehension

#### 1️⃣ Generate a sequence by multiplying each number by 2

⚙️ **Without List Comprehension**:
```python
seq = []
for i in range(5):
    seq.append(i * 2)
print(seq)
```

✅ **With List Comprehension**:
```python
seq = [i * 2 for i in range(5)]
print(seq)
```
**Output:**
```
[0, 2, 4, 6, 8]
```



#### 2️⃣ Filtering with conditions (Odd numbers only)


⚙️ **Without List Comprehension**:
```python
seq = []
for i in range(10):
    if i % 2 == 1:
        seq.append(i)
print(seq)
```

✅ **With List Comprehension**:
```python
seq = [i for i in range(10) if i % 2 == 1]
print(seq)
```
**Output:**
```
[1, 3, 5, 7, 9]
```


#### 3️⃣ Applying different operations based on conditions


⚙️ **Without List Comprehension**:
```python
seq = []
for i in range(1, 10):
    if i % 2 == 0:
        seq.append(i * 2)
    else:
        seq.append(i * 3)
print(seq)
```

✅ **With List Comprehension**:
```python
seq = [(i * (2 if i % 2 == 0 else 3)) for i in range(1, 10)]
print(seq)
```
**Output:**
```
[3, 4, 9, 8, 15, 12, 21, 16, 27]
```


#### 4️⃣ Combining two lists

⚙️ **Without List Comprehension**:
```python
seq = []
for x in list_x:
    for y in list_y:
        seq.append(x + y)
print(seq)
```

✅ **With List Comprehension**:
```python
list_x = ['a', 'b', 'c']
list_y = ['1', '2', '3']
seq = [x + y for x in list_x for y in list_y]
print(seq)
```
**Output:**
```
['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
```

#### 5️⃣ Transposing a matrix using list comprehension



⚙️ **Without List Comprehension**:
```python
transposed = []
for i in range(4):
    row = []
    for each in matrix:
        row.append(each[i])
    transposed.append(row)
print(transposed)
```
✅ **With List Comprehension**:
```python
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
transposed = [[row[i] for row in matrix] for i in range(4)]
print(transposed)
```
**Output:**
```
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```

### 🔍 Key Differences:
- **Readability:** List comprehension condenses multiple lines of code into a single, more readable expression.
- **Performance:** List comprehensions are generally faster than `for` loops because they are optimized for execution.
- **Memory Efficiency:** They generate lists directly instead of repeatedly calling `.append()`, which can be slightly more efficient.

By using list comprehensions, you can write cleaner and more efficient Python code! 🚀

### 🏆 Why Use List Comprehensions?
✅ **Concise** – Reduces multiple lines of code into one  
✅ **Faster Execution** – More optimized than traditional loops  
✅ **Readability** – Easier to understand at a glance  

Using list comprehensions can significantly improve your code efficiency while keeping it **clean and readable**!

---

## ✨ Summary

🎯 **Lists store multiple data types** dynamically.\
🔄 **Looping techniques** like `enumerate()` improve efficiency.\
📦 **Nested lists** allow multi-dimensional structures.\
⚙️ **List operations** include slicing, modifying, and sorting.\
🚀 **List comprehension** simplifies list creation.

🔥 **Happy Coding!** 🐍✨

