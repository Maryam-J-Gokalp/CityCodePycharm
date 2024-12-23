#ExampleI
#Opening a text file that does not exist in the current directory
from importlib.metadata import files

f1 = open("write_here.text", "w")
f1.close()

# ExampleII
#Write () method used with the "w" access code
f1 = open("write_here.txt", "w")
f1.write("line 2\n")
f1.close()

#Example III
#Write() method used with the "a" access mode
f1 = open("write_here.txt", "a")    #open file
f1.write("line 2\n")              #write the string
f1.close()

# Common Errors in Python
#Write() method only takes a parameter of type string
f1 = open("write_here.txt", "w")
i = 1
f1.write(str(i))  # Convert the integer to a string before writing
f1.close()

#Example IV
# Write a program that takes text input and
# appends it with a reversed order of the words
text = input("enter some text")
words = text.split(" ")
file = open("text.txt", "a")
for w in range(len(words)):
    file.write(words[len(words)-1 - w] + " ")
    file.write("\n")
    file.close()

# Example V
#Write a program that writes the upper-case letters in the alphabet, one per line, to a file.
file_name = input("Enter the name of the text file: ")
file1 = open(file_name, "w")
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # Corrected the sequence of letters
for s in range(len(alphabet)):
    file1.write(alphabet[s] + "\n")  # Indented properly to be inside the loop
file1.close()


#   Try It Yourself
# Write a program in python
# environment that
# § reads in a file
# § Calculates the number of characters,
# words and lines in the file
# § Writes this information to a
# different text file
# Prompt the user to enter the name of the file to read
file_name = "Brazil fera"  # The file name is now directly specified

# Open the file in read mode and process its contents
with open(file_name, "r") as file:
    content = file.readlines()  # Read all lines from the file

# Calculate the number of lines, characters, and words
lines, chars, words = len(content), sum(len(line) for line in content), sum(len(line.split()) for line in content)

# Prompt the user for the output file name
output_file = input("Enter the name of the output text file: ")

# Write the results to the output file
with open(output_file, "w") as file:
    file.write(f"Lines: {lines}\nWords: {words}\nCharacters: {chars}\n")

# Confirmation message
print(f"Statistics saved to {output_file}.")
