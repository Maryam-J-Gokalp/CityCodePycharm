x = int(input("enter x: "))
y = int(input("enter y: "))
z = int(input("enter z: "))
if(x > y):
    if(x > z):
        print("largest number is", x)
    else:
        print("largest number is", z)
else:
    if(y > z):
        print("largest number is", y)
    else:
        print("largest number is", z)
