#Set Data Type
#Sets are created using curly brackets {}, as opposed to lists which are defined using square brackets [] around the elements
# Sets will only contain unique values Repeated values are added only once in the set my-set1 = {1,2,3,1,3,3,1}
#Example Result
my_set1 = {1, 2, 3, 1, 3, 3, 1}
print(my_set1)

#Making a Set from a Sequence
# set() – is used to convert a sequence into a set
#] Works on lists and tuples
# Example Result
my_set2 = set([10, 20, 30, 30])
print(my_set2)

my_set3 = set(("a", "b", "b", "a"))
print(my_set3)

#Making a Sequence from a Set
#list(), tuple() – used to convert a set into a list or tuple respectively
#Example Result
my_set4 = {10, 20, 30, 10}
my_list1 = list(my_set4)
print(my_set4)
print(my_list1)

my_set5 = {10, 20, 30, 10}
print(my_set5)

My_tuple1 = tuple(my_set5)
print(My_tuple1)

my_set2 = set([10, 20, 30, 30])
print(my_set2)

my_set3 = set(("a", "b", "b", "a"))
print(my_set3)

#Making a Sequence from a Set
#list(), tuple() – used to convert a set into a list or tuple respectively
#Example Result
my_set4 = {10, 20, 30, 10}
my_list1 = list(my_set4)
print(my_set4)
print(my_list1)

my_set5 = {10, 20, 30, 10}
print(my_set5)

My_tuple1 = tuple(my_set5)
print(My_tuple1)

#Examples
#Creating a set
set1 = {"a","a","b","a"}
print(set1)

#Tuple to a set
tuple1 = (1,2,2,3,5)
set2 = set(tuple1)
print(set2)

#Removing duplicates from a list
list1 = [11,23,11,42,51,11]
set3 = set(list1)
list2 = list(set3)
print(list2)

#Try It Yourself
#Write a program in Python environment that takes 10 inputs, stores them in a list and removes any duplicates.
#Hint: use the input() function inside a FOR loop, which repeats 10 times
# Append elements into a list, then
#convert to a set and convert back

#Use a FOR loop to iterate over a tuple and print each element
# Define the tuple
list8 = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10")

# Iterate over the tuple and print each element
for t in list8:
    print(t)  # Print each individual element

