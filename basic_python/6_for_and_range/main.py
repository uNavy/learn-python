# FOR LOOP & RANGE IN PYTHON
# A for loop is used to iterate over a sequence (list, tuple, dictionary, set, or string).
# The range() function generates a sequence of numbers, often used as a loop counter.

# BASIC FOR LOOP USING RANGE
# This loop runs 5 times, iterating from 0 to 4
#%%
for i in range(5):
    print("index:", i)
#%%
for i in range(int(
    input("Enter a number: ")
    )):
    print("index:", i)

#%%
# CONVERTING RANGE TO A LIST
# The range() function produces a range object, which can be converted to a list
r = range(5)
print("r:", list(r))  # Converts range(0, 5) to a list [0, 1, 2, 3, 4]
#%%
# USING RANGE WITH START AND STOP
# range(start, stop) generates numbers from 'start' to 'stop - 1'
for i in range(1, 4):
    print("index:", i)  # Output: 1, 2, 3

#%%
# USING RANGE WITH STEP
# range(start, stop, step) increments values by 'step'
for i in range(1, 10, 3):
    print("index:", i)  # Output: 1, 4, 7
#%%
# EQUIVALENT FOR LOOPS
# The following three loops produce the same output
for i in range(3):
    print("index:", i)
for i in range(0, 3):
    print("index:", i)
for i in range(0, 3, 1):
    print("index:", i)

#%%

# USING RANGE WITH NEGATIVE STEP
# Counting backward from 5 to -4
for i in range(5, -5, -1):
    print("index:", i)

# ITERATING OVER A LIST
# The for loop iterates over each element in the list
messages = ["morning", "afternoon", "evening"]
for m in messages:
    print(m)  # Output: morning, afternoon, evening

# ITERATING OVER A TUPLE
# Similar to lists, for loops can iterate over tuples
numbers = ("twenty four", 24)
for n in numbers:
    print(n)  # Output: "twenty four", 24

# ITERATING OVER A STRING
# Iterates over each character in the string
for char in "hello python":
    print(char)  # Outputs each character individually

# ITERATING OVER A DICTIONARY
# Iterates through dictionary keys, retrieving corresponding values
bio = {"name": "toyota camry", "year": 1993}
for key in bio:
    print("key:", key, "value:", bio[key])

# ITERATING OVER A SET
# Since sets are unordered, output order may vary
numbers = {"twenty four", 24}
for n in numbers:
    print(n)

# NESTED FOR LOOPS
# Creates a pattern of stars decreasing in each row
max_stars = int(input("Enter number of stars: "))
for i in range(max_stars):
    for j in range(0, max_stars - i):
        print("*", end=" ")  # Prints stars in the same line
    print()  # Moves to a new line after each row
# %%
