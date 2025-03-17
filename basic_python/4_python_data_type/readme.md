# 🐍 Python Data Types

## 📌 Introduction
Python has various **built-in data types** used to store different kinds of values. This guide covers numeric types, sequences, mappings, and more.

---

## 🔢 Numeric Data Types
Python supports three main numeric types:

- **Integer (`int`)** – Whole numbers.
- **Float (`float`)** – Decimal or floating-point numbers.
- **Complex (`complex`)** – Numbers with a real and imaginary part.

```python
number_1 = 10000024  # 🔢 Integer
number_2 = 3.14  # 🔢 Float
number_3 = 120 + 3j  # 🔢 Complex
```

---

## 📝 String Data Type (`str`)
A string is a sequence of characters enclosed in quotes.

```python
string_1 = "hello python"  # 📜 Single-line string using double quotes
string_2 = '''Hello\nPython'''  # 📜 Multi-line string using triple single quotes
```

---

## ✅ Boolean Data Type (`bool`)
Boolean values can either be `True` or `False`.

```python
bool_1 = True  # ✅ Boolean True
bool_2 = False  # ❌ Boolean False
```

---

## ⚪ None Data Type (`None`)
Represents an empty or undefined value, similar to `null` in other languages.

```python
data = "hello"
print(data)  # Output: hello

data = None
print(data)  # Output: None
```

---

## 📋 List Data Type (`list`)
A **list** is an ordered collection that can contain different data types.

```python
list_1 = [2, 4, 8, 16]  # 🔢 List of integers
list_2 = ["grayson", "jason", "tim", "damian"]  # 🧑 List of strings
list_3 = [24, False, "Hello Python"]  # 🔀 Mixed data types

print(list_1[2])  # Output: 8
```

---

## 🔒 Tuple Data Type (`tuple`)
A **tuple** is similar to a list but immutable (cannot be modified after creation).

```python
tuple_1 = (2, 3, 4)  # 🔢 Tuple of integers
tuple_2 = ("numenor", "valinor")  # 🌍 Tuple of strings
tuple_3 = (24, False, "Hello Python")  # 🔀 Mixed data types

print(tuple_1[2])  # Output: 4
```

---

## 🔑 Dictionary Data Type (`dict`)
A **dictionary** stores data in key-value pairs.

```python
profile_1 = {
    "name": "Noval",
    "is_male": False,
    "age": 16,
    "hobbies": ["gaming", "learning"]
}

print("name: %s" % (profile_1["name"]))  # Output: name: Noval
print("hobbies: %s" % (profile_1["hobbies"]))  # Output: hobbies: ["gaming", "learning"]
```

---

## 🎯 Set Data Type (`set`)
A **set** is a collection of **unique elements**. Sets do not maintain order and cannot be accessed using an index.

```python
set_1 = {"pineapple", "spaghetti"}
print(set_1)  # Output: {'pineapple', 'spaghetti'}
```

---

## 📌 Other Data Types
Additional Python data types include:
- **`frozenset`** – Immutable version of a set.
- **`bytes`** – Immutable byte sequences.
- **`memoryview`** – Access buffer memory directly.
- **`range`** – Generates a sequence of numbers.

These will be covered in separate chapters. 🚀

---

## ✨ Summary
✅ Python provides various data types for handling different types of values.\
✅ Lists and tuples store ordered collections, while sets store unique elements.\
✅ Dictionaries use key-value pairs.\
✅ `None` represents an empty value.\
✅ Use appropriate data types for optimal code performance.

🚀 **Happy Coding!** 🐍🎉