# 🐍 Python Variables

## 📌 Introduction
In programming, a **variable** is a container for values stored in memory. This guide covers Python variable declaration, naming conventions, and assignment operations.

---

## 🏷️ Variable Declaration
Python allows declaring variables directly using the **assignment operator (`=`)**.

```python
name = "Navy"  # 📝 STRING
hobby = 'Gym'  # 🏋️‍♂️ STRING
age = 18  # 🔢 INTEGER
male = True  # ✅ BOOLEAN
```

---

## 🖥️ Displaying Variables
Use the `print()` function to display variable values.

```python
print("==== 🆔 BIODATA ====")
print("name: %s" % (name))  # %s is used for STRING formatting
print("hobby: %s, age: %d, male: %r" % (hobby, age, male))  # %d for INTEGER, %r for BOOLEAN
```

🔹 **Example Output:**
```
==== 🆔 BIODATA ====
name: Navy
hobby: Gym, age: 18, male: True
```

---

## 🏗️ Variable Naming Conventions
Following **PEP 8**, variables should use **snake_case**.

```python
message = 'hello, good morning'  # ✅ PROPER NAMING EXAMPLE
exam_score = 99.2  # 🔢 FLOAT
```

🚫 **Bad Example:**
```python
Message = "wrong"  # ❌ Avoid using uppercase for variable names
examscore = 85.5  # ❌ Harder to read, missing underscore
```

---

## 🔄 Updating Variables
Python allows updating variables after declaration.

```python
name = "Navy Git"  # ✏️ Updated Name
age = 21  # 🔢 Age updated
```

---

## 🏷️ Declaring Explicit Data Types
Python allows **explicit type annotations** for better code clarity.

```python
name: str = "Navy"
hobby: str = 'Gym'
age: int = 18
male: bool = True
exam_score: float = 99.2
```

---

## 🎯 Declaring Multiple Variables in One Line
Python supports **multiple variable declarations in a single line**.

```python
value1, value2, value3, value4 = 24, 25, 26, 21
```

---

## 📊 Calculating the Average
You can perform arithmetic operations on variables.

```python
average_value = (value1 + value2 + value3 + value4) / 4
print("average score: %f" % (average_value))  # 🎯 Display FLOAT value using %f
```

🔹 **Example Output:**
```
average score: 24.000000
```

---

### ✨ Summary
✅ Variables store values in memory. \
✅ Use `snake_case` for variable names.\
✅ Variables can be updated and explicitly typed.\
✅ Declare multiple variables in one line.\
✅ Perform calculations using variables.

🚀 **Happy Coding!** 🐍🎉