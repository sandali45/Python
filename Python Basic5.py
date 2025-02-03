# Defining a tuple
thistuple = ("sua", "kai", "soobin")
# Looping through a tuple using a for loop
for x in thistuple:  
  print(x)  # Prints each element in the tuple
# Looping through a tuple using an index-based for loop
thistuple = ("sua", "kai", "soobin")
for i in range(len(thistuple)):  # Loop through indices
  print(thistuple[i])  # Access each element using its index
# Looping through a tuple using a while loop
thistuple = ("sua", "kai", "soobin")
i = 0
while i < len(thistuple):  # Continue looping until i reaches the length of the tuple
  print(thistuple[i])  # Print the current element
  i = i + 1  # Increment i to move to the next element
print("----------------------------------------------------------------");
# Concatenating two tuples
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2  # Combines both tuples into one
print(tuple3)  # Output: ('a', 'b', 'c', 1, 2, 3)
# Duplicating a tuple using multiplication
fruits = ("sua", "kai", "soobin")
mytuple = fruits * 2  # Repeats the tuple elements twice
print(mytuple)  # Output: ('sua', 'kai', 'soobin', 'sua', 'kai', 'soobin')
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(f"The count 5 is: {x}")
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print(f"The index 8 number is: {x}")
print("----------------------------------------------------------------");
# Creating a set, duplicates are automatically removed
thisset = {"sua", "choi", "vanos", True, 1, 2}  
print(thisset)  # Output: {'sua', 'choi', 1, 2, True, 'vanos'}  
# Note that sets do not allow duplicates, so even if you add the same element, it will only appear once.
# Checking the length of a set (number of unique elements)
thisset = {"sua", "kai", "soobin"}
print(len(thisset))  # Output: 3 (3 unique elements)
# Checking the type of a set
myset = {"sua", "kai", "soobin"}
print(type(myset))  # Output: <class 'set'> (The type is 'set')
# Creating a set using the set() constructor with a tuple
thisset = set(("sua", "kai", "soobin"))  # Creating a set from a tuple (Note the double round brackets)
print(thisset)  # Output: {'sua', 'kai', 'soobin'} (Creates a set with the unique elements from the tuple)
print("----------------------------------------------------------------");
# Iterating through a set using a for loop
thisset = {"sua", "kai", "soobin"}
for x in thisset:
  print(x)  # Prints each element in the set (order is unpredictable)
# Checking if an element exists in the set
thisset = {"sua", "kai", "soobin"}
print("sua" in thisset)  # Output: True (because "sua" is in the set)
print("bb" in thisset)  # Output: False (because "bb" is not in the set)
# Checking if an element is NOT in the set
thisset = {"sua", "kai", "soobin"}
print("vanos" not in thisset)  # Output: True (since "vanos" is not in the set)
