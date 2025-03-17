# 🔄 Loop Control Statements in Python 🚀  

## 📌 Introduction  
This guide covers **loop control statements** in Python:  

⚙️ **Break Statement** 🛑 – Terminates a loop when a condition is met.  
⚙️ **Continue Statement** 🔄 – Skips the current iteration and moves to the next one.  
⚙️ **Simulating Labeled Loops** 🎯 – Using flags to control nested loops.  

---

## 🛑 Break Statement – Stopping a Loop Based on a Condition  
A `while` loop can run **indefinitely** until a condition forces it to stop.  
In this example, the loop continues **until the user enters a number that is not divisible by 3**.  

```python
while True:
    n = int(input("ENTER A NUMBER DIVISIBLE BY 3: "))  # User input
    
    if n % 3 != 0:
        break  # Terminates the loop when the number is not divisible by 3
    
    print(f"{n} IS DIVISIBLE BY 3")  # Confirmation if the number is valid
```

🔹 The loop will only break if the input **is NOT divisible by 3**.  

---

## 🔄 Continue Statement – Skipping an Iteration Based on a Condition  
The `continue` statement **skips the rest of the loop body** and moves to the next iteration.  

This example iterates from `0` to `9`, but **skips values** less than `3` or greater than `7`.  

```python
for i in range(10):
    if i < 3 or i > 7:
        continue  # Skips the current iteration
    
    print(i)  # Prints numbers from 3 to 7 (3, 4, 5, 6, 7)
```

🔹 Values **less than 3** and **greater than 7** are ignored.  

---

## 🎯 Simulating a Labeled Loop Using a Flag Variable  
Python **does not support labeled loops**, but **flags** can control nested loops.  

This example prints a **star pattern** while **limiting the number of stars per row to 8**.  

```python
max_rows = int(input("Number of Stars: "))  # User input
continue_outer_loop = True  # Flag to control the outer loop

for current_row in range(max_rows):  # Outer loop
    if not continue_outer_loop:
        break  # Exit the outer loop if the flag is False

    for current_star_count in range(current_row + 1):  # Inner loop
        print("*", end=" ")  # Print stars on the same line
        
        if current_star_count >= 7:  # Limit stars per row to 8
            continue_outer_loop = False  # Set flag to False to stop the outer loop
            break  # Exit inner loop when reaching 8 stars
    
    print()  # Move to the next line
```

🔹 The **inner loop stops at 8 stars**, and the **outer loop terminates when the flag is False**.  

---

## 🛠 Debugging a Labeled Loop Simulation  
This version includes **debugging messages** to track loop behavior.  

```python
max_rows = int(input("Number of Stars: "))  
continue_outer_loop = True  

print("\nDEBUG: Starting the outer loop...\n")

for rows in range(max_rows):  
    print("\nDEBUG: Outer Loop Continue:", continue_outer_loop)
    
    if not continue_outer_loop:
        print("\nDEBUG: Outer loop stopped. Exiting...\n")
        break  

    print(f"DEBUG: Current row -> {rows}")
    star_row = ""  

    for columns in range(rows + 1):  
        print(f"DEBUG: Printing star {columns + 1} in row {rows}")
        star_row += "* "  

        if columns >= 7:  
            continue_outer_loop = False  
            print("DEBUG: Star limit reached (8 stars). Flag set to False. Breaking inner loop...\n")
            break  
    
    print(star_row)  

print("\nDEBUG: Program execution completed.\n")
```

🔹 The debug logs show exactly **when and why** the loops stop.  

---

## 🔁 Nested Loops with Break & Continue  
This example demonstrates **nested loops controlled by user input**.  

```python
print("\nDEBUG: Starting outer loop...\n")

while True:  # Outer loop
    user_input = input("Loop 1 - Enter command (break/continue): ").strip().lower()

    if user_input == "break":
        print("DEBUG: 'break' command received in outer loop. Program stops.\n")
        break  # Exit all loops

    elif user_input == "continue":
        print("DEBUG: 'continue' command received in outer loop. Entering inner loop...\n")

        while True:  # Inner loop
            print("Running in inner loop")
            nested_input = input("Loop 2 - Enter command (break/continue): ").strip().lower()

            if nested_input == "break":
                print("DEBUG: 'break' command received in inner loop. Returning to outer loop...\n")
                break  # Exit inner loop

            elif nested_input == "continue":
                print("DEBUG: 'continue' command received in inner loop.\n")
                continue  # Skip to next iteration of inner loop

            print(f"DEBUG: Inner loop continues. Input: {nested_input}\n")

    print("DEBUG: Outer loop still running...\n")
```

🔹 **User input controls when the loops continue or stop.**  

---

## ✨ Summary
✅ **Break** stops a loop when a condition is met.  
✅ **Continue** skips the current iteration and moves to the next one.  
✅ **Flags** can be used to simulate labeled loops.  
✅ **Debugging messages** help track loop behavior.  

🚀 **Happy Coding!** 🐍🔥

