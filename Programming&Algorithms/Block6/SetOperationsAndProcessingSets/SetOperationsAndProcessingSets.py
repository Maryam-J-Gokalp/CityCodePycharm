#Processing Sets |
#Use an IN keywords to check if the value exists in a set
names = {"Sam", "Jo","Adam","Aaron","Tamar"}
if"Jill" in names:
    print("Jill exists in names")
else:
    print("name not found")

#Processing Sets II
#Use a FOR loop to iterate over a set and print each element
names = {"Sam","Jo","Adam","Aaron","Tamar"}
for n in names:
    print(n)

#Set Operations I
#union() – used to find all values from thensets, without duplicates
#Alternatively, | operator can be used
set1 = {"red","orange","green","blue","purple"}
set2 = {"white", "green", "red", "black","yellow"}
print(set1.union(set2))
print(set1 | set2)

#Set Operations II
# intersection() – used to find all values common to both sets, without duplicates
#Alternatively, & operator can be used
set1 = {"red", "orange","green","blue","purple"}
set2 = {"white", "green", "red","black", "yellow"}
print(set1.intersection(set2))
print(set1 &set2)

#Set Operations III
# difference() – used to find all values found in one set but not the other
#Alternatively, - operator can be used
set1 = {"red", "orange","green","blue","purple"}
set2 = {"white", "green", "red","black", "yellow"}
print(set1.symmetric_difference(set2))
print(set1 ^ set2)

#Try It Yourself
#customer1 = {"oil paints", "lamp", "watch",
#"frame", "kit-kat", "desk"}
#customer2 = {"lamp", "monitor", "home-hub",
#"desk", "canvas"}
#Using the two sets given above, write a program which determines the following :
#• Items bought by both customer1 and customer2
#• All items bought by customer1 and customer2
#• Items bought by customer1 or customer2 but not bought by both
#• Items that customer2 bought but not customer1
#• Remaining items the customer1 had after they returned the items matching with
#customer2
# Define the sets
customer1 = {"oil paints", "lamp", "watch", "frame", "kit-kat", "desk"}
customer2 = {"lamp", "monitor", "home-hub", "desk", "canvas"}

# Items bought by both customer1 and customer2 (intersection)
common_items = customer1 & customer2
print("Items bought by both customer1 and customer2:", common_items)

# All items bought by customer1 and customer2 (union)
all_items = customer1 | customer2
print("All items bought by customer1 and customer2:", all_items)

# Items bought by customer1 or customer2 but not by both (symmetric difference)
exclusive_items = customer1 ^ customer2
print("Items bought by customer1 or customer2 but not by both:", exclusive_items)

# Items that customer2 bought but not customer1 (difference)
customer2_exclusive = customer2 - customer1
print("Items that customer2 bought but not customer1:", customer2_exclusive)

# Remaining items customer1 had after returning matching items with customer2
customer1_remaining = customer1 - customer2
print("Remaining items customer1 had after returning matching items:", customer1_remaining)
