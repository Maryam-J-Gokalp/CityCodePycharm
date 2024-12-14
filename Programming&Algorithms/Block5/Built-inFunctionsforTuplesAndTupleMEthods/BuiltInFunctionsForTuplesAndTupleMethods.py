# Built-in Functions for Tuples I
# min(tuple_name) – used to find an element with the smallest value in the #tuple
#Example Result
from pickletools import string1

tuple1 = (1, 2, 3)
min(tuple1)

tuple2 = (1, 2, 3)
max(tuple2)

#Built-in Functions for Tuples II
#len(tuple_name) – used to find the length (number of elements) of a tuple
#sum(list_name) – used to find the sum of all elements in a list (add together their values)
#Example Result
tuple3 = (1, 2, 3)
len(tuple3)

tuple4 = (1, 2, 3)
sum(tuple4)


#Examples I
# Minimum value
tuple1 = ("a", "b", "c", "d")
print(min(tuple1))  # Finds the smallest value alphabetically

# Length of a tuple
tuple3 = ("a", "b", "c", "d")
print(len(tuple3))  # Prints the number of elements in the tuple

# Maximum value
tuple2 = ("a", "b", "c", "d")
print(max(tuple2))  # Finds the largest value alphabetically

# Sum of the tuple
tuple4 = (1, 2, 3, 4, 5)
print(sum(tuple4))  # Sums up the numbers in the tuple

#Tuple Methods
#count(value) – used to count the number of times a value appears in a tuple
#index(value) – used to find the index of a value in a tuple
#Example Result
tuple5 = (1, 2, 3)
tuple5.count(2)  # Returns the number of times the value '2' appears in the tuple

tuple6 = (1, 2, 3)
tuple6.index(1)  # Returns the index of the first occurrence of the value '1'

#Making a Tuple from a List
#tuple() – used to convert a sequence to a tuple
#Example Result
list1 = [1, 2, 3]
tuple(list1)
print(list1)

#Examples II
# Index of the largest value
tuple7 = (3, 5, 1, 6, 2)
print(tuple7.index(max(tuple7)))  # Finds the index of the largest value in tuple7

# Average value of the tuple
tuple8 = (3, 5, 1, 6, 2)
print(sum(tuple8) / len(tuple8))  # Calculates the average value of tuple8

# String to tuple
str1 = "tuple"
print(tuple(str1))  # Converts the string "tuple" into a tuple of characters

#Examples III
# Number of instances
tuple5 = (1, 2, 3, 2, 1)
print(tuple5.count(2))  # Counts the number of times the value 2 appears in tuple5

# List to tuple
list1 = [1, 2, 3, 4, 5]
print(tuple(list1))  # Converts the list into a tuple

# Finding the index
tuple6 = (1, 2, 3, 4, 5)
print(tuple6.index(4))  # Finds the index of the value 4 in tuple6

# Try It Yourself
# Enter and run the following statements in the python environment:
list1 = [1.5, 2, 14]
tuple1 = tuple(list1)
print(min(tuple1))  # Finds the smallest value in tuple1

tuple4 = ([3, 4], [2, 28])
print(max(tuple4))  # Finds the largest element in tuple4 based on lexicographical order

tuple5 = (1, 2, (1, 2))
tuple6 = (1, 2)
print(tuple5.count(tuple6))  # Counts the number of times tuple6 appears in tuple5

tuple2 = (1, "b", True)
tuple3 = (tuple2, 1)
print(tuple3.index(1))  # Finds the index of the value 1 in tuple3
