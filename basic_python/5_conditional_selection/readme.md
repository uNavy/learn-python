# 🐍 Conditional Selection in Python 🚀  

## 📌 Introduction  
Conditional selection is a block of code that **executes only when a specified criterion is met**. 🎯

---

## ✅ If Statement  
The `if` keyword is used to execute a **block of code** only if a specific condition is `True`.  

```python
grade = 100

if grade == 100:
    print("🎉 PERFECT")

if grade == 90:
    print("👍 OK")
    print("💪 KEEP WORKING HARD!")
```

---

## 📏 Indentation Block  
In Python, a block of code is **indicated by indentation** (four spaces recommended by PEP 8).  

```python
if grade == 90:
    print("👍 OK")
    print("💪 KEEP WORKING HARD!")
```

---

## 🔀 Elif Statement  
`elif` (short for **else if**) allows additional **conditional checks** after `if`.  

```python
str_input = input("✏️ ENTER YOUR GRADE: ")
grade = int(str_input)

if grade == 100:
    print("🎉 PERFECT")
elif grade >= 85:
    print("🔥 AWESOME")
elif grade >= 65:
    print("✅ PASSED THE EXAM")
```

---

## ⌨️ Input Function  
The `input()` function prompts the **user for input** and returns a string value.  

### 🔄 Type Conversion  
`int()` converts a **string** to an **integer**.  

```python
str_input = input("✏️ ENTER YOUR GRADE: ")
grade = int(str_input)
print("📥 USER INPUT:", grade, type(grade))
```

---

## 🔚 Else Statement  
The `else` statement executes a **block of code** if none of the previous conditions are met.  

```python
if grade == 100:
    print("🎉 PERFECT")
elif grade >= 85:
    print("🔥 AWESOME")
elif grade >= 65:
    print("✅ PASSED THE EXAM")
else:
    print("❌ BELOW THE PASSING GRADE")
```

---

## 🔄 Nested Conditionals  
Conditional statements can be **nested** within other conditionals.  

```python
if grade == 100:
    print("🎉 PERFECT")
elif grade >= 85:
    print("🔥 AWESOME")
elif grade >= 65:
    print("✅ PASSED THE EXAM")
    if grade <= 70:
        print("⚠️ BUT YOU NEED TO IMPROVE IT!")
    else:
        print("👌 WITH OK GRADE")
else:
    print("❌ BELOW THE PASSING GRADE")
```

---

## 🔗 Logical Operators in Conditionals  
`and`, `or`, and `not` can be used in **conditional statements**.  

```python
grade = int(input("✏️ ENTER YOUR CURRENT GRADE: "))
prev_grade = int(input("📊 ENTER YOUR PREVIOUS GRADE: "))

if grade >= 90 and prev_grade >= 65:
    print("🔥 AWESOME")
if grade >= 90 and prev_grade < 65:
    print("🔥 AWESOME. YOU DEFINITELY WORKED HARD, RIGHT?")
elif grade >= 65:
    print("✅ PASSED THE EXAM")
else:
    print("❌ BELOW THE PASSING GRADE")

if (grade >= 65 and not prev_grade >= 65) or (not grade >= 65 and prev_grade >= 65):
    print("👏 AT LEAST YOU PASSED ONE EXAM. GOOD JOB!")
```

---

## ⚡ One-Line Conditionals  
Single-line `if` statements for **simple conditionals**.  

```python
if grade >= 65: print("✅ PASSED THE EXAM")
if grade < 65: print("❌ BELOW THE PASSING GRADE")
```

---

## 🎭 Ternary Operator  
```python
print("✅ PASSED THE EXAM") if grade >= 65 else print("❌ BELOW THE PASSING GRADE")
```

### 📥 Ternary Operator with Variable Assignment  
```python
message = "✅ PASSED THE EXAM" if grade >= 65 else "❌ BELOW THE PASSING GRADE"
print(message)
```

---

## 🔍 Pattern Matching  
`match` and `case` can be used for **advanced pattern matching**. 🎭  
For more details, refer to the chapter on **Pattern Matching**. 📖

---

### ✨ Summary
✅ **if** statement executes a block of code only if the condition is **True**.  
✅ **elif** allows additional conditional checks.  
✅ **else** executes a block if no previous conditions are met.  
✅ Logical operators (and, or, not) enhance conditional logic.  
✅ Nested conditionals allow more complex checks.  
✅ One-line conditionals make code concise.  
✅ Ternary operators simplify conditional assignments.  
✅ Pattern matching is useful for structured conditions.

---

🎉 **Happy Coding!** 🐍🚀💡

