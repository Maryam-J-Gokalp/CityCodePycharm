#Bubble Sort
# In the first pass, each element in the list is compared with the following element in the list.
#If this element is bigger then the element being compared, then they are swapped.
#If you repeat this process enough times, the data will be sorted in ascending order
from os.path import split


#Examples:  50,3,15,8,31,26  | the 50 swap to 3, 50,15,8,31,26 | the 50 swap with 8 ---> 3, 15, 50, 8, 31, 26

# Bubble Sort Algorithm
# 1.n = len(list)
# 2. for i in range(n-1)
# 3. for j in range(n-1-i)
# 4. if list[j] > list[j + 1]
# 5. temp = list[j]
# 6. list[j] = list[j + 1]
# 7. list[j + 1] = temp

def bubble_sort(list1):  # Define the function bubble_sort that takes a list as input
    n = len(list1)  # Step 1: Get the number of elements in the list

    for i in range(n - 1):  # Step 2: Loop n-1 times (to ensure sorting)
        for j in range(n - 1 - i):  # Step 3: Loop through the list, excluding the last sorted elements
            if list1[j] > list1[j + 1]:  # Step 4: Compare adjacent elements
                # Step 5-7: Swap the elements if they are in the wrong order
                temp = list1[j]  # Store list1[j] in temp
                list1[j] = list1[j + 1]  # Replace list1[j] with list1[j + 1] (the smaller one)
                list1[j + 1] = temp  # Assign the original value of list1[j] to list1[j + 1] (swap)

input_string = input("Enter your numbers, then press enter: ")  # Prompt the user for input
split_input = input_string.split()  # Split the entered string into a list of substrings based on spaces
numbers = [int(n) for n in split_input]  # Convert each substring in the list to an integer and store in 'numbers'

bubble_sort(numbers)  # Call the bubble_sort function on the 'numbers' list
print("Sorted list: ", numbers)  # Print the sorted list to the user



#-------------------------------------------------------------->
# Try It Yourself
    # Write a program in python environment that
    # takes a string as an input and sorts in
    # alphabetical order using the bubble sort
    # algorithm above
def bubble_sort(arr):
    # Get the length of the list
    length = len(arr)

    # Outer loop for each pass through the list
    for i in range(length - 1):
        # Inner loop to compare adjacent elements
        for j in range(length - 1 - i):
            # Check if the current element is greater than the next one
            if arr[j] > arr[j + 1]:
                # Swap elements if they are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# Get user input as a string
user_input = input("Please enter a string: ")

# Convert the input string into a list of characters
character_list = list(user_input)

# Apply the bubble sort to the list of characters
bubble_sort(character_list)

# Join the sorted list back into a string
sorted_output = ''.join(character_list)

# Display the sorted string
print("The sorted string is:", sorted_output)