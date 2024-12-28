#Constant Order of Complexity Example
#Function foo(x):
#y = 5x
#y = y + 5
#Return y
#Executed only
#once
#Complexity:
#O(1 + 1) = O(1)
def foo(x):
    y = 5 * x  # Step 1, the function takes the input x (a value passed to the function) and multiplies it by 5. The result of 5 * x is then assigned to the variable y.
    y = y + 5  # Step 2, , we take the value of y (from the previous step) and add 5 to it. The result is then assigned back to the variable y.Continuing the previous example where y = 15, after this step, y will be updated to y + 5 = 15 + 5 = 20.
    return y    # Step 3, value stored in y to wherever the function foo(x) was called. When the function is called, the final value of y will be given as the output of the function.


#--------------------------------------------------------->
def foo2(list):
    bar = 0          # Step 1: Constant time operation (step 1 and 2 executed once
    i = 1            # Step 2: Constant time operation
    while i <= len(list):  # Step 3: Loop runs once per element in the list
        bar = bar + 2 * list[i]  # Step 4: Constant time operation
        i = i + 1     # Step 5: Constant time operation
    return bar        # Step 6: Constant time operation

#------------------------------------------------------------->
def foo3(list):
    sum = 0               # Step 1: Constant time operation
    c = 1                 # Step 2: Constant time operation
    while c <= len(list): # Step 3: Outer loop (runs n times)
        c1 = 1            # Step 4: Constant time operation
        while c1 <= len(list):  # Step 5: Inner loop (runs n times for each iteration of the outer loop)
            sum = sum + list[c] * list[c1]  # Step 6: Constant time operation inside the inner loop
            c1 = c1 + 1   # Step 7: Constant time operation inside the inner loop
        c = c + 1         # Step 8: Constant time operation for the outer loop
    return sum            # Step 9: Constant time operation

#----------------------------------------------------------->
def foo4(n):
    product = 1              # Step 1: Constant time operation
    c = n                    # Step 2: Constant time operation, set c to n
    while c > 0:             # Step 3: Loop runs as long as c is greater than 0
        product = product * c  # Step 4: Constant time operation inside the loop
        c = c // 2           # Step 5: Constant time operation (c is halved in each iteration)
    return product           # Step 6: Constant time operation
