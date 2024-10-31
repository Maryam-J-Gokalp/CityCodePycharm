x=2
x=2**x
print(x)

#  1. x variable assign the value 2 then
#  2. the expression 2**x raise power of 2, since x is current 2
# this calculate 2**" equal 4

python_is_cool = True
print(python_is_cool)

# Example II boolean
George = 30 # age
Jack = 41 #age
same_age = Jack == George
print(same_age)

George = 38
Jack = 41
Jack_is_older = Jack > George
print(Jack_is_older)

George = 30
Jack = 41

Jack_is_younger = Jack < George
print(Jack_is_younger)

George = 30
Jack = 41
different_age = Jack != George
print(different_age)

# Example III
George = 30
Jack = 41
thirty_or_more = George >= 30
print('George is 30 or older')
print('thirty_or_more')
thirty_or_more = Jack >= 30
print('Jack is 30 or older')
print(thirty_or_more)

# Example IV
George = 30
Jack = 41
thirty_or_more = George >= 30
print("George is 30 or younger:")
print(thirty_or_more)
thirty_or_more = Jack >= 30
print("Jack is 30 or younger:")
print(thirty_or_more)

#Example V
George = 30
Jack = 41
both_over_fourty = ("George .= 40") and ("Jack .= 40")
print(both_over_fourty)

George = 30
Jack = 41
either_over_fourty = (George >= 40) or (Jack >= 40)
print(either_over_fourty)

#VI
George = 30
Jack = 41

twenty_to_fourty = (George >= 20) and (George <= 40)
print("George is between 20 and 40:")
print(twenty_to_fourty)
twenty_to_fourty = (Jack >= 20) and (Jack <= 40)
print("Jack is between 30 and 40:")
print(twenty_to_fourty)

#VII
George = 30
Jack = 41

not_twenty_to_fourty = (George < 20) or (George >40)
print("George is under 20 or over:")
print(not_twenty_to_fourty)
not_twenty_to_fourty = (Jack < 20) or (Jack > 40)
print("Jack is under 20 or over 40:")
print(not_twenty_to_fourty)

x = 5
y = 7
print(x ==7)

x = 5
y = 7
print(x > y)

x = 5
y = 7
print(x !=y)
x = 5
y = 7
print(x < y)

#II
a = True
b = False
print(a and b)

a = True
b = False
print(a and (not b))