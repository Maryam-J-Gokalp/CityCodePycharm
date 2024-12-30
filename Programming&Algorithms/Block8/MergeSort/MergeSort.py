# merger sort
# start with algarish contain 8 elements such as: 50, 3, 15, 8, 31, 26, 11 and 42
# then the submit is divid into one element each such as: 50, 3, 15 , 8 next divission: 31, 26, 11, 42
#from unittest.mock import right from os.path import split from unittest.mock import right


# then the sublist is dividing again sych below
# 50 | 3 | 15 | 8                2rd 31 | 26 | 11 | 42
#divid again
# 50 | 3  -->15|8                 31|26 ---->11|42

#make another division
## 50 | 3       ->15 | 8           31  |  26    -->11 | 42
# 50--> 3          15-->8          31c-->c26       11--> 42

# Merge sort-Conquer is when the algarism are merge together based on the division of the sort until combined the whole number again

# Merge Sort Algorithm
# Use merge_sort function repeatedly to divide the list
# into two halves, sort them and then combine them
# 1. find mid, left and right
# 2. merge_sort(left)
# 3. merge_sort(right)
# 4. merge(left, right)

# MERGE SORT EXAMPLE
# Merge Sort Example
def merge_sort(list1):
    """
    This function sorts a list using the merge sort algorithm.
    """
    if len(list1) > 1:
        mid = len(list1) // 2    # Find the midpoint of the list
        left = list1[:mid]       # Divide the list into left half
        right = list1[mid:]      # Divide the list into right half

        # Recursively apply merge_sort to each half
        merge_sort(left)
        merge_sort(right)

        # Merge the sorted halves back into the main list
        i = j = k = 0

        # Compare elements from both halves and insert the smallest into list1
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list1[k] = left[i]
                i += 1
            else:
                list1[k] = right[j]
                j += 1
            k += 1

        # If left has remaining elements, copy them to list1
        while i < len(left):
            list1[k] = left[i]
            i += 1
            k += 1

        # If right has remaining elements, copy them to list1
        while j < len(right):
            list1[k] = right[j]
            j += 1
            k += 1

# Input handling and execution
try:
    input_string = input("Enter your numbers, separated by spaces, then press enter: ")
    split_input = input_string.split()
    numbers = [int(n) for n in split_input]  # Convert input to a list of integers

    merge_sort(numbers)
    print("Sorted list:", numbers)
except ValueError:
    print("Please enter valid integers separated by spaces.")

#---------------------------------------------------------------------->
def merge_sort_string(string_list):
    """
    This function sorts a list of characters using the merge sort algorithm.
    """
    if len(string_list) > 1:
        mid = len(string_list) // 2  # Find the midpoint
        left = string_list[:mid]    # Divide into left half
        right = string_list[mid:]   # Divide into right half

        # Recursively apply merge_sort_string to each half
        merge_sort_string(left)
        merge_sort_string(right)

        # Merge the sorted halves
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                string_list[k] = left[i]
                i += 1
            else:
                string_list[k] = right[j]
                j += 1
            k += 1

        # Copy any remaining elements from left
        while i < len(left):
            string_list[k] = left[i]
            i += 1
            k += 1

        # Copy any remaining elements from right
        while j < len(right):
            string_list[k] = right[j]
            j += 1
            k += 1

input_string = input("Enter a string to sort alphabetically: ")  # Input from the user

string_list = list(input_string)   # Convert the input string into a list of characters

merge_sort_string(string_list)     # Sort the list of characters using merge_sort_string

sorted_string = ''.join(string_list)  # Convert the sorted list back to a string

print("Sorted string:", sorted_string)  # Output the sorted string
