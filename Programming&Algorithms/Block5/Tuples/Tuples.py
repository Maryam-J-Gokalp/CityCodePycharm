# Tuple Data Type
# § Tuples are created using parenthesis (), as
# opposed to lists which are defined using
# square brackets [] around the elements
# § Examples:
# # my_tuple1 contains 3 elements of type int
# my_tuple1 = (1, 2, 3)
# # my_tuple2 contains 3 elements of type int, string and float
# my_tuple2 = (4, "apples", 4.5)
from doctest import Example

#Accessing Elements in Tuples
# Like in lists, elements are indexed:
# 0 is the index of the first element position
# 1 is the index of the second element position
# Tuple length - 1 (or just -1) is the index of the last element position
# Tuple elements can be accessed by using the tuple name followed by the index of the element inside the [ ]
# my_tuple2[0] returns 4
# my_tuple2[1] returns "apples"
# my_tuple2[-1] returns 4.5

# Example |
#A tuple is like a box that holds several things, in this case, numbers. Once you put items in the tuple, you can't change them later.
tuple1 = (1,2,3)  #tuple1 = (1, 2, 3) creates a tuple named tuple1 with the numbers 1, 2, and 3.
print(tuple1)  # shows everything inside the box: (1, 2, 3).

tuple2 = (1,2, 3)
print(tuple2[-1])  #Numbers in a tuple have positions, starting from 0 for the first item. Position 0 → 1 Position 1 → 2 Position 2 → 3
# [-1] means "get the last item in the tuple." So, print(tuple2[-1]) will show 3.

tuple3 = (1,2, 3)
print(tuple3[0])  #[0] means "get the first item in the tuple. In this case, tuple3[0] refers to the first number in the tuple, which is 1.
#So, print(tuple3[0]) will display 1.

# Common Errors in Python
#Tuples are immutable: once created, position and value of an element cannot change
tuple4 = (1, 2, 3)

# Convert the tuple to a list to allow modification
list4 = list(tuple4)
list4[1] += 1

# Convert the list back to a tuple
tuple4 = tuple(list4)
print(tuple4)

#Examples III
#tuple with Single element tuple
tuple5 = ("a",)
print(tuple5)

# Lists inside a tuple as elements
tuple7 = ("a", ["b", "c"])
print(tuple7)       # Prints the entire tuple: ('a', ['b', 'c'])
print(tuple7[1])    # Accesses the second element, which is the list: ['b', 'c']


#Tuples as elements
tuple6 = (1, (2, 3))
print(tuple6)       # Prints the entire tuple: (1, (2, 3))
print(tuple6[1])    # Accesses the second element, which is another tuple: (2, 3)


# Accessing an element of a tuple element
tuple8 = (("a", 2), 5)
print(tuple8[0])      # Accesses the first element: ('a', 2)
print(tuple8[0][0])   # Accesses the first element of the nested tuple ('a', 2), which is 'a'


#Try It Yourself
#Enter and run the following statementsin the python environment:
#Tuple Sum:

# Tuple Sum
# Tuple Example
tuple1 = (5, 7)
sum_value = sum(tuple1)  # Calculate the sum of tuple1
print(f"Sum of tuple1: {sum_value}")

# Tuple with a list inside
tuple4 = ([9, 3],)
print(f"First element of tuple4: {tuple4[0]}")
print(f"Last element of tuple4: {tuple4[-1]}")

# Nested Tuples
tuple3 = ((1, 2, 3), 4)
print(f"Second element of tuple3: {tuple3[1]}")
print(f"Second element of the nested tuple in tuple3: {tuple3[0][1]}")

# Conditional Check with Tuple
tuple2 = ("apple", 3.5)
if tuple2[0] == "apple":
    print(f"Second element of tuple2: {tuple2[1]}")

# Accessing a Nested Tuple
tuple8 = (("a", 2), 5)
print(tuple8[0])      # Accesses the first element: ('a', 2)
print(tuple8[0][0])   # Accesses the first element of the nested tuple, 'a'
