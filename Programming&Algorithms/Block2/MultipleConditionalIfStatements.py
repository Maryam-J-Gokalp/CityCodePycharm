x = int(input())
if(x > 0 and x < 5):
    print(x, "is in the range")
else:
    print(x, "is not in the range")

#Examples
x = int(input("enter x: "))
y = int(input("enter y: "))
if(x > 0 and y > 0):
    print("both numbers are not positive")

# Examples
today = input("which day is today? ")
if(today == "Saturday" or today == "Sunday"):
    print("Today is a weekend! ")
else:
    print("Today is a weekend, ")

#A program that takes two integers as inputs and
#outputs the sum of the integers if both are positive or
#“incorrect input” message otherwise
x = int(input("Enter x: "))
y = int(input("Enter y: "))
if x > 0 and y > 0:
    print("The sum is:", x + y)
else:
    print("Incorrect input")

#A program that outputs the number of days in a given
#month (assume that it is not a leap year)
month = input("Enter the month: ")
if month == "January" or month == "March" or month == "May" or month == "July" or month == "August" or month == "October" or month == "December":
    print("31 days")                             #Months with 31 days: January, March, May, July, August, October, December
elif month == "April" or month == "June" or month == "September" or month == "November":
    print("30 days")                                 #Months with 30 days: April, June, September, November.
elif month == "February":                            #February is assumed to have 28 days (since it's not a leap year)
    print("28 days (Non-leap year)")
else:
    print("Invalid month name")

month= input("number of days in a given month? ")
if(month == "January" or month == "March" or month == "May" or month == "July" or month == "August" or month == "October" or month == "December"):
      print("31 days")                             #Months with 31 days: January, March, May, July, August, October, December:
elif month == "April" or month == "June" or month == "September" or month == "November":
     print("30 days")  # Months with 30 days: April, June, September, November.
elif month == "February":                            #February is assumed to have 28 days (since it's not a leap year)
    print("28 days (Non-leap year)")
else:
    print("Assume that it is not a leap year, ")