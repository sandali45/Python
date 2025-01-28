# A tuple is a collection that is:
# - Ordered: The items are in a specific sequence.
# - Unchangeable: The items in a tuple cannot be changed after creation.
# - Allows duplicate values: You can have repeated elements in a tuple.
# - Indexed: Each element has a specific position, starting from index 0.

# Example of a tuple
thistuple = ("Sua", "kai", "soobin")
print(thistuple)  # Prints the tuple

# Tuples allow duplicate values
thistuple = ("Sua", "kai", "soobin", "Sua", "kai", "soobin")
print(thistuple)  # Prints the tuple with duplicate elements

# Tuples can hold any data type
thistuple = (1, 2, 3, 4)  # Tuple with integers
print(f"The length is: {len(thistuple)}")  # Prints the length of the tuple

# A tuple with a single element (note the comma is required for it to be recognized as a tuple)
thistuple = ("sua",)
print(type(thistuple))  # Prints <class 'tuple'>

# If you create a tuple without a trailing comma, it will not be recognized as a tuple
thistuple = ("sua")
print(type(thistuple))  # Prints <class 'str'> because it’s interpreted as a string

# Examples of tuples with different data types
tuple1 = ("Sua", "kai", "soobin")  # Tuple with strings
tuple2 = (1, 5, 7, 9, 3)  # Tuple with integers
tuple3 = (True, False, False)  # Tuple with boolean values
print(tuple1)  # Prints tuple1
print(tuple2)  # Prints tuple2
print(tuple3)  # Prints tuple3

print("----------------------------------------------------------------")
# Example tuple
thistuple = ("Sua", "kai", "soobin")
# Accessing the second element (index 1)
print(thistuple[1])  # Output: "kai"
# Accessing the last element using negative indexing
print(thistuple[-1])  # Output: "soobin"
# A longer tuple for slicing examples
thistuple = ("Sua", "kai", "soobin", "vanos", "jun", "choi", "ishi")
# Slicing the tuple: Get elements from index 2 to 4 (5 is excluded)
print(thistuple[2:5])  # Output: ("soobin", "vanos", "jun")
# Slicing the tuple: Get elements from the start to index 3 (4 is excluded)
print(thistuple[:4])  # Output: ("Sua", "kai", "soobin", "vanos")
# Slicing the tuple: Get elements from index 2 to the end
print(thistuple[2:])  # Output: ("soobin", "vanos", "jun", "choi", "ishi")
# Slicing the tuple: Get elements from index -4 to -1 (negative indexing)
print(thistuple[-4:-1])  # Output: ("vanos", "jun", "choi")
# Check if an element exists in the tuple using the `in` keyword
thistuple1 = ("Sua", "kai", "soobin", "vanos", "jun", "choi", "ishi")
if "kai" in thistuple1:  # Case-sensitive check
  print("Yes, 'kai' is in the name tuple")  # This will not print if "Kai" != "kai" simple capital leteers matters
