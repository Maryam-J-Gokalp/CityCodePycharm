#Opening times for a bank branch are:    Weekdays: 09:00 - 17:00 Weekend: Closed
  #  Write a program in Python environment that takes  2  inputs, day  of the week and current time, and outputs whether
   # the bank branch is open or closed Note: time can  just  an integer from 0 to 24 hours
from xml.sax.handler import property_interning_dict

day_of_week = input("Please enter the day of the week: ").strip().capitalize()
current_time = int(input("Please enter the current hour (0-24): "))

if day_of_week in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
    if 9 <= current_time < 17:
        print("Bank status: Open")
    else:
        print("Bank status: Closed")
elif day_of_week in ["Saturday", "Sunday"]:
    print("Bank status: Closed")
else:
    print("Error: Invalid day entered.")


x = int(input("Enter a number: "))

if x > 0:
    print(x, "is positive")
    if x % 2 == 0:  # Use modulo operator (%) to check for even numbers
        print("and even")
    else:
        print("and odd")
else:
    print(x, "is not positive")


