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
