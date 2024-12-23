# Built in functions for lists II
set3 = {1,2,3}
len(set3)
print(set3)

#Example I
set1 = {"white","red","blue","red","black" }
print(set1)
print(min(set1))

# Maximum Value
set1 = {"white", "red", "blue", "red", "black"}
print(set1)
print(max(set1))

#Example II --> Lenghth of a set
set1 = {"white", "red", "blue", "red", "black"}
print(set1)
print(len(set1))

#Adding and removing a value
#Add a value used to add a value somewhere in the set
#remove a value used to remove a desire value from the set

set4 = {1,2,3}
set4.add(4)
set5 = {1,2,3}
set5.remove(1)
print(set5)

# Poppping and clearing values
#pop() used to remove an element from the set
#clear () used to remove all elements from the set
#Example
set6 = {1,2,3}
set6.pop()
set7 = {1,2,3}
set7.clear()

#Examples III
#Adding element
set1 = {175,184, 172}       #creating set1
set1.add(176)                #add command
print(set1)

#popping an element
set1 = {175,177,184,172}
set1.pop()
print(set1)

#Removing an element
set1 = {175,177,184,172}
set1.remove(184)
print(set1)

#Clearing the set
set1 = {175,172,177,187}
set1.clear()
print(set1)

# try it yourself
#Write a program that keeps taking
#haracters as the input and storing them
#Write a program that keeps taking caracters as the input and storing them
#n a set until empty string is entered.
#hen print the number of unique
#haracters that was entered.
#ote: use the input() inside a WHILE
#oop. Use the BREAK statement to exitthe loop when "" is encountered.

chars = set()  # Create an empty set
while (char := input("Enter a character (or press Enter to finish): ")) != "":
    chars.add(char)  # Add character to the set
print("Number of unique characters entered:", len(chars))

