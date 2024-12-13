#Processing Tuples I
#Use an IN keyword to check if the element exists in a tuple
# Processing Tuples I
# Use the IN keyword to check if the element exists in a tuple
birds = ("Hawk", "robin", "swift", "toucan")

# Check if "toucan" exists in the tuple
if "toucan" in birds:
    print("toucan exists in birds")
else:
    print("bird not found")

#Processing Tuples II
#Use a FOR loop to iterate over a tuple and print each element
birds = ("hawk", "robin","swift","toucan")  #The tuple birds contains four elements: "hawk", "robin", "swift",
for t in birds:                                 #The for loop iterates over each element of the tuple.
    print(t)                                  #statement outputs the current value of t to the console.

#Example |
numbers = (2, 3, 5, 7)
product = 1
for n in numbers:
    product *=n
    print(product)

# Example II
# Convert a string into a tuple and then find the
# largest and smallest elements in the tuple
# Converting the input
# sequence into a tuple
my_tuple = tuple(input(("Enter a string: ")))
print(my_tuple)
print("smallest value is:", min(my_tuple))
print("largest value is:", max(my_tuple))

#Example |||
#Check if the number entered in the console is part of the tuple already. if not, append it
tuple1 = (4,2,7,6,5,3)
n = int(input("Enter a number: "))
if n not in tuple1:
    list1 = list(tuple1)
    list1.append(n)
    tuple1 = tuple(list1)

    print(tuple1)

# Initialize an empty list to store car prices
car_prices = []

# Loop to input 7 car prices
# Collect car prices and calculate average
car_prices = [float(input(f"Enter price for car {i + 1}: ")) for i in range(7)]
car_prices_tuple = tuple(car_prices)
average_price = sum(car_prices_tuple) / len(car_prices_tuple)

# Output results
print("\nCar prices:", car_prices_tuple)
print(f"Average car price: {average_price:.2f}")


