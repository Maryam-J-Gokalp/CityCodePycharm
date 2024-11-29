from itertools import count

n = int(input("enter n: "))
total = 0

for count in range(1, n+1):
    if count % 2 == 0:
        continue
        total += count
        print("the count is", count)
        print("the total is", total)


n = int(input("enter n: "))
print("divisors of", n, "are: ")
for count in range(1, n+1):
    if n % count != 0:
        continue
        print("count")


#continue statements for henry is baking cakes, but he is only adding the icing to every other cake
# Let's say Henry is baking 10 cakes
total_cakes = 10

for cake_number in range(1, total_cakes + 1):  # Loop through each cake
    # Check if the cake number is odd
    if cake_number % 2 != 0:  # If the cake number is odd
        continue  # Skip the rest of the loop and go to the next iteration

    # This part will only execute for even cake numbers
    print(f"Adding icing to cake number {cake_number}")  # Add icing to the cake


 #Try It Yourself
#Write a program in Python environment
#that calculates the sum of every third
#number between m and n
#Hint: m and n are given by the user input (using the input
#() function) at the start of the code
#m and n are assumed to be of type int and m < n
#For example, m = 2 and n = 14

# Program to calculate the sum of every third number between m and n

# Get user input for the starting and ending numbers
m = int(input("Enter the starting number (m): "))  # Start number
n = int(input("Enter the ending number (n): "))    # End number

# Initialize a variable to hold the total sum
total_sum = 0

# Loop through the range from m to n
for number in range(m, n + 1):
    # Check if the number is the third number in the sequence
    if (number - m) % 3 == 0:
        total_sum += number  # Add the number to the total sum

# Print the result
print("The sum of every third number between", m, "and", n, "is:", total_sum)
