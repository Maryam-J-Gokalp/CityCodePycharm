# Non-BooleanIfConditionalExamples
#Boolean
from time import perf_counter

if True:                         # cheeck if is true and print 1
    print(1)

#String
if "False" :                      # False inside "" make a string is conside true, it will print 1
    print(1)

#Boolean
if False :                         #<--We are checking is false is true, since false is not true this part of code does not run and print 1
    print(1)

#String
if "":                                #empty string not text inside, empty string is consider false
    print(1)

# numeric data types
if 124:
    print(1)

if 0.1:
    print(1)

if 0:
    print(1)

if 0.0:
    print(1)

 # if else statement example
x = int(input())
if x > 0:
    print(x, "is positive")
elif x < 0:
    print(x, "is negative")
else:
    print(x, "is zero")

# flow chart start, read x, x >0? if ye print expression 1 and if not print expression 2

#examples
George = 30
Jack = 41
print("George", "is" if(George > Jack) else "is not", "older than Jack")

# Examples
answer = input("What programming language are we using? ")
if answer == "Python":
    print("Correct!")
else:
    print("Incorrect")

#
x = int (input("enter a whole number: "))
y = 6
if(x < y):
    print("your number is smaller than", y)
else:
    print("your number is", y, "or greater")

