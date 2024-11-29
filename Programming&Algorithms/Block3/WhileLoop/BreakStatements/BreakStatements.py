#TIY 1
#ask fot the number of times to be entered
x = int(input("Enter number of times"))
#set total to zero
total = 0
#set counter equal to 1
for i in range(1, x+1):
    total = i
    #print statement
    print("Hello World!")
    #when 5 statements have been printed stop even if x given is larger than 5
    if total == 5:
        break

n = int(input("enter n: "))
total = 0
for count in range(1, n+1):
    total += count
    if total > 50:
        break
print("the total is", total)
print("the total is", count)


#Example
total = 0
while 1==1:
    n = int(input("enter n: "))
    if n <=0:
        break
        total += n
        print("the total is", total)

# Try It Yourself
# Write a program in Python environment
# that prints “Hello world!” x times, but a
# maximum of 5 times, even if x is greater

total = 0
while 1==1:
    HelloWorld =int(input("enter Hello World", ))
    if HelloWorld <=0:
        break
        total += HelloWorld
        print(" Hello World",  "5x")
