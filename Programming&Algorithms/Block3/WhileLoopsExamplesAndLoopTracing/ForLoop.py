m = int(input("Enter m: "))  # Get the starting number
n = int(input("Enter n: "))  # Get the ending number
total = 0  # Initialize the variable to store the sum of odd numbers

# Check if m is even
if m % 2 == 0:
    m += 1  # If m is even, make it the next odd number

# Loop through odd numbers from m to n (inclusive)
for count in range(m, n + 1, 2):  # Step is 2 to ensure only odd numbers are included
    total += count  # Add the current odd number to the total
    print(("Sum of odd numbers from", m, "to", n, "is", total))


# trace the execution of the following For loop example
m = int(input("Enter m: "))  # Get the starting number
n = int(input("Enter n: "))  # Get the ending number

for count in range(1, n + 1, 1):  # Loop from 1 to n (inclusive), step = 1
    m -= count  # Subtract count from m
    print("The total is", m)  # Print the updated value of m

#Step-by-Step Execution:
#Input Stage:
#𝑚 = 10 (starting number).
#𝑛 = 4
#n=4 (ending number).

#Initialize Loop:
#range(1, n + 1, 1) generates the sequence [1,2,3,4],
#Start: 1.
#Stop: n +1=5(exclusive, so stops at 4).
#step: 1.

#Iterations:
#First Iteration (count = 1):
#m = 10-1=9.
#output: the total is 9
# second iteration
# m = 9-2 =7 and the output is 7
# third iteration count = 3
#m = 7 - 3=4.
#output the total is 4
#fourth iteration cont = 4
#m=4-4=0. and the output is 0
# terminationation  the valued of count be 5 and greater than n+1=5, so the loop ends

