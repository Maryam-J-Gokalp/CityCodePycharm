#Creating a Dictionary
#Defined inside curly brackets {} with colons separating a key from its value
#Commas separate the key-value pairs
# dictionary with 3 key-value pairs
from traceback import print_exception

d = {1: "b", 2: "m", 3: "c"}
print(d)

#dictionary with one pair
singer = {1 : "Sam Smith"}
print(singer)

#empty dictionary
empty_dictionary = {}
print(empty_dictionary)

#Dictionary from a Sequence
#dict() – is used to convert a sequence of pairs into a dictionary
#Works on lists and tuples

d1 = dict(((1, "a"), (2, "b"), (3, "c")))
print(d1)

d2 = dict([[1, "a"], [2, "b"], [3, ""]])
print(d2)

d3 = dict([(1, "a"), (2, "b"), (3, "c")])
print(d3)

# Accessing Values in Dictionaries
# To access a value, use its associative key
# Use the key inside square brackets - [<key>]
# Alternatively, use the get() method

# Example Result
d4 = {1: 'a', 2: 'b', 3: 'c'}
print(d4[1])  # Output: 'a'

d5 = {'a': 1, 'b': 2, 'c': 3}
print(d5.get('c'))  # Output: 3


#Modifying Values in Dictionaries
#To modify a value, use its associative key with new value to be assigned
#Example Result
d6 = {1: True, 2: False, 3: True}
d6[1] = False

d7 = {'a': 1, 'b': 2, 'c': 3}
d7['a'] = 5

#Removing Entries
#pop() - used to remove a value with the specified key, returns the value of the key being removed
#del <dictionary name> [<key>] -used to remove a value with the specified key, does not return anything

d8 = {1: True, 2: False, 3: True}
d8.pop(1)

d9 = {'a': 1, 'b': 2, 'c': 3}
del d9['b']

#Try It Yourself
#Enter and run the following statementsin the python environment
d = {"movie": "Forrest Gump", "artist": "Tom Hanks", "year": 1994}
print(d["artist"])  # Output: "Tom Hanks"
print(d.get("year"))  # Output: 1994

d["artist"] = "Robin Wright"
print(d)  # Output: {'movie': 'Forrest Gump', 'artist': 'Robin Wright', 'year': 1994}

d.pop("artist")
print(d)  # Output: {'movie': 'Forrest Gump', 'year': 1994}





