#Set Data Type
#Sets are created using curly brackets {}, as opposed to lists which are defined using square brackets [] around the elements
#Sets will only contain unique values

#Example
my_set1 = {1,2,3,1,3,3,1}
print(my_set1)

#Making a Set from a Sequence
# set() – is used to convert a sequence into a set
#Works on lists and tuples
my_set2 = set([10, 20, 30, 30])
print(my_set2)

my_set3 = set(("a", "b", "b", "a"))
print(my_set3)

#Examples
#Creating a set
set1 = {"a", "a", "b", "a"}  #will remove duplicate "a", leaving only
print(set1)

# Tuple to a set
tuple1 = (1,1,2,3,5)   #Converting it to a set with set2 = set(tuple1) removes the duplicate, resulting in {1, 2, 3, 5}.
set2 = set(tuple1)
print(set2)

#Removing duplicates from a list
list1 = [11,23,11,42,51,11]   #Converting it to a set (set3 = set(list1)) removes duplicates, resulting in {11, 23, 42, 51}.
set3 = set(list1)
list2 = list(set3)
print(list2)

# Try It Yourself
# Write a program in Python environment
# that takes 10 inputs, stores them in a list
# and removes any duplicates.
# Hint: use the input() function inside a
# FOR loop, which repeats 10 times
# Append elements into a list, then
# convert to a set and convert back
# Create an empty list to store inputs
# List with names, including duplicates
list10 = ["Joao", "Joao", "Pedro", "Marco", "To", "Maria", "Luzia", "Francisco", "Joana", "Tozinho", "Lulu"]

# Remove duplicates by converting to a set and back to a list
unique_list = list(set(list10))

# Print the unique list
print("List without duplicates:", unique_list)

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