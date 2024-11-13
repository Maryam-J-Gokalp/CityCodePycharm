# Example of using if, elif, and else statements in Python
from multiprocessing.connection import answer_challenge

# Define a variable
temperature = 25

if temperature > 30:
    print("It's a hot day!")  # Executed if temperature is above 30
elif temperature > 20:
    print("It's a warm day.")  # Executed if temperature is 21 to 30
elif temperature > 10:
    print("It's a cool day.")  # Executed if temperature is 11 to 20
else:
    print("It's a cold day.")  # Executed if temperature is 10 or below

# Elif Statement Flow Chart
# Program to check if a number is positive, negative, or zero
#Input Prompt: The program first prompts the user to enter a number, which is stored as an integer in x.
#Conditional Statements:
#if x > 0: Checks if the number is positive. If true, it prints that the number is positive.
#elif x < 0: If the first condition is false, it checks if x is negative. If true, it prints that the number is negative.
#else: If neither condition is true (meaning x is neither positive nor negative), it defaults to printing that the number is zero.

# Another check if the number is positive or zero
x = int(input("Enter another number: "))
if x > 0:
    print(x, "is positive")
else:
    print(x, "is zero")

# Age comparison example
George = 30
Jack = 41

if George > Jack:
    print("George is older than Jack")
elif George == Jack:
    print("George is the same age as Jack")
else:
    print("George is younger than Jack")

# Directional choice based on input
answer = input("Choose a direction (left, right, or straight): ").lower()
if answer == "left":
    print("You will arrive at town A")
elif answer == "right":
    print("You will arrive at town B")
else:
    print("You will arrive at town C")


#Common Errors in python
#Added Initial if Statement: The code now begins with if number > 0, which is required for using elif conditions.
#Indented print Statements: Each print() statement is indented to align with the if, elif, and else structure.
#Expanded Conditions: Added an elif number < 0 condition to handle negative numbers and an else block for the case when the number is zero.

number = int(input("Enter a whole number: "))
if number > 0:
    print("Positive number")
elif number < 0:
    print("Negative number")
else:
    print("The number is zero")
#__________________________________________________________________
# Enter and run the following statements
x = int(input("enter a whole number: "))   # ask to add whole number & assign to variable x

# comparison variables define to y = 6 and z =  15 <--this number are the x will be compared to
y = 6                                       # less than y (6): if x is smaller than 6, the program prints (your number is smaller than 6)
z = 15                                      # Greater than z (15): if x is Less than y (6)

if(x < y):                                      # if the number is smaller than 6, the number yout type stored in x is less than 6, it print your number is smaller than 6
    print("your number is smaller than", y)      #it print your number is smaller than 6
elif(x > z):
    print("your number is greater than", z)      #if number is greater than 15, is says your number is greater than 15
else:
    print("your number is between", y, "and", z)   # if the numnber is between 6 and 15, smaller than 6 and bigger than 15, it says your number is between 6 and 15