#Binary Search
#It will split the data lists and repeats the process until a search key is found
#Binary search example
# 3, 8, 15, 26, 31, 50, 62, 73, 83, 86
from operator import index
from re import search


# Binary Search Algorithm
def binary_search(array, target):
    # Initialize pointers for the start and end of the list
    start = 0
    end = len(array) - 1

    while start <= end:
        # Calculate the middle index
        middle = (start + end) // 2

        # Check if the target is at the middle index
        if array[middle] == target:
            print(f"{target} found in the list at index {middle}.")
            return middle  # Return the index where the target was found

        # If the target is smaller, narrow the search to the left half
        elif array[middle] > target:
            end = middle - 1

        # If the target is larger, narrow the search to the right half
        else:
            start = middle + 1

    # If the loop ends, the target is not in the list
    print(f"{target} not found in the list.")
    return -1  # Return -1 to indicate the target is not found

# Example usage
numbers = [2, 4, 6, 8, 10, 12, 14, 16]
key = 10
binary_search(numbers, key)

#-------------------------------------------------------------------->
#Tracing the Behaviour of the Binary Search
# 3, 8, 15, 26, 31, 50, 62, 73, 83, 86 with explanations of First, Mid, and Last.

#Summary of Iterations:
#Iteration	First (Index, Value)	Mid (Index, Value)	Last (Index, Value)	Comparison	Action
#1	0 (3)	4 (31)	9 (86)	31 < 50	First = Mid + 1 (5)
#2	5 (50)	7 (73)	9 (86)	73 > 50	Last = Mid - 1 (6)
#3	5 (50)	5 (50)	6 (62)	50 == 50	Key found at index 5


#--------------------------------->
#Let’s trace the binary search algorithm for the list:

#3, 8, 15, 26, 31, 50, 62, 73, 83, 86
#Search Key: 65

#----------->Step 1:
#First = 0, Last = 9, Mid = 4 (value = 31).
#31 < 65 → Update First to 5.

#---------->Step 2:
#First = 5, Last = 9, Mid = 7 (value = 73).
#73 > 65 → Update Last to 6.

#----------->Step 3:
#First = 5, Last = 6, Mid = 5 (value = 50).
#50 < 65 → Update First to 6.

#------------>Step 4:
#First = 6, Last = 6, Mid = 6 (value = 62).
#62 < 65 → Update First to 7.

#----------->Final Step:
#First = 7, Last = 6 → Condition First > Last.
#Result: 65 is not in the list.

#Final Output:
#65 is not found in the list.

#-------------------------------------------------->
#Binary Search Example
index = -1
list1 = [3, 8, 15, 26, 31, 50, 62, 73, 83, 86]
first = 0
last = len(list1)-1
key = "key not found"
search_key = int(input())               #<------user input search_key is 50
while first <= last:                    #<------0 <= 9 evaluates to True
    index = (first + last) // 2         #<------(o + 9) // 2 = 4
    if list1[index] == search_key:          #<------31 == 50 evaluates to False
        key = "key found"
        break
    else:
        if list1[index] > search_key:       #<--------31 > 50 evaluates to False
            last = index -1
        else:
            first = index + 1        #<---------first = 4 + 1 = 5. the end of loop body is reached, so execution jumps back to the beginning of the loop and condition is tested again

#---------------------------------------------------------->
index = -1
list1 = [3, 8, 15, 26, 31, 50, 62, 73, 83, 86]
first = 0
last = len(list1)-1
key = "key not found"
search_key = int(input())               #<------user input search_key is 50
while first <= last:                    #<------0 <= 6 evaluates to True
    index = (first + last) // 2         #<------(5 + 6) // 2 = 5
    if list1[index] == search_key:          #<------50 == 50 evaluates to true
        key = "key found"                    #<--------key set to found
        break                                #<-----terminate the execution of the loop
    else:
        if list1[index] > search_key:       #<--------31 > 50 evaluates to False
            last = index -1
        else:
            first = index + 1        #<---------first = 4 + 1 = 5. the end of loop body is reached, so execution jumps back to the beginning of the loop and condition is tested again
            print(key, "in list1")     #<------print that the value is found in the list




#Analysis
#Binary search runs in logarithmic time, which means the number of iterations cannot be more than log n + 1, n being the size of the list
#Example
# when n = 100
# log2 n + 1 = 6.64 + 1 = 7.64
# The worst case scenario would require log n computations. The search will need no more than 8 iterations
# The big-O notation for binary search is O(log n)
#Logarithmic Time (O(log n))
#The time complexity O(log n) means the number of steps required grows very slowly compared to the size of the list n.
#For every iteration, the list is halved, so the maximum number of iterations depends on how many times you can halve the list before it's empty.

#Example:
#If the list has 100 elements:

#First iteration: Halve 100 → 50 elements remain.
#Second iteration: Halve 50 → 25 elements remain.
#Third iteration: Halve 25 → 12 elements remain.
#Fourth iteration: Halve 12 → 6 elements remain.
#Continue this until 1 element is left

#LINEAR AND BINARY SEARCH COMPARISON

#Linear Search                                                                     Binary Search
#Is simple to code and implement                                                   Is more complex to code
#Quite efficient for short length data lists                                       Efficient for any length of data list
#Very slow on large lists since each data element has to be compared               Fast on any length of data list since it only deals with half sub-lists. Hence the name is binary search
#Does not require data to be ordered Data has to be ordered
# Average search length is n/2 where n is the number elements in the list          Search length is log n
#Plays a part in other algorithms such as finding maximum,                          Binary search is used in fast searching routines
# minimum and also in some sorting routines

#----------------------------------------------------------------------->
#Try It Yourself II
#Write a program in python environment that takes a alphabetically sorted string and a
#character as an input and finds whether the
#character is found within the string using a
#binary search

def binary_search_string(s, target):
    first, last = 0, len(s) - 1

    while first <= last:
        mid = (first + last) // 2

        if s[mid] == target:
            return f"'{target}' found at index {mid}."
        elif s[mid] > target:
            last = mid - 1
        else:
            first = mid + 1

    return f"'{target}' not found in the string."

# Input and function call
s = input("Enter a sorted string: ")
target = input("Enter a character to find: ")
print(binary_search_string(s, target))
