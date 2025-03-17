# 🐍 Python Constants

## 📌 Introduction
A **constant** is a variable whose value is set once and cannot be changed. Python does not have built-in support for constants, but we use naming conventions and type hints to indicate their immutability.

---

## 🔖 Declaring Constants
Python constants are typically written in **UPPER_CASE** following **PEP 8** guidelines. We use `Final` from the `typing` module to indicate a variable should not be modified.

```python
from typing import Final

PI: Final = 3.14  # 🔢 FLOAT CONSTANT
TOTAL_MONTH: Final[int] = 12  # 🗓️ INTEGER CONSTANT
```

---

## 🖥️ Displaying Constants
Use the `print()` function to output constant values.

```python
print("pi: %f" % (PI))
print("total months in a year: %d" % (TOTAL_MONTH))
```

🔹 **Example Output:**
```
pi: 3.140000
total months in a year: 12
```

---

## 🏗️ Using Constants in Calculations
Constants can be used for mathematical operations, such as calculating the area of a circle.

```python
radius = 7  # 🎯 Radius of the circle
circle_area = PI * radius ** 2
print("circle area: %f" % (circle_area))
```

🔹 **Example Output:**
```
circle area: 153.860000
```

---

## ✨ Summary
✅ Use **UPPER_CASE** for constants following **PEP 8**.\
✅ Use `Final` from `typing` to indicate constants.\
✅ Constants can be used in calculations but should not be reassigned.\
✅ Use `print()` to display constant values.

🚀 **Happy Coding!** 🐍🎉