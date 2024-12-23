#Define Function Example I
from functools import total_ordering


def print_message():
    print("Hello World")

    # User Defined Function Example II


def calculate_total(x, y):  # Corrected the function definition syntax
    total = x + y  # Perform the addition
    return total  # Return the result


num1 = 101
num2 = 110
my_total = calculate_total(num1, num2)  # Call the function with arguments
print("Total of", num1, "and", num2, "=", my_total)  # Print the result

# Docstring Example
def calculate_average(x, y, z):  # Corrected the function header with a colon
    """
    This function takes three numbers as inputs,
    calculates their sum, and returns the average.
    """
    total = x + y + z
    average = total / 3
    return average

num1, num2, num3 = 13, 19, 27
result = calculate_average(num1, num2, num3)
print(result)   #19.666666666666668


# Creating a Custom Function Example II
# Why use a user defined function here?
# § Area and perimeter can be calculated for
# different values of the inputs i.e., radius
# § Program can be decomposed into two functions: one to
# calculate the area and one to calculate the circumference
# § Better management and reusability

# Program to calculate area and perimeter of a circle using custom functions
from math import pi  # Importing only the required constant

def area_of_circle(radius):
    """
    Calculates and returns the area of a circle given its radius.
    """
    return pi * (radius ** 2)

def circumference_of_circle(radius):
    """
    Calculates and returns the circumference of a circle given its radius.
    """
    return 2 * pi * radius

# User input for the radius
circle_radius = float(input("Please enter the radius of the circle: "))

# Calculating the area and circumference using the functions
circle_area = area_of_circle(circle_radius)
circle_circumference = circumference_of_circle(circle_radius)

# Outputting the results
print(f"Circle radius: {circle_radius}")
print(f"Circle area: {circle_area:.2f}")
print(f"Circle circumference: {circle_circumference:.2f}")




#Creating a Custom Function Example III
#Algorithm
#1. read in radius
#2. function calculate_area(r)
#3. return pi * r * r
#4. function calculate_circumference (r)
#5. return pi * 2 * r
#6. calculate_area(radius)
#7. calculate_ circumference (radius)
#8. display results


from math import pi  # Import the "pi" value (approximately 3.14) from the math module.

# Define a function to calculate the area of a circle
def calculate_area(r):  # 'r' is the radius passed to this function.
    return pi * r ** 2  # The formula for the area of a circle: π × radius².

# Define a function to calculate the circumference of a circle
def calculate_circumference(r):  # 'r' is the radius passed to this function.
    return 2 * pi * r  # The formula for the circumference: 2 × π × radius.

# Ask the user to input the radius of the circle
radius = float(input("Enter radius: "))  # Convert the input to a decimal number (float).

# Use the functions to calculate the area and circumference and display them
print(f"Area: {calculate_area(radius):.2f}, Circumference: {calculate_circumference(radius):.2f}")
# Call the functions with the user-provided radius.
# Display the results rounded to 2 decimal places using {:.2f}.

#Creating a Custom Function Example IV
pi = 3.14
def calculate_area(r):
    global pi
    circle_area = pi * r * r
    return circle_area
def calculate_circumference(r):
    global pi
    circumference = 2 * pi * r
    return circumference
radius = float(input("Enter a value for radius"))
print("The area is: {:.2f}".format(calculate_area(radius)))
print("The circumference is: {:.2f}".format(calculate_circumference(radius)))


#Try It Yourself I
#Write a function in python environment that
#determines how many days there are in a particular month
#The input should be read as the month name (assuming a non-leap year) in the main program.
# Function to determine the number of days in a month
def get_days_in_month(month, year=None):
    # Dictionary that stores the number of days in each month for a non-leap year
    days_in_month = {
        "january": 31, "february": 28, "march": 31, "april": 30,
        "may": 31, "june": 30, "july": 31, "august": 31,
        "september": 30, "october": 31, "november": 30, "december": 31,
    }

    # If the month is not in the dictionary, return "Invalid month."
    if month not in days_in_month:
        return "Invalid month."

    # If the month is February and the year is provided, check if it's a leap year
    if month == "february" and year:
        # Leap year check: divisible by 4, but not 100 unless divisible by 400
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            # If it's a leap year, February has 29 days
            return f"There are 29 days in {month.capitalize()}."

    # If the month is valid and not February (or February in a non-leap year), return the number of days in that month
    return f"There are {days_in_month[month]} days in {month.capitalize()}."

# Main program starts here
# Get the month name from the user and convert it to lowercase to ensure uniformity
month = input("Enter the month: ").lower()

# If the month is February, ask for the year to check for leap year
if month == "february":
    # Get the year from the user
    year = int(input("Enter the year: "))
    # Print the result from the function, considering leap year
    print(get_days_in_month(month, year))
else:
    # For months other than February, simply print the number of days
    print(get_days_in_month(month))




# Try It Yourself II
# Extend the above exercise by including a
# second parameter in the function passing in
# the year.
# Then, determine whether the year is a leap
# year or not and subsequently adjust the value
# of the number of days in February accordingly
# Hint: assume all years divisible by 4 are leap years

def days_in_month(month, year):  # Function to find the number of days in a month for a given year
    days = {  # Dictionary for days in each month (non-leap year)
        "january": 31, "february": 28, "march": 31, "april": 30,
        "may": 31, "june": 30, "july": 31, "august": 31,
        "september": 30, "october": 31, "november": 30, "december": 31
    }

    if month == "february" and year % 4 == 0:  # Check if it's February and a leap year
        return 29  # February has 29 days in a leap year

    return days.get(month.lower(), "Invalid month")  # Return days or indicate an invalid month


# Take input for the month and year
month = input("Enter the month: ").lower()  # Prompt user for the month (case insensitive)
year = int(input("Enter the year: "))  # Prompt user for the year

# Use the function to determine days and print the result
result = days_in_month(month, year)  # Call the function
print(f"Days in {month.capitalize()}: {result}")  # Display the days or an error message





