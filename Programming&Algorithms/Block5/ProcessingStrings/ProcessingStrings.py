from itertools import repeat
from pickletools import string1
from tabnanny import check
# == symbol in python use to compare two things and check if exactly the same
check1 = "Strings" == "string"  #<--since the upper and the lower case strings are not the same in python are different
print(check1)  # when print the result of the strings are different and it comes false

check2 = "String" != "string"
print(check2) # output is true

#The result is True because "String" (with uppercase S) is not the same as "string" (with lowercase s). Python treats uppercase and lowercase letters as different, so the != operator sees them as unequal.

repeat1 = "&" * 5
print(repeat1)

repeat2 = "Hello" *3
print(repeat2)

#Examples I
#Empty string
string1 = ''
str2 = ''
print(string1 == str2)

#Repetition with a space
str6 = "a1 "
print(str6 * 3)

# Repetition
str5 = "a1"
print(str5 * 3)

# Quotation marks
str3 = '"Good"'
str4 = 'Good'
print(str3 !=str4)

#Concatenating Strings
# + Operator used to combine two strings into one
#Example
S1 = "Hello"
S2 = "World"
S3 = S1 + S2
print(S3)

#Examples II
#Note: concatenation will not add spaces, like the
#print() function
str7 = "Python" + "is" + "fun"
print(str7)

#Spaces are part of the
str7 = "Python " + "is" + "fun"
print("str8")

#Common Errors in Python
str9 = "string" + 1.0
print(str9)

#Examples III
#Compare concatenation with itself and
#replication twice
str10 = "String"
str11 = str10 + str10
str12 = str10 * 2
if str11 == str12:
    print("Strings are the same")
else:
    print("Strings are not the same")

#Write a program that compares two strings entered by the user
#If the strings are the same, only the first one is printed
#If the strings are different, the strings are concatenated, and the new string is printed

str13 = "muito"
str14 = "Obrigado"

# Concatenate the strings
concatenated_string = str13 + str14

# Compare the strings
if str13 == str14:
    print(str13)
else:
    print(concatenated_string)  # Print the concatenated result
