#Linear Search
#Simplest search method to implement
#Scanning takes place from left to right until the search key is found
#Linear search example
from re import search

List: [15, 8, 31, 73, 86, 3, 26, 83, 50, 62]
#Search key: 73

#----------------------------------------------------------------->
def linear_search(list, key):
    index = -1  # Step 1: Initialize index to -1 (key not found initially)
    list1 = [15, 8, 31, 86, 3, 26, 83, 50, 62]
    search_key = int(input())
    # Step 2: Input search key is passed as argument 'key'

    for i in range(len(list1)):  # Step 3: Iterate over the list
        if list[i] == search_key:  # Step 4: Check if the current element matches the key
            index = i  # Step 5: If found, store the index of the element
            break  # Step 6: Exit the loop as key is found

    if index != -1:  # Step 7: If key is found (index not -1)
        print("key found in list1")  # Step 8: Print key found message
    else:  # Step 9: If key is not found
        print("key not found in list1")  # Step 10: Print key not found message


#----------------------------------------------------->
#Try It Yourself
#Write a program in python environment that takes a string and a character as an input and
#finds whether the character is found within the string

string = input("Enter a string: ")  # Take string input
char = input("Enter a character: ")  # Take character input
if char in string:  # Check if the character is in the string
    print("Character found")  # Print if found
else:
    print("Character not found")  # Print if not found
