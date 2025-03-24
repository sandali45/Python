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

# Example 1: Using a simple for loop to iterate through the list
thislist = ["kai", "vanos", "soobin"]
for x in thislist:
    print(x)  # Prints each item in the list one by one

# Example 2: Using a for loop with range() and indexing
thislist = ["kai", "vanos", "soobin"]
for i in range(len(thislist)):
    print(thislist[i])  # Accesses each element by its index and prints it

# Example 3: Using a while loop to iterate through the list
thislist = ["kai", "vanos", "soobin"]
i = 0
while i < len(thislist):
    print(thislist[i])  # Prints the current item
    i = i + 1           # Moves to the next index

# Example 4: List comprehension with print (short and clean)
thislist = ["kai", "vanos", "soobin"]
[print(x) for x in thislist]  # Iterates through the list and prints each item
