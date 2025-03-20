# PYTHON TUPLE - IMPORTANT NOTES & EXAMPLES

# TUPLE VS LIST
# - TUPLE IS IMMUTABLE (CANNOT BE CHANGED AFTER CREATION), WHILE LIST IS MUTABLE (CAN BE MODIFIED).
# - TUPLE USES () OR CAN BE WRITTEN WITHOUT PARENTHESES, WHILE LIST USES [].
# - TUPLE ELEMENTS CAN BE DUPLICATED AND CAN CONTAIN DIFFERENT DATA TYPES.

# EXAMPLES OF TUPLE DECLARATION
x = ()  # EMPTY TUPLE
x = tuple()  # EMPTY TUPLE USING tuple() FUNCTION
x = (1, True, "h", 2, 1)  # TUPLE WITH MULTIPLE DATA TYPES
x = 1, True, "h", 2, 1  # TUPLE WITHOUT PARENTHESES

# EXAMPLES OF LIST DECLARATION
x = []  # EMPTY LIST
x = list()  # EMPTY LIST USING list() FUNCTION
x = [1, True, "h", 2, 1]  # LIST WITH MULTIPLE DATA TYPES

# ACCESSING TUPLE ELEMENTS USING INDEX
example_tuple = (2, 3, 4, "hello python", False)
print("ELEMENT 0:", example_tuple[0])  # OUTPUT: 2
print("ELEMENT 1:", example_tuple[1])  # OUTPUT: 3

# INDEX ERROR EXAMPLE (ACCESSING NON-EXISTENT INDEX WILL RAISE AN ERROR)
# print("ELEMENT 5:", example_tuple[5])  # UNCOMMENTING THIS WILL CAUSE IndexError

# LOOPING THROUGH A TUPLE
example_tuple = ('ultra instinct shaggy', 'nightwing', 'noob saibot')
for element in example_tuple:
    print(element)

# LOOPING USING INDEX
for i in range(len(example_tuple)):
    print("INDEX:", i, "ELEMENT:", example_tuple[i])

# USING ENUMERATE() TO GET INDEX & VALUE
for i, value in enumerate(example_tuple):
    print("INDEX:", i, "ELEMENT:", value)

# CHECKING IF AN ELEMENT EXISTS IN A TUPLE
example_tuple = (10, 70, 20)
n = 70
if n in example_tuple:
    print(n, "EXISTS IN THE TUPLE")
else:
    print(n, "DOES NOT EXIST IN THE TUPLE")

# NESTED TUPLE (TUPLE INSIDE A TUPLE)
nested_tuple = ((0, 2), (0, 3), (2, 2), (2, 4))
for row in nested_tuple:
    for cell in row:
        print(cell, end=" ")
    print()

# COMBINATION OF LIST AND TUPLE
data = [
    ("ultra instinct shaggy", 1, True, ['detective', 'saiyan']),
    ("nightwing", 3, True, ['teen titans', 'bat family']),
]

# APPENDING A NEW TUPLE TO A LIST
data.append(("noob saibot", 6, False, ['brotherhood of shadow']))
data.append(("tifa lockhart", 2, True, ['avalanche']))

# PRINTING LIST OF TUPLES
print("NAME | RANK | WIN | AFFILIATION")
print("------------------------------")
for row in data:
    for cell in row:
        print(cell, end=" | ")
    print()

# CONVERTING STRING TO TUPLE
alphabets = tuple("abcdefgh")
print(alphabets)  # OUTPUT: ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')

# CONVERTING LIST TO TUPLE
numbers = tuple([2, 3, 4, 5])
print(numbers)  # OUTPUT: (2, 3, 4, 5)

# CONVERTING RANGE TO TUPLE
r = range(0, 3)
rtuple = tuple(r)
print(rtuple)  # OUTPUT: (0, 1, 2)

# TUPLE PACKING (COMBINING MULTIPLE VARIABLES INTO A SINGLE TUPLE)
first_name = "aerith gainsborough"
rank = 11
win = False
row_data = (first_name, rank, win)
print(row_data)  # OUTPUT: ('aerith gainsborough', 11, False)

# TUPLE UNPACKING (EXTRACTING ELEMENTS FROM A TUPLE INTO SEPARATE VARIABLES)
row_data = ('aerith gainsborough', 11, False)
first_name, rank, win = row_data
print(first_name, rank, win)  # OUTPUT: aerith gainsborough 11 False

# EMPTY TUPLE (REPRESENTING A COLLECTION THAT CAN BE EMPTY)
empty_tuple = ()
print(empty_tuple)  # OUTPUT: ()

# SAMPLE DATA WITH AN EMPTY TUPLE
sample_data = [
    ("ultra instinct shaggy", 1, True, ('detective', 'saiyan')),
    ("nightwing", 3, True, ('teen titans', 'bat family')),
    ("cat meow", 7, False, ()),  # EMPTY AFFILIATION
]
