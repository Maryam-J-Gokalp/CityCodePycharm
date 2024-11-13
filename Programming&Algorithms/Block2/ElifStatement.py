from colorsys import yiq_to_rgb
from doctest import Example
from threading import Condition

x = int(input())
if x > 0:
    print(x, "is positive")
elif x < 0:
    print(x, "is negative")
else:
    print(x, "is zero")

# ELif statement flow Chart
# --> Start---> read x ---> x > 0? yes or no ---> if yes print message 2, if no print message 3, and if yes print message 1

# Examples
George = 30
Jack = 41

if(George > Jack):
    print("George is older than Jack")
elif(George == Jack):
    print("George is the same age as Jack")
else:
    print("George is younger than Jack")

# Examples
answer = input("left, right or straight? ")
if(answer == "left"):
    print("You will arrive at town A")
elif(answer == "right"):
    print("You will arrive at town B")
else:
    print("You will arrive at town C")

# Practice code
x = int
y = 6
z = 15
if(x < y):
    print("your number is smaller than", y)
elif(x > z):
    print("your number is greater than", z)
else:
    print("your number is between", y, "and", z)