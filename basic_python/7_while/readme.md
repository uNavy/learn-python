# 🔄 While Loop in Python 🐍🚀

## 📌 Introduction  
A **while loop** repeatedly executes a block of code as long as a **specified condition is `True`**. 🔁

---

## ✅ Basic While Loop  
A `while` loop continues executing until the condition becomes `False`.

```python
should_continue = True

while should_continue:
    n = int(input("✏️ ENTER AN EVEN NUMBER GREATER THAN 0: "))
    
    if n <= 0 or n % 2 == 1:
        print(n, "❌ IS NOT AN EVEN NUMBER GREATER THAN 0")
        should_continue = False  # 🛑 STOP THE LOOP
    else:
        print("✅ NUMBER:", n)
```

---

## 🔢 While Loop with a Counter  
A while loop that prints numbers from `0` to `n-1`.  

```python
n = int(input("✏️ ENTER MAX DATA: "))
i = 0

while i < n:
    print("📊 NUMBER:", i)
    i += 1  # 🔺 Increment counter
```

---

## ⬆️ Increment and ⬇️ Decrement  
Python **does not support** `++` or `--` operators. Instead, use:  
✅ `i += 1` (equivalent to `i = i + 1`)  
✅ `i -= 1` (equivalent to `i = i - 1`)  

---

## 🔁 For Loop vs While Loop  
The same loop can be written using a `for` loop:  

```python
n = int(input("✏️ ENTER MAX DATA: "))

for i in range(n):
    print("📊 NUMBER:", i)
```

---

## 🏗️ Nested While Loop  
Creates a **pattern of stars** using a **nested while loop**. 🌟

```python
n = int(input("✏️ ENTER MAX DATA: "))
i = 0

while i < n:
    j = 0
    while j < n - i:
        print("⭐", end=" ")  # Print stars in the same line
        j += 1
    print()  # Move to the next line
    i += 1
```

---

## 🔄 Combining For and While  
A **for loop** can be combined with a **while loop** for flexibility.  

```python
n = int(input("✏️ ENTER MAX DATA: "))

for i in range(n):
    j = 0
    while j < n - i:
        print("⭐", end=" ")
        j += 1
    print()
```

---

### ✨ Summary  
✅ **While loop executes as long as the condition is True.**  
✅ **Use logical conditions to control the loop.**  
✅ **Python does not support `++` or `--`, use `+=` or `-=` instead.**  
✅ **`for` loop is used when the number of iterations is known, `while` is more flexible.**  
✅ **Nested loops can be used to create patterns.**  
✅ **For and while loops can be combined for complex iterations.**  

🚀 **Happy Coding!** 🐍🔥

