#Elements form the unsorted part are inserted into the correct positions in the sorted part.
#Insertion Sort
#Insertion sort algorithm splits the list into sorted part and unsorted part.
from os.path import split


# Tracing the behaviour of the Insertion Sort
# Initially, the sorted sub-list contains the first element in the list.
# 50 | 3 | 15 | 8 | 31 | 26

#Tracing the Bahaviour of the Insertion Sort
# 50 | 3 | 15 | 8 | 31 | 26

# The sorted sub-list is [50] Insert 3 into the list

# Tracing the Behaviour of the Insertion Sort
# 3 | 50 | 15 | 8 | 31 | 26
# The sorted sub-list is [3, 50] Insert 15 into the list

#--------------------------------------------------------------->
# Insertion Sort Algorithm
#1. n = len(list)
#2. for i in range(n-1)
#3. j = i
#4. while j > 0 and list[j-1] > list[j] do
#5. temp = list[j]
#6. list[j] = list[j-1]
#7. list[j-1] = temp
#8. j = j - 1

# Insertion Sort Example
def insertion_sort(list1):

#    This function sorts the list using the insertion sort algorithm.

    n = len(list1)
    for i in range(1, n):  # Start from index 1
        j = i
        while j > 0 and list1[j - 1] > list1[j]:  # Compare adjacent elements
            # Swap elements
            list1[j], list1[j - 1] = list1[j - 1], list1[j]
            j -= 1  # Move to the previous index

# Input from the user
input_string = input("Enter your numbers, separated by spaces, then press enter: ")
split_input = input_string.split()
numbers = [int(n) for n in split_input]  # Convert input to integers

# Sort the list using insertion_sort
insertion_sort(numbers)

# Output the sorted list
print("Sorted list:", numbers)


#------------------------------------------------->
#Try It Yourself
#Write a program in python environment that
#takes a string as an input and sorts in
#alphabetical order using the insertion sort
#algorithm above

def insertion_sort_string(chars):
    """
    Sorts a list of characters alphabetically using the insertion sort algorithm.
    """
    for i in range(1, len(chars)):
        key = chars[i]
        j = i - 1
        while j >= 0 and chars[j] > key:
            chars[j + 1] = chars[j]
            j -= 1
        chars[j + 1] = key


# Get user input as a string
user_input = input("Please enter a string: ")

# Convert the input string into a list of characters
character_list = list(user_input)

# Apply insertion sort to the list of characters
insertion_sort_string(character_list)

# Join the sorted list back into a string
sorted_output = ''.join(character_list)

# Display the sorted string
print("The sorted string (Insertion Sort) is:", sorted_output)
