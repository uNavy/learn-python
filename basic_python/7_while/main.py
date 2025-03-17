# KEYWORD WHILE
# WHILE LOOPS EXECUTE AS LONG AS A CONDITION IS TRUE
# THIS LOOP CONTINUES UNTIL THE USER ENTERS AN ODD NUMBER OR A NUMBER LESS THAN OR EQUAL TO 0
should_continue = True

while should_continue:
    n = int(input("ENTER AN EVEN NUMBER GREATER THAN 0: "))
    
    if n <= 0 or n % 2 == 1:
        print(n, "IS NOT AN EVEN NUMBER GREATER THAN 0")
        should_continue = False  # STOP THE LOOP IF THE CONDITION IS MET
    else:
        print("NUMBER:", n)

# WHILE LOOP CONTROLLED BY A LOGICAL OPERATION
# THIS LOOP PRINTS NUMBERS FROM 0 TO N-1
n = int(input("ENTER MAX DATA: "))
i = 0

while i < n:
    print("NUMBER", i)
    i += 1  # INCREMENT COUNTER

# INCREMENT AND DECREMENT IN PYTHON
# PYTHON DOES NOT SUPPORT ++ OR -- OPERATORS
# INCREMENT: i += 1 IS EQUIVALENT TO i = i + 1
# DECREMENT: i -= 1 IS EQUIVALENT TO i = i - 1

# FOR VS WHILE
# THE SAME LOOP CAN BE WRITTEN USING FOR
n = int(input("ENTER MAX DATA: "))

for i in range(n):
    print("NUMBER", i)

# NESTED WHILE LOOP
# THIS CREATES A PATTERN USING A NESTED WHILE LOOP
n = int(input("ENTER MAX DATA: "))
i = 0

while i < n:
    j = 0
    while j < n - i:
        print("*", end=" ")  # PRINTS STARS IN THE SAME LINE
        j += 1
    print()  # MOVES TO THE NEXT LINE
    i += 1

# COMBINATION OF FOR AND WHILE
# THIS MODIFIES THE NESTED LOOP TO USE A COMBINATION OF FOR AND WHILE
n = int(input("ENTER MAX DATA: "))

for i in range(n):
    j = 0
    while j < n - i:
        print("*", end=" ")
        j += 1
    print()
