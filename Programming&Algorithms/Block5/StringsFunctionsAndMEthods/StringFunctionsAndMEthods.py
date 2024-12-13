#Checking the String I
#isalpha() – used to check if all characters in the string are alphabetic
#isnumeric() – used to check if all characters in the string are numeric
str1 = "Hello World!"
print(str1.isalpha())

str2 = "Hello World!"
print(str2.isnumeric())

#Checking the String II
# #islower() – used to check if all characters in the string are lowercase letters
#Example Result
#isuppe – used to check if all characters in the string are uppercase letters

str3 = "Hello World!"
print(str3.islower())

str4 = "Hello World!"
print(str4.isupper())

#Examples I
#Is upper empty?
str4 = ""
print(str4.isupper())

# Is lower empty?
str3 = ""
print(str3.islower())

#Is lower?
str1 = "lowercase"
print(str1.islower())

# Is upper?
str2 = "UPPERCASE"
print(str2.isupper())

#Examples II
#Is numeric empty?
str8 = ""
print(str8.isnumeric())

# Is alphabetic empty?
str7 = ""
print((str7.isalpha()))

#Is alphabetic?
str5 = "abc"
print(str5.isalpha())

# Is numeric?
str6 = "123"
print(str6.isnumeric())

#Modifying the String I
#lower() – used to change all characters in the string to lowercase
#upper() – used to change all characters in the string to uppercase
#Example Result
str5 = "Hello World!"
print(str5.lower())

str6 = "Hello World!"
print(str6.upper())

#Modifying the String II
#capitalize() – used to change the first character in the string to uppercase
#split() – used to split a string at a specified character

#Example Result
str7 = "hello world!"
print(str7.capitalize())

str8 = "Hello World!"
print(str8.split(' '))

#Examples III
#Split
str12 = "r2d2"
print(str12.split('2'))

# Capitalise
str11 = "Monday"
print(str11.capitalize())


#To lowercase
str9 = "January"
print(str9.lower())

# To uppercase
str10 = "January"
print(str10.upper())

#Try It Yourself
#Write a program to display three countries' names entered by the user in alphabetical order
#Note: remember that for strings comparison is case sensitive, so strings should first be turned to lowercase.
#However, the country names printed should be capitalised again.

# Get input from the user for three countries
country1 = input("Enter the name of the first country: ")
country2 = input("Enter the name of the second country: ")
country3 = input("Enter the name of the third country: ")

# Convert the countries to lowercase for case-insensitive comparison
country1_lower = country1.lower()
country2_lower = country2.lower()
country3_lower = country3.lower()

# Sort the countries in alphabetical order
countries = [country1_lower, country2_lower, country3_lower]
countries.sort()

# Capitalize the country names and print them in order
for country in countries:
    print(country.capitalize())


