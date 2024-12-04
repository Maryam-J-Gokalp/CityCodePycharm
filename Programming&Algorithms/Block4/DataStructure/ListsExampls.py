#Example 1 of lists
list1 = [1,2,3]
print(list1)

list1 = [1,2,3]
print(list1[-1])

list1 = [1,2,3]
print(list1[0])


#Example II Modifying an element of list
list1 = [1,2,3]
list1[1] += 1
print(list1)

list1 = [1,2,3]
list1[1] = list1[0]
print(list1)

list1 = [1,2,3]
list1[1] = False
print(list1)

#List Properties  Lists are mutable, so elements can
# Altered,  Added,  Removed Lists can be empty
# Used to initialize empty lists and add elements later
# Lists can contain another list as an element

#Examples III Empty List
list2 = []
print(list2)

#Lists aqs elements
list3 = [[1,2,3], 4,5,[]]
print(list3)

#Lists as elements
list1 = [1,2,3]
list2 = []
list3 = [list1, 4, 5, list2]
print(list3)

#Printing an element of type list
list1 = [1,2,3]
list2 = []
list3 = [list1, 4,5, list2]
print(list3[0])


#Enter and run the following statements in the python  environment:

list1 = [2, 3]
sum = list1[0] + list1[1]
print(sum)

list4 = [15, True]
if list4[1] == True:
    print(list4[0])

list3 = [5, "orange"]
list3[0] -= 2
print(list3[1], list3[0])

list2 = [1, 2, 3]
list2[0] += list2[2]
print(list2[0])



