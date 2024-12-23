#Why use Functions?
#Break larger or complex programs into smaller, more manageable parts
#Easier to develop, manage and debug larger programs
# Code reusability – once written, the function can be called
#within a program multiple times

# Define a function that adds two numbers
def add_numbers(num1, num2):
    result = num1 + num2  # Function body: perform addition
    return result  # Return the result to the caller

# Call the function with two numbers
sum_result = add_numbers(5, 3)

# Print the result of the function call
print("The sum is:", sum_result)
