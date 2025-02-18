# Removing an element using remove()
thisset = {"kai", "vanos", "soobin"}
thisset.remove("kai")  # Removes "kai" from the set
print(thisset)  # Output: {'vanos', 'soobin'}
# Removing an element using discard()
thisset.discard("soobin")  # Removes "soobin" from the set
print(thisset)  # Output: {'vanos'}
# Removing an element using pop()
thisset = {"kai", "vanos", "soobin"}
x = thisset.pop()  # Removes and returns a random element (since sets are unordered)
print(x)  # Prints the removed element
print(thisset)  # Prints the remaining set after pop()
# Clearing all elements from a set
thisset = {"kai", "vanos", "soobin"}
thisset.clear()  # Empties the set but keeps the variable
print(thisset)  # Output: set() (empty set)
# Deleting the entire set
thisset = {"kai", "vanos", "soobin"}
del thisset  # Deletes the set completely
# Trying to print the deleted set will cause an error
print(thisset)  # Error: NameError: name 'thisset' is not defined
