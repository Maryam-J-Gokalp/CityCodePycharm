from colorsys import yiq_to_rgb


# code before if statement excuted on if the condition is tru
# and is skipped if the conditions is false
x = 1
if(x > 0):  # after x if the condition is true
    x += 1
    print(x)    # print body identify and x body is executed

#IF Statement Flow Chart
    y = -1                              # start read y
    if(y > 0) :                         # x > 0? decision condition (No or yes)
        y += 1                          # initialize
        print(y)                         # body is executed print the body message y


# Examples I
x = int(input())                                     # start
if(x > 5):                                          # condition
    print("Your number is greater than 5")            # execute body


# Examples II
x = int(input("Enter a whole number"))                   # start input users enter number, and input number and ask user to use whole number
if(x % 2 == 0):                                          # check if the number is even by testing if (x % 2 == 0): ---. if is even print number even if false skip statement
    print("Your name is even")

x = 5
if(x > 3):
    x -= 3
    print(x)

    code = input()
    if(code == "123"):
        print("unlocked")

        name = input("name: ")
        if(name != ""):
            print("Your name is:", name)