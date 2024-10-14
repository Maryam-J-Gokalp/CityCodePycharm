letter = 'a'
print(letter)  #output a

# letter = 'a': This assigns the value 'a' (a string containing the letter 'a') to the variable letter.
# print(letter): This prints the value of the variable letter, which is the string 'a'.

empty_string = ''       # assign value '' to empty_string represent empty string by '' double quote
print(empty_string) # This prints the value of empty_string holds an empty string, nothing will be printed to the output  and the line is blank

number = '8'  # assign value 8 to number
print(number)  # print number the output is 8 because value is 8

greeting = 'Hello, how are you today?'
print(greeting)
# This assigns the string 'Hello, how are you today?' to the variable greeting.
#print(greeting): This prints the value of the variable greeting --> Hello, how are you today?

# letter string type
letter = 'a'
print(type(letter))
# assign a single character string a, to the variable letter
#print(type(letter)): Now, we want to find out what kind of thing letter is, and type() function, to determine the date type of variable.letter. The type() function returns the type of the object passed to it.
#output <class 'str'> indicates that the data type of letter is a string (str).

description = '2 squared is:'
number = 4
print(description)
print(number)  #output 4
# printing multiple variable
#description = '2 squared is:': This line creates a variable called description and assigns it the text '2 squared is:'. This is just a string that gives information about the number.
#number = 4: Here, we create another variable called number and give it the value 4. This number represents the result of squaring 2 (since 2 =4).
#print(description): This line tells the computer to display the text stored in the description variable, print number 4 when run shows 4

description = '2 squared is'
number = 4
print(description, number)
# same line
# create a variable called description, and assign string 2 squared is, string is a single character enclosed in single or double quote, here string is number 2
#number = 4 <---create a variable name number, assign into the integer value 4. The integer 4 represents the result of squaring 2, because 2 = 4
#print values(description, number): <---The print() function outputs these together as a single line: 2 squared is 4.

description = 'squared is'
number = 2
number_squared = number ** 2
print(number,description,number_squared)
#multiple number variable
# description = 'squared is', abd creates a variable named description and assigns it the string 'squared is indicating that we are discussing the result of squaring a number
# number = 2 <-----This line creates a variable named number and assigns it the integer value 2.

description = 'squared is:'
number = 2
print(number, description,number ** 2)   #output square is 4
#Variable Assignment:
#description = 'squared is:' --->creates a variable description that holds the string 'squared is:'. This string is part of the phrase that will explain what is happening when we display the result.
#number = 2: ------>This assigns the integer value 2 to the variable number. This variable represents the base number that will be squared (raised to the power of 2).
#Calculation Inside print():