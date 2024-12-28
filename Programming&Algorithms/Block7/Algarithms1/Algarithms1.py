# Algorithm Example
def count_vowels(w):
    # List of vowels including both uppercase and lowercase
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    # Initialize the count of vowels
    n = 0

    # Iterate through each letter in the word
    for letter in w:
        if letter in vowels:  # Check if the letter is a vowel
            n += 1  # Increment count if the letter is a vowel

    # Return the final count
    return n

# Main part of the program
word = input("Enter a word: ")
vowel_count = count_vowels(word)
print("Number of vowels:", vowel_count)
