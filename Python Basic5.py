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
