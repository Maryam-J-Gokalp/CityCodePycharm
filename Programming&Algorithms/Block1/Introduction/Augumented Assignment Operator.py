x = 1
x += 1
print(x)

#Python to take the current value of x (which is 1), add 1 to it, and then store that new value back in x.
#After this line, x now holds the value 2 because 1 + 1 = 2.
#print(x):

#This command tells the computer to display the current value of x.
#Since x now holds the value 2 after the addition, it prints 2.

y = 5
y -=7
print(y)

# Assign the value 5 into current value y, which is 5
#y -= 7:
#The -= operator is a shorthand way of saying "subtract from the current value of y
#urrent value of y (which is 5) and subtract 7 from it.
#Now, y becomes 5 - 7, which equals -2. So, y now holds the value -2.

z = 4
z *= 3
print(z)

#The = sign here doesn’t mean "equal" like it does in math. In programming, = means assign. So, this line means we are giving or assigning the value 4 to a box called z.
#Imagine you have a box labeled z, and you put the number 4 inside the box.
#Example to Make it Easier:
#Imagine you have 4 apples (z = 4), and someone says, "Now triple the apples." You would now have 4 + 4 + 4 = 12 apples. That’s what this code does!

#Full Walkthrough:
#You start with z = 4 (putting the number 4 into the box called z).
#The z *= 3 tells the computer to multiply the value in z by 3. Multiplying is like repeating the number multiple times, so 4 becomes 12.
#print(z) shows the number 12, because that's the new value inside the box z.

w = 27
w/= 10
print("W")
# assigns the value 27 to the variable w
#augmented assignment operator, specifically for division. ake the value inside w (which is 27), divide it by 10, and store the result back in w
#So, dividing 27 by 10 gives you 2.7. Now, w contains 2.7


# below statement combining augmented assignment numeric operator

m = 1.0
m += 3 - 2
print("m")
#  assigns the value 1.0 to the variable m.
#First, the expression 3 - 2 is calculated. When you subtract 2 from 3, the result is 1.
#So, the line becomes m = m + 1.
#Since m started with the value 1.0, you now add 1 to it, which makes the new value of m equal to 2.0
#The value of m was originally 1.0. After the operation m += 3 - 2, the value of m becomes 2.0.
#However, the output will only show the letter "m", not the value. So, the final output of this code will be:


n = 5#
n += 2 * 2
print("n")
#variable n holding the data type 5, is assigned the value 5 to variable and n became 5
#The value of n was originally 5. After the operation n += 2 * 2, the value of n becomes 9.
# output will only show the letter "n", not the value. So, the final output of this code will be:

u = 3
u *=2 + 2
print(u)
# assign variable 3 to  variable n, so n become 3
#u *=2 + 2 this is like a math problem. First, we look at the part 2 + 2.
#What’s 2 plus 2? It’s 4!
# Now, we have u *= 4. This is just a shortcut for saying: 3 multiplied by 4? It’s 12!
#u is 12 --->print(u), it tells the computer, "Show me what’s inside the box u."
#And the computer shows the number 12


v = 27
v/= 5 + 5
print("V")

#v = 27: You assign the value 27 to the variable v.
#v /= 5 + 5: The expression 5 + 5 equals 10. The operation /= is shorthand for v = v / 10. So, v becomes 27 / 10, which results in 2.7.
#print(v): This will output 2.7 because that is the value of v after the division.

x = 2
x **= x
print("x")
# x = 2: The variable x is assigned the value 2.
#x **= x: This is shorthand for x = x ** x. The ** operator is the exponentiation operator, so it means "raise x to the power of x." Since x is currently 2, this becomes x = 2 ** 2, which is 4.
#print("x"): This prints the string "x" and not the value of the variable x. If you want to print the value of x, you should use print(x) instead.'
# output 4

y = 3
y **= y
print("y")
#y = 3: This assigns the value 3 to the variable y.
#y **= y: This is shorthand for y = y ** y. The ** operator raises y to the power of y. So, this becomes y = 3 ** 3, which equals 27 because
#3 = 3×3×3=27.
#print("y"): This prints the string "y", not the value of the variable. If you want to print the value of y, you should use print(y)

m = 5
m //= 2
print("m")

# m = 5: The variable m is assigned the value 5.
# m //= 2: This is shorthand for m = m // 2. The // operator performs floor division, which divides the number and rounds down to the nearest integer.
# So, m = 5 // 2 results in 2, because 5 divided by 2 is 2.5, and floor division rounds it down to 2.
# print("m"): This will print the string "m", not the value of the variable. If you want to print the value of m, you need to use print(m).
# output 2

n = 6
n //= 2.5
print("n")
#n = 6: This assigns the value 6 to the variable n.
#n //= 2.5: The // operator performs floor division, which divides the numbers and rounds down to the nearest integer.
#So, n = 6 // 2.5 calculates as follows: 6÷2.5=2.4
#Floor division rounds 2.4 down to 2.
#Therefore, after this operation, n becomes 2. print("n"): This will print the string "n", not the value of the variable. If you want to print the value of n, you should use print(n)

i = 26
i %= 5
print("i")
#i = 26: The variable i is assigned the value 26.
#i %= 5: This is shorthand for i = i % 5. The % operator gives the remainder when i is divided by 5.
#So, i = 26 % 5
#26÷5 equals 5 with a remainder of 1, since 26=5×5+1.
#Therefore, after this operation, i becomes 1.
#print("i"): This will print the string "i", not the value of the variable. To print the value of i, you should use print(i)
# output 1

j = 27.5
j %= 5
print("j")  # output 2.5
#j = 27.5: The variable j is assigned the value 27.5.
#j %= 5: This is shorthand for j = j % 5. The % operator gives the remainder when j is divided by 5.
#So, j = 27.5 % 5 --->27.5÷5=5.5, which means 27.5 is 5.5 times 5
#The remainder when 27.5 is divided by 5 is 27.5−(5×5)=27.5−25=2.5
#operator j becomes 2.5
#This happens because 27.5 % 5 gives the remainder of 2.5 when dividing 27.5 by 5.

v = 1
v += 5
print(v) # output 6
#v = 1: The variable v is assigned the value 1.
#v += 5: This is shorthand for v = v + 5. So, v becomes 1 + 5 = 6.
#print(v): This prints the value of v, which is 6.


y = 10
y -= 11
print(y)  # output -1
#y = 10: The variable y is assigned the value 10.
#y -= 11: This is shorthand for y = y - 11. So, y becomes 10 - 11 = -1.
#print(y): This prints the value of y, which is -1.

n = 4
n *= 5
print(n)  # output 20
#n = 4: The variable n is assigned the value 4.
#n *= 5: This is shorthand for n = n * 5. So, n becomes 4 * 5 = 20.
#print(n): This prints the value of n, which is 20.

j = 10
j /= 4
print(j) # output 2.5
#j = 10: The variable j is assigned the value 10.
#j /= 4: This is shorthand for j = j / 4. So, j becomes 10 / 4 = 2.5.
#print(j): This prints the value of j, which is 2.5.

x = 5
x -= 3
print(y)  # output 2
#x = 5: The variable x is assigned the value 5.
#x -= 3: This is shorthand for x = x - 3. So, x becomes 5 - 3 = 2.
#print(x): This prints the value of x, which is 2.

i = 15
i /= 3
print(i)  # output 5.0
# i = 15: The variable i is assigned the value 15.
# i /= 3: This is shorthand for i = i / 3. So, i becomes 15 / 3 = 5.0.
# print(i): This prints the value of i, which is 5.0.

w = -3
w += 10
print(w)  #output 7
#w = -3: The variable w is assigned the value -3.
#w += 10: This is shorthand for w = w + 10. So, w becomes -3 + 10 = 7.
#print(w): This prints the value of w, which is 7

m = 6
m *= 3
print(m)  # output 18
#m = 6: The variable m is assigned the value 6.
#m *= 3: This is shorthand for m = m * 3. So, m becomes 6 * 3 = 18.
#print(m): This prints the value of m, which is 18.


y = 3
y **= 3
print(y)  #output 27
#y = 3: The variable y is assigned the value 3.
#y **= 3: This is shorthand for y = y ** 3, which means raising y to the power of 3. So, So, y=3 3 =27.
#print(y): This prints the value of y, which is 27.

j = 29
j %= 8
print(j)  #output 5
#j = 29: The variable j is assigned the value 29.
#j %= 8: This is shorthand for j = j % 8, which gives the remainder when j is divided by 8. So,
#j=29%8=5, since 29 divided by 8 gives a quotient of 3 and a remainder of 5.
#print(j): This prints the value of j, which is 5

x = 2
x **= 4
print(x) #output 16
#x = 2: The variable x is assigned the value 2.
#x **= 4: This is shorthand for x = x ** 4, which means raising x to the power of 4. So, x = 2 = 16.
#print(x): This prints the value of x, which is 16.


n = 16
n //= 5
print(n)  # output 3
#m = 29: The variable m is assigned the value 29.
#m //= 8: This is shorthand for m = m // 8, which performs floor division.
# m=29//8=3, since 29, divided by 8 gives 3.625, and floor division rounds it down to 3.m=29//8=3, since 29 divided by 8 gives 3.625, and floor division rounds it down to 3.
#print(m): This prints the value of m, which is 3.


m = 29
m //= 8
print(m)  #output 1
#i = 16: The variable i is assigned the value 16.
#i %= 5: This is shorthand for i = i % 5, which gives the remainder when i is divided by 5. So, i=16%5=1, since 16 divided by 5 gives a remainder of 1.
#print(i): This prints the value of i, which is 1.

i = 16
i %= 5
print(i)  # output 1
#i = 16: The variable i is assigned the value 16.
#i %= 5: This is shorthand for i = i % 5, which gives the remainder when i is divided by 5. So, i=16%5=1, since 16 divided by 5 gives a remainder of 1.
#print(i): This prints the value of i, which is 1.
