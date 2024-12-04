birds = ["sparrow", "dove", "swan", "duck"]
for i in range(len(birds)):
    print("index of", birds[i], "in birds is", i)

#Processing List II
#Alternatively enumerate() function can be used with the FOR loop to print all of the elements of
#a list and their indices

birds = ["sparrow", "dove","swan", "duck"]
for i, b in enumerate(birds):
    print("index of", b, " in birds is", i)

#Processing Lists III
#Use the WHILE loop to remove any elements
#with a value "a" from the list

word = ["a", "d", "a", "m","a","n","t"]
while "a" in word:
    word.remove("a")
    print("word after removing letter a is:", word)

#List Comprehension
word = ["a", "d", "a", "m", "a", "n", "t"]
letters = [i for i in word if i != "a"]
print("word after removing letter a is:", letters)

#More list Comprehension Example
letters = ["b","2","a","e","a","b","7","c","9"]
b_count = [1 for i in letters if i == "b"]
print(sum(b_count))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = [i * i for i in numbers if i % 2 == 0]
print(even_squares)


# TRY IT
#ty It Yourself
#roblem 1
#rite a program in Python environment
#hat takes an input of 5 numbers and
#Calculates their average
#hint Use an input() function within a loop that
#xecutes 5 times.
#alculate the average by using sum() and len()functions

# Initialize an empty list to store the numbers
# Initialize an empty list to store the numbers
numbers = []

# Counter to track how many numbers have been entered
count = 0

# Use a while loop to take input until 5 numbers are entered
while count < 5:
    num = float(input(f"Enter number {count + 1}: "))
    numbers.append(num)
    count += 1  # Increment the counter

# Calculate the average
average = sum(numbers) / len(numbers)

# Print the result
print("The average of the numbers is:", average)


