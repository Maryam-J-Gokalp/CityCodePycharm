#Why use Sort Algorithms?
#Sorting – a classic subject in computer science
#Examples
#Sports league tables. Ranking countries based on GDP
#Sorting products based on their price
#Sorting restaurants based on their review rating
from os.path import split


#Purpose of Sorting Algorithms
#Simplify Problems: Provide logical methods to organize data.
#Improve Efficiency: Sort elements in arrays or lists quickly.
#Enable Searching: Essential for search methods like binary search.

#Applications. Sorting is vital for:
#Fast lookups (e.g., binary search).
#Clear data visualization.
#Efficient data storage and retrieval.

#ACTIONS
#The simplest way of sorting a list is to first
#find the smallest element in the list. Then place it at position 0 of the new list
#Then find the second smallest element in the list and place it at position 1
#Repeat this process for all elements in the list

#Simple Sorting Algorithms II
def simple_sort(list1):
    n = len(list1)  # Get the number of elements in the input list.
    list_sorted = []  # Initialize an empty list to store sorted elements.

    for i in range(n):  # Loop through the list n times (where n is the original list length).
        min1 = list1[0]  # Assume the first element in the list is the smallest.
        for j in range(len(list1)):  # Check every element in the list to find the smallest one.
            if list1[j] < min1:  # Compare current element with the assumed smallest.
                min1 = list1[j]  # Update the minimum value if a smaller element is found.

        list_sorted.append(min1)  # Add the smallest element to the sorted list.
        list1.remove(min1)  # Remove the smallest element from the original list.

    return list_sorted  # Return the sorted list.

# Take user input
input_string = input("Enter your numbers, then press enter: ")  # Prompt the user to input numbers separated by spaces.

split_input = input_string.split()  # Split the input string into individual components (by spaces) to form a list of strings.

numbers = [int(n) for n in split_input]  # Convert each string in the list to an integer to create a list of numbers.

numbers = simple_sort(numbers)  # Call the `simple_sort` function to sort the list of numbers.

print("sorted list:", numbers)  # Print the sorted list to the user.



#-------------------------------------------------------------->
def simple_sort(string_list):
    n = len(string_list)  # Get the number of elements (characters) in the string list.
    sorted_list = []  # Initialize an empty list to store sorted characters.

    for i in range(n):  # Loop through the list n times (where n is the original length of the string list).
        min_char = string_list[0]  # Assume the first character is the smallest.
        for j in range(len(string_list)):  # Check every character to find the smallest one.
            if string_list[j] < min_char:  # Compare current character with the assumed smallest.
                min_char = string_list[j]  # Update the minimum character if a smaller one is found.

        sorted_list.append(min_char)  # Add the smallest character to the sorted list.
        string_list.remove(min_char)  # Remove the smallest character from the original list.

    return ''.join(sorted_list)  # Join the sorted characters into a single sorted string.

# Take user input
input_string = input("Enter a string: ")  # Prompt the user to input a string.

# Convert the string into a list of characters
char_list = list(input_string)

# Sort the characters in alphabetical order using the simple sorting algorithm
sorted_string = simple_sort(char_list)

# Output the sorted string
print("Sorted string:", sorted_string)









