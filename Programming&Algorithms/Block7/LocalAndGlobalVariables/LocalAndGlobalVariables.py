#Local variables Example
# a variable accessible from anywhere within the program after the point they have been created
#Global variable remains available when the program is executing
def calculate_average(x,y, z):   # function header this function calculates an average of 3 number

    total = x + y + z
    average = total / 3
    return average

num1, num2, num3 = 13,19,27
result = calculate_average(num1,num2,num3)
print(result)

# Global Variable Example
def calculate_average(x, y, z):
    total = x + y + z  # Calculate the total of the inputs
    average = total / 3  # Compute the average
    return average

# Inputs
num1, num2, num3 = 13, 19, 27

# Calculate the average
result = calculate_average(num1, num2, num3)

# Output the result
print(result)

#--------------------------------------------------->

# Common Errors in Python
# Calling a local variable outside of the scope it was c reated in
def fruits():
    quantity_apples = 30
    fruits() # function call
    print("Apples =", quantity_apples)

# Scope of Variable II
def numbers1():
    n = 10
    return n
def numbers2():
    n = 20
    return n

n = numbers1()
print("n =", n)

# Passing Arguments Example
def increment(num1):
    num1 += 1
    print("The number after the increment within the function is:", num1)

    num1 = 0
    print("The original value of the number before the function call is:", num1)
    increment(num1)
    print("The value of the number after the function call is:", num1)

#Try It Yourself
#Write a program in python environment that
#Reads in a string of numbers separated by spaces and stores the numbers in a list
#List is then passed to a function distinct_numbers to create a list of distinct numbers
#The list is then returned to the main program for printing#
# For example: if input = 1 2 4 5 2 3 1 2 3 6, then output = 1 2 4 5 3 6

def distinct_numbers(numbers_list):
    # Using set to get distinct numbers and converting it back to a list
    return list(set(numbers_list))

def main():
    # Read input from the user
    numbers = input("Enter numbers separated by spaces: ")

    # Convert the input string into a list of numbers (strings)
    numbers_list = numbers.split()

    # Call the function to get distinct numbers
    result = distinct_numbers(numbers_list)

    # Print the result
    print("Distinct numbers:", " ".join(result))


# Run the main program
if __name__ == "__main__":
    main()
