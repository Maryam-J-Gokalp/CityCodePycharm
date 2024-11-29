#Write a program in Python environment that
#calculates and prints half of each number from 1 to n
# Function to calculate and print half of each number from 1 to n
def calculate_and_print_halves(n):
    # Loop through each number from 1 to n
    for i in range(1, n + 1):
        half = i / 2  # Calculate half of the number
        print(f"Half of {i} is {half}")  # Print the result

# Example usage:
n = int(input("Enter a number n: "))  # Ask user for input
calculate_and_print_halves(n)  # Call the function with the user input

