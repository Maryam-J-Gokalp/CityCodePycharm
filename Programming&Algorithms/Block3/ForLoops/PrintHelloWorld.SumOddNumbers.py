#TIY 1
#ask fot the number of times to be entered
x = int(input("Enter number of times"))
#set counter equal to 1
for i in range(1, x+1):
    #print comment as required
    print("Hello World!")

    # TIY 2
    # ask fot number n
    n = int(input("Enter a value for n:"))
    # set sum to zero
    sum = 0
    # set counter equal to 1
    for i in range(1, n + 1, 2):
        # add value to sum
        sum = sum + i
    # print the final value
    print("The sum of the odd numbers from 1 to n is", sum)