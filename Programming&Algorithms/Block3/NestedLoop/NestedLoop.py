n = int(input("enter n: "))
m = 1
while m <= n:    # condition 1
    total = 0 # Set variation for the nested loop
    i =1
    while i <= m:   # condition 2
        total += 1
        i += 1        # extra indentation for the body of the nested loop
        m += 1
        print("sum is", total)



 # Example
n = int(input("Enter n: "))  # Get user input for the upper limit
m = 1  # Initialize m

while m <= n:  # Continue while m is less than or equal to n
    total = 0  # Reset total for each value of m
    i = 1  # Initialize i for summation

    while i <= m:  # Sum numbers from 1 to m
        total += i  # Add i to total
        i += 1  # Increment i

    # Print the sum for the current value of m
    print("Sum of 1 to", m, "is", total)

    m += 1  # Increment m to calculate for the next number


# Try It Yourself
# Trace the execution of the following
# nested loop:
n = int(input("Enter n: "))  # Get the starting value of n from the user
total = 0  # Initialize total to 0

while n > 0:  # Outer loop continues as long as n > 0
    m = n  # Assign the current value of n to m
    i = 1  # Initialize i to 1

    while i <= m:  # Inner loop runs as long as i <= m
        total += i  # Add i to total
        i += 1  # Increment i
        n -= 1  # Decrement n
        print("Total is", total)  # Print the current value of total


