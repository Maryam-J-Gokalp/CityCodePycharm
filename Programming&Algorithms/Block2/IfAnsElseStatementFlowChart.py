#IF ELSE Statements Flow Chart
# start and input x ask for a number and store as x ---> x = int(input())
# condition is true print x is positive or print false is not positive ----> is x if(x > 0):
# print(x, "is positive") --> execute when the condition is true
#-->else:
#---> print(x, "is not positive")


# Example 1
George = 30
Jack = 41
if(George > Jack):
    print("George is older than Jack")
else:
    print("George is not older than Jack")


# Example II
answer = input("What programming language are we using? ")
if(answer == "Python"):
    print("Correct")
else:
    print("Incorrect")

# Enyter a run the following statements in the python environment
x = int(input("enter a whole number: "))
y = 6
if(x < y):
    print("your number is smaller tham", y)
else:
    print("your number is", y, "or greater")