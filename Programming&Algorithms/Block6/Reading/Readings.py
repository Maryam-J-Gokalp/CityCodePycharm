#Text Files
#§ A sequence of strings on disk
#§ All text file types use an encoding syste (e.g., ASCII or UTF-8) to record the characters
#§ Text files can be viewed or modified using a text editor (e.g., Notepad)

#OPEN Function II
# Use an assignment statement, with open() on the right
# open file 'my_file' in reading mode
f1 = open("my_file.txt", "r")
# close file 'my_file’
f1.close()

try:
    # Attempt to open the file in read mode
    with open("my_file.txt", "r") as file:
        # Read the file's contents and display them
        data = file.read()
        print(data)
except FileNotFoundError:
    # Handle the case where the file does not exist
    print("The specified file 'my_file.txt' could not be located.")
except PermissionError:
    # Handle the case where file access is restricted
    print("Access to 'my_file.txt' is denied due to insufficient permissions.")
except Exception as error:
    # Handle any other unexpected errors
    print(f"An error occurred: {error}")

#------------------------->------------------------------------->
# Example II
f1 = open("my_file.txt", "r")
s = f1.read()
f1.close()
print(s)

#readlines () method produces the following list of strings
f1 = open("my_file.txt", "r")
s = f1.readlines()
f1.close()
print(s)

#Example IV
#readline() method produces a string of the first line of text in the text file
f1 = open("my_file.txt", "r")
s = f1.readline()
f1.close()
#Example V
#readline() method can be used again to access subsequent lines from the text file
f1 = open("my_file.txt", "r")
s = f1.readline()  # Read the first line
s = f1.readline()  # Read the second line
f1.close()

# Print both lines
print(s)
print(s)

#Try It Yourself
# Write a program in python environment that
# Reading a text file line by line. Calculates the total of all numbers. read from the file
#Numbers may appear in a sequence. like in the example on the right

# Variable to keep track of the sum of all numbers
sum_of_numbers = 0

# Open the file and read its contents line by line
with open("my_file.txt", "r") as file:
    for line in file:
        # Break the line into individual parts
        items = line.split()

        # Attempt to turn each part into a number and add it to the sum
        for item in items:
            try:
                number = float(item)  # Convert to a float
                sum_of_numbers += number  # Add to the total sum
            except ValueError:
                pass  # Ignore items that are not numbers

# Display the final sum of all numbers
print("The total sum of all numbers in the file is:", sum_of_numbers)


