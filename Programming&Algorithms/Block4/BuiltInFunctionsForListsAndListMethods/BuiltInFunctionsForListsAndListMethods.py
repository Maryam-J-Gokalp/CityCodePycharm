#Maximum value
list1 = ["a", "d", "c", "b"]
print(list1)

#Length of a list
list3 = ["a", "d", "c", "d"]
print(len(list3))

#Maximum value
list2 = ["a", "d", "c", "d"]
print(len(list2))

#Sum of the list
list4 = [1, 4, 3, 2]
print(sum(list4))

#Example II
#Appending an element
list1 = ["a", "b", "c", "b"]
list1.append("e")
print(list1)

#Popping an element
list3 = ["a", "d", "c", "b"]
list3.pop()  # This will remove and return the last element "b".
print(list3)  # Output will be: ["a", "d", "c"]

#Inserting an element
list2 = ["a", "d", "c", "b"]
list2.insert(0, "e")
print(list2)

#Removing an element
list4 = ["a", "d", "c","d"]
list4.remove("c")
print(list4)


# Finding the Index of an Element
# Examples III
#Reversing a list
list1 = ["a", "d", "c", "b"]
list1.reverse()
print(list1)

#Finding the index
list3 = ["a", "d", "c","b"]
list1.reverse()
print(list3.index("b"))

#Sorting a list
list2 = ["a","d","c","b"]
list2.sort()
print(list2)

#Finding the index
list4 = ["a",["d"], ["c"],["b"]]
list5 = ["d"]
print(list4.index(list5))  #output 1

#Try It Yourself
#Enter and run the following statements in the python environment:
list1 = []
for n in range(0, 5):
 list1.append(n)
print(list1)

list4 = [1, 5, 3, 4, 2]
list4.insert(list4.index(5), 6)
print(list4)

list2 = [1, 5, 3, 4, 2]
list2.remove(max(list2))
print(list2)

list3 = [1]
if len(list3) > 0:
 print("list is not empty")
