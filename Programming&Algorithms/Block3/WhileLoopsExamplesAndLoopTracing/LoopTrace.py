from itertools import count

n = int(input("enter n: "))
total = 1
count = 1

while count <=n:                                 # 1 <= 3 evaluates to true
    total *= count                                #total
    count += 1                                    #end of loop is reached, the execution jump back to the beginning of while loop and start again
    print("factorial of", n, "is", total)         # print value for factorial of n
   # entet n: 3
  #  factorial of 3 is 6


# Loop trace example !!
count = 0
y = int(input("enter y:  "))
while y > 1:
    y //= 2
    count += 1
    print(count)

    m = int(input("enter m: "))
    n = int(input("enter n: "))
    total = 0

    while m <= n:
        total += m
        m += 1
        print(("the total is", total))

