#x =int(input())
today = input("Enter day of week? ")
if(today == "Day of week" or today == "Weekdays"):
    print("Today is Weekdays! ")
else:
    print("Today is Weekend, ")

# Input for the day of the week and time
day = input("Enter the day of the week: ").strip().lower()
time = int(input("Enter the current hour in 24-hour format (e.g., 9 for 12 AM, 13 for 5 PM): "))

# Determine if the bank is open or closed
if day in ["monday", "tuesday", "wednesday", "thursday", "friday"]:
    if 9 <= time < 17:  # Bank operates from 9 AM to 5 PM on weekdays
        print("The bank is open.")
    else:
        print("The bank is closed.")
elif day in ["saturday", "sunday"]:  # Closed on weekends
    print("The bank is closed.")
else:  # Handle invalid day inputs
    print("Invalid input for the day. Please enter a valid weekday or weekend.")



#Try It Yourself
#Opening times for a bank branch are:
#Weekdays: 09:00-17:00
#Weekend: Closed
#Write a program in Python environment that takes 2
#inputs, day of the week and current time, and outputs
#whether the bank branch is open or closed
#Note: time can just be an integer from 0 to 24 hours
