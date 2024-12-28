from re import search


def ordered_linear_search(list1, key):
    index = -1  # Initialize index to -1 to indicate that the key has not been found yet
    list1 = [3, 8, 15, 26, 31, 50, 62, 73, 83, 86]
    search_key = int(input())
    # Loop through each element in the list
    for i in range(0,len(list1)):
        if list1[i] == search_key:  # If the current element equals the key
            index = i  # Set the index to the current index of the found key
            break  # Exit the loop immediately since we've found the key

        elif list1[1] > search_key:  # If the current element is greater than the key, stop searching
            break  # Exit the loop since the list is ordered, and further elements will be greater than the key

    # After the loop, check if the index was updated (i.e., key was found)
    if index != -1:  # If the index is not -1, it means the key was found
        print("key found in the list1")  # Print the key and its index
    else:  # If the index is still -1, it means the key wasn't found
        print("key not found in the list1")  # Print a message indicating the key was not found

#Try It Yourself
#Write a program in python environment that takes a alphabetically sorted string and a
#character as an input and finds whether the character is found within the string using an ordered linear search

def isInAlphabeticalOrder(word):
    word1=sorted(word)
    word2=[]
    for i in word:
        word2.append(i)
    if word2 == word1:
        return True
    else:
        return False
