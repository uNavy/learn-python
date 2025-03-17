# ✅ INTRODUCTION TO LISTS 📜
my_list = [1, 2, 3, 4, 5]  # A SIMPLE LIST CONTAINING NUMBERS
string_list = ['apple', 'banana', 'cherry']  # LIST OF STRINGS
diverse_list = [42, 'hello', 3.14, True]  # LIST WITH MIXED DATA TYPES
empty_list = []  # AN EMPTY LIST

# ANOTHER LIST EXAMPLE
list_1 = [10, 70, 20]

# VERTICAL LIST
list_2 = [
    'ab',
    'cd',
    'hi',
    'ca'
]

# LIST WITH MIXED DATA TYPE
list_3 = [3.14, 'hello python', True, False]

# EMPTY LIST
list_4 = []

# ✅ LOOPING THROUGH LISTS 🔄
# FUNCTION enumerate()
for index, value in enumerate(my_list):
    print(f"INDEX: {index}, VALUE: {value}\n")  # ENUMERATE GIVES INDEX & VALUE
    # OUTPUT EXAMPLE:
    # INDEX: 0, VALUE: 1
    # INDEX: 1, VALUE: 2
    # INDEX: 2, VALUE: 3
    # INDEX: 3, VALUE: 4
    # INDEX: 4, VALUE: 5
# LOOPING USING A SIMPLE FOR LOOP
for item in string_list:
    print(f"FRUIT: {item}\n")  # PRINT EACH ELEMENT
    # OUTPUT EXAMPLE:
    # FRUIT: apple
    # FRUIT: banana
    # FRUIT: cherry
    

# ✅ NESTED LISTS 📦
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # LIST INSIDE ANOTHER LIST
# OUTPUT: 8

print(nested_list[2][1])  # ACCESSING ELEMENT FROM NESTED LIST

# ✅ FUNCTION list()
# CONVERTING range TO list
range_list = list(range(5))  # CONVERT RANGE TO LIST
# range_list= [0, 1, 2, 3, 4]

# CONVERTING string TO list
char_list = list("hello")  # CONVERT STRING TO LIST OF CHARACTERS
# char_list= ['h', 'e', 'l', 'l', 'o']

# CONVERTING tuple TO list
tuple_list = list((1, 2, 3, 4, 5))  # CONVERT TUPLE TO LIST
# tuple_list= [1, 2, 3, 4, 5]

# ✅ LIST OPERATIONS ⚙️
# ACCESSING ELEMENT VIA INDEX
print(my_list[2])  # GET ELEMENT AT INDEX 2
# OUTPUT: 3


# CHECKING IF ELEMENT EXISTS
print(3 in my_list)  # RETURNS TRUE IF 3 EXISTS
# OUTPUT: True

# SLICING LIST
print(my_list[1:4])  # SLICE LIST FROM INDEX 1 TO 3
# OUTPUT: [2, 3, 4]

# MODIFYING ELEMENT VALUE
my_list[0] = 99  # CHANGE FIRST ELEMENT TO 99

# APPENDING ELEMENT
my_list.append(6)  # ADD 6 TO THE END OF LIST

# EXTENDING/ CONCATENATING/ UNION ELEMENTS
my_list.extend([7, 8, 9])  # ADD MULTIPLE ELEMENTS TO LIST

# INSERTING ELEMENT AT INDEX i
my_list.insert(2, 100)  # INSERT 100 AT INDEX 2

# REMOVING ELEMENT
my_list.remove(3)  # REMOVE ELEMENT 3 FROM LIST

# REMOVING ELEMENT AT INDEX i
del my_list[1]  # DELETE ELEMENT AT INDEX 1

# REMOVING ELEMENTS WITHIN A RANGE
del my_list[1:3]  # DELETE ELEMENTS FROM INDEX 1 TO 2

# COUNTING ELEMENTS IN LIST
print(len(my_list))  # PRINT LENGTH OF LIST
# OUTPUT: 6

# FINDING INDEX OF ELEMENT IN LIST
print(my_list.index(5))  # GET INDEX OF VALUE 5
# OUTPUT: 1

# EMPTYING LIST
my_list.clear()  # REMOVE ALL ELEMENTS

# REVERSING LIST ORDER
my_list = [1, 2, 3, 4, 5]
my_list.reverse()  # REVERSE ORDER OF ELEMENTS

# COPYING LIST
copy_list = my_list.copy()  # CREATE A COPY OF LIST

# SORTING LIST
my_list.sort()  # SORT LIST IN ASCENDING ORDER


# SORTING LIST IN DESCENDING ORDER
my_list.sort(reverse=True)  # SORT LIST IN DESCENDING ORDER


# CREATING A LIST OF LISTS
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # MULTIDIMENSIONAL LIST


# LIST COMPREHENSION TO CREATE A LIST OF SQUARES
squares = [x**2 for x in range(10)]  # GENERATE SQUARES FROM 0 TO 9
