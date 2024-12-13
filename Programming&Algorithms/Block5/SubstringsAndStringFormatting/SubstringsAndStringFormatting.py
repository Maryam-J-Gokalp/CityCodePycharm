#Examples I
#Default step
sub_str4 = "Mississippi"[3:6]
print(sub_str4)

# Default start and end
sub_str3 = "Mississippi"[::3]
print(sub_str3)

#Default end and step

sub_str2 = "Python"[4:]
print(sub_str2)

# Default start and step
sub_str1 = "Python"[:2]
print(sub_str1)

#Placeholder
#format() method and curly brackets {} are used to create a placeholder in a string
# The placeholder can then be replaced with a different value of type string
# Example Result
city = "London"
str1 = "Welcome to {}"
print(str1.format(city))

#Placeholder Identifiers
#If multiple placeholders are used for one string, they can be identified using
#Named indexes
#Numbered indexes
#Example Result
# Using Named Indexes
print("{name} is {age}".format(name="John", age=36))  # result: "John is 36"

# Using Numbered Indexes
print("{0} is {1}".format("John", 36))  # result: "John is 36"

#Examples II
# Get the name from the user
str1 = input("Please enter your name: ")
print("{0}, your name is {0}".format(str1))  # Using named format with the same value for both placeholders

# Get two numbers from the user
int1 = int(input("Please enter a number: "))
int2 = int(input("Please enter another number: "))
print("{i1} + {i2} = {sum}".format(i1=int1, i2=int2, sum=int1+int2))

#String Alignment I
#: operator followed by an integer is used within a placeholder to add a specified amount of extra white spaces
#Example Result
str2 = "Hello{:3}World!"
print(str2.format(""))  #Hello World!

str3 = "Hello World{:5}!"
print(str3.format(""))  #Hello World !


#String Alignment II
#< , ^ , > operators are used with the : operator to align the text in the placeholder
#to the left, centre or right respectively
#Example Result
Str4 = "a{:>4}c".format("b")  #result --> a bc
Str5 = "a{:^4}c".format("b")  #result ---> a b c
Str6 = "a{:<4}c".format("b") # -->  ab c

#Examples III
#Align together, centrally and apart
print("{hi: <15} | {hi:>15}|".format(hi = "Hello there"))  # Hello there  | Hello there|
print("{hi:^15} | {hi:^15}|".format(hi = "Hello there"))  # Hello there  | Hello there|
print("{hi: >15} | {hi:>15}|".format(hi = "Hello there"))  # Hello there  | Hello there|

# Read a letter from the user
letter = input("Please enter a letter: ").lower()  # Convert to lowercase for case-insensitive check

# Check if the input is a valid single letter
if len(letter) == 1 and letter.isalpha():
    # Check if the letter is a vowel
    if letter in 'aeiou':
        print(f"{letter} is a vowel.")
    else:
        print(f"{letter} is a consonant.")
else:
    print("Invalid input! Please enter a single letter.")
#Try It Yourself
#Write a program which reads a letter from the user and determines whether it is a vowel or a consonant.
# Implement a check which ensures that the input contains letters only and no digits or other symbols

# Check if the input is a valid single letter
if len(letter) == 1 and letter.isalpha():
    # Check if the letter is a vowel
    if letter in 'aeiou':
        print(f"{letter} is a vowel.")
    else:
        print(f"{letter} is a consonant.")
else:
    print("Invalid input! Please enter a single letter.")
