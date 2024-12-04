
# List Operator +
# + is the concatenation operator
# Used to combine lists together

# Example: Concatenation
list1 = [2, 4]
list2 = [3, 5]
print(list1 + list2)  # Output: [2, 4, 3, 5]

# Concatenation Examples
# List and list
list1 = [1, 2]
list2 = [3, 4]
print(list1 + list2)  # Output: [1, 2, 3, 4]

# Assignment
list1 = []
list1 = list1 + [3, 4]
print(list1)  # Output: [3, 4]

# List and empty list
list1 = []
list2 = [3, 4]  # Fixed assignment
print(list1 + list2)  # Output: [3, 4]

# List within a list
list1 = [1, 2, [2] + [3, 4]]  # Concatenating [2] and [3, 4] within the main list
print(list1)  # Output: [1, 2, [2, 3, 4]]

# List Operator [:]
# [:] is the slice operator
# It is used to extract a slice from a list.
# The result is a list containing values between two indices specified
# before and after `:` within `[]`.

# Example: From index 1 to 4 (excluding index 4)
list1 = [1, 2, 3, 4, 5]
sliced_list = list1[1:4]  # Create a new list with elements from index 1 to 3
print(sliced_list)  # Output: [2, 3, 4]

# Print the original list
print(list1)  # Output: [1, 2, 3, 4, 5]

# Slice Examples:
# From index 1 to 4 (excluding index 4)
print(list1[1:4])  # Output: [2, 3, 4]

# From the start to index 4 (excluding index 4)
print(list1[:4])  # Output: [1, 2, 3, 4]

# From index 1 to the end
print(list1[1:])  # Output: [2, 3, 4, 5]

# Access a specific element by index
print(list1[2])  # Output: 3

#List Operator *
#* is the replication operator
# #Used to duplicate the elements of a list
# Operator is used between a list and an int
# Result is a list containing several copies of the elements of the
# original list. Number of copies depends on the int value
#Example Result
list1 = ["a", "b"]
list1 * 2
#result ["a", "b", "a", "b"]

#Replication Examples
#List of ints
list1 = [1,2]
print(list1 * 3)

#List of empty lists
list1 = [[]]
print(list1 * 3)

#Empty list
list1 = []
print(list1 *3)

#List within a list
list1 = [[1]]
list1[0] = list1[0] *2
print((list1 * 3))

#---------------------------List Operator IN
#List Operator IN --.Used to check if a value is found in a list
#Operator is used between a variable of any
#type and a list
#Result is a Boolean value
#True if the value is found in the list
#False if the value is not found in the list
#Example Result

list1 = [9, 8, 7, 6]
print(6 in list1)
#True

#IN Examples
#String in a list
list1 = ["a", "b", "c",]
str1 = "a"
print(str1 in list1)

#List in a list
list1 = [[1]]
list2 = [1]
print(list2 in list1)

#Sum in a list
list1 = [4,3,6]
print(2+2 in list1)

#Empty string in an empty list
list1 = []
str1 =""
print(str1 in list1)

#List Operator NOT IN
#Used to check if a value is not in a list
#Operator is used between a variable of any
#type and a list
#Result is a Boolean value
#True if the value is not found in the list
#False if the value is found in the list
#Example Result
list1 = [9, 8, 7, 6]
6 not in list1

#NOT IN Examples
#String not in a list
list1 = ["a", "b","c"]
print(str1 not in list1)

#List not in a list
list1 = [[1]]
list2 = [2]
print((list2 not in list1))

#Product not in a list
list1 = [4,2,6]
num1 = 2*3
print(num1 not in list1)

#Empty string not in an empty list
list1 = []
str1 = ""
print(str1 not in list1)

#Try It Yourself
#Enter and run the following statements
#in the python environment:
list1 = [2, 3]
list2 = [4]
print(list1 + list2 * 2)

list5 = [1, 2, 3, 4, 5]
if 2 in list5:
  print(list5[3:4] * 4)

list4 = [1, 2, 3, 4, 5]
list4 = list4[3:]
print(1 not in list4)

list3 = [1, 2, 3, 4, 5]
list3 = list3[3:]
print(1 in list3)
