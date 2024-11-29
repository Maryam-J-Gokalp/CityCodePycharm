n = int(input("enter n: "))
total=0
count=1
while count <= n:
    total += count
    count += 1
    print("the total is", total)
# output enter n 5x

    #Example 2
    x = int(input("enter x: "))
    total = 0
    while(x != ""):
        total+= int(x)
        x = input("Enter x: ")
        print(total)

# Problem 1
# Write a program in Python environment
# that takes an input value x and prints
# “Hello World!” that x times
# Get the input value x
x = int(input("Enter the number of times to print 'Hello World!': "))
# Loop to print "Hello World!" x times
for i in range(x):
    print("Hello World!")
