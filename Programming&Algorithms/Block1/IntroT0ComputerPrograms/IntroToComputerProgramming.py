# Convert 5 kilometre into metres
#Know
from functools import total_ordering

number_of_km = 5
#1000m in one km
conversion_factor = 1000
#Calculate the unknown
number_of_m = number_of_km * conversion_factor
#print the answer
print(number_of_m)


# Calculate the total cost of a Book 'costing £7.99 and a Notebook Costing £4.99 if you have a 15& Discout?
#Understand the problem -> formalize and interpret data
# Indentify the know, unknowns, conditions, key parts of the problems draw a diagram if it help
#define book price
# Define the prices of each item
book_price = 7.99
notebook_price = 4.59

# Calculate the total price before applying any discount
total_price = book_price + notebook_price

# Apply a 15% discount to the total price
discount_rate = 0.15
total_discount = total_price * discount_rate  # Calculate the discount amount

# Calculate the final total price after discount
total_price_after_discount = total_price - total_discount

# Print the discount and final total price
print("Total Discount:", total_discount)
print("Total Price after Discount:", total_price_after_discount)


#Problem
# calculate the total cost of a book costing £7.99 and a notebook costing £4.59 if you have a 15% discount?
# Define the prices of each item
book_price = 7.99
notebook_price = 4.59

# Calculate the total price before applying any discount
total_price = book_price + notebook_price

# Apply a 15% discount to the total price
discount_rate = 0.15
new_price_percentage = 100 - discount_rate
total_price = book_price + notebook_price  # Calculate the discount amount

# Calculate the final total price after discount
total_price_after_discount = (book_price + notebook_price)
total_price /= 100
total_price *= new_price_percentage

# Print the discount and final total price
print(total_price)


# problems solve
#Calculate the total cost of 10 apples and 14 oranges, if each apple costs £0.50 and each orange costs £0.40?
# Define the quantity and cost of each item
num_apples = 10           # Number of apples
num_oranges = 14          # Number of oranges
cost_per_apple = 0.50     # Cost per apple in £
cost_per_orange = 0.40    # Cost per orange in £

# Calculate the total cost for each item
total_cost_apples = num_apples * cost_per_apple
total_cost_oranges = num_oranges * cost_per_orange

# Calculate the overall total cost
total_cost = total_cost_apples + total_cost_oranges

# Print the result
print(total_cost)
