# 🐍 For Loop & Range in Python 🚀  

## 📌 Introduction  
A **for loop** is used to iterate over a sequence (list, tuple, dictionary, set, or string). The **range()** function generates a sequence of numbers, often used as a loop counter. 🎯  

---  

## 🔄 Basic For Loop Using Range  
This loop runs **5 times**, iterating from `0` to `4`.  

```python
for i in range(5):
    print("🔢 Index:", i)
```

The following loop takes **user input** to determine the range:  

```python
for i in range(int(input("✏️ Enter a number: "))):
    print("🔢 Index:", i)
```

---  

## 📋 Converting Range to a List  
The `range()` function produces a **range object**, which can be converted to a list.  

```python
r = range(5)
print("📜 Range as list:", list(r))  # Output: [0, 1, 2, 3, 4]
```

---  

## 🎯 Using Range with Start & Stop  
`range(start, stop)` generates numbers from `start` to `stop - 1`.  

```python
for i in range(1, 4):
    print("🔢 Index:", i)  # Output: 1, 2, 3
```

---  

## ⏭️ Using Range with Step  
`range(start, stop, step)` increments values by `step`.  

```python
for i in range(1, 10, 3):
    print("🔢 Index:", i)  # Output: 1, 4, 7
```

---  

## 🔄 Equivalent For Loops  
The following loops produce the **same output**:  

```python
for i in range(3):
    print("🔢 Index:", i)
for i in range(0, 3):
    print("🔢 Index:", i)
for i in range(0, 3, 1):
    print("🔢 Index:", i)
```

---  

## 🔙 Using Range with Negative Step  
Counting **backward** from `5` to `-4`.  

```python
for i in range(5, -5, -1):
    print("🔢 Index:", i)
```

---  

## 📑 Iterating Over Different Data Types  

### 📋 Iterating Over a List  
```python
messages = ["🌞 Morning", "🌆 Afternoon", "🌙 Evening"]
for m in messages:
    print(m)
```

### 🔢 Iterating Over a Tuple  
```python
numbers = ("🔟 Ten", 10)
for n in numbers:
    print(n)
```

### 🔠 Iterating Over a String  
```python
for char in "🐍 Python":
    print(char)  # Outputs each character
```

### 📜 Iterating Over a Dictionary  
```python
bio = {"🚗 Car": "Toyota Camry", "📅 Year": 1993}
for key in bio:
    print("🔑 Key:", key, "➡️ Value:", bio[key])
```

### 🔢 Iterating Over a Set  
```python
numbers = {"♾️ Infinity", 24}
for n in numbers:
    print(n)
```

---  

## 🌟 Nested For Loops  
Creates a **pattern of stars** decreasing in each row.  

```python
max_stars = int(input("✏️ Enter number of stars: "))
for i in range(max_stars):
    for j in range(0, max_stars - i):
        print("⭐", end=" ")  # Prints stars in the same line
    print()  # Moves to a new line after each row
```

---  

### ✨ Summary  
✅ **For loops** are used to iterate over sequences.  
✅ **Range()** generates a sequence of numbers.  
✅ **Start, stop, and step** define the range of iteration.  
✅ **Looping** through lists, tuples, dictionaries, sets, and strings is easy with `for`.  
✅ **Nested loops** help create patterns.  

🎉 **Happy Coding!** 🚀🐍💡

