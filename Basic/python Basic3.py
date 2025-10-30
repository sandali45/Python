# Create a list of names
thislist = ["Ishi", "kai", "vanos", "sua", "soobin"]

# Sort the list alphabetically in ascending order
thislist.sort()
print(thislist)

# Recreate the list of names
thislist = ["Ishi", "kai", "vanos", "sua", "soobin"]

# Sort the list alphabetically in descending order
thislist.sort(reverse = True)
print(thislist)


print("-----------------------------------------------------------------------")

# Create a list of numbers
thislist = [100, 50, 65, 82, 23]

# Sort the list in ascending order (numerically)
thislist.sort()
print(thislist)

# Recreate the list of numbers
thislist = [100, 50, 65, 82, 23]

# Sort the list in descending order (numerically)
thislist.sort(reverse = True)
print(thislist)


print("-----------------------------------------------------------------------")

# Define a custom sorting function that sorts based on the absolute difference from 50
def myfunc(n):
  return abs(n - 50)

# Recreate the list of numbers
thislist = [100, 50, 65, 82, 23]

# Sort the list using the custom function 'myfunc' as the key
thislist.sort(key = myfunc)
print(thislist)


print("-----------------------------------------------------------------------")

# Create a list of names
thislist = ["Ishi", "kai", "vanos", "sua", "soobin"]

# Sort the list alphabetically in ascending order
thislist.sort()
print(thislist)

# Recreate the list of names with mixed case
thislist = ["ishi", "kai", "vanos", "sua", "soobin"]

# Sort the list alphabetically, ignoring case sensitivity using str.lower as the key
thislist.sort(key = str.lower)
print(thislist)

# Recreate the list of names
thislist = ["Ishi", "kai", "vanos", "sua", "soobin"]

# Reverse the list (reverse the order without sorting)
thislist.reverse()
print(thislist)

print("-----------------------------------------------------------------------")
# Create a list of names
thislist = ["Ishi", "kai", "vanos"]
# Copy the list using the .copy() method
mylist = thislist.copy()
print(mylist)  # Prints the copied list
# Copy the list by creating a new list using the list() function
mylist = list(thislist)
print(mylist)  # Prints the copied list
# Copy the list using slicing ([:] creates a shallow copy of the entire list)
mylist = thislist[:]
print(mylist)  # Prints the copied list
print("-----------------------------------------------------------------------")
# Create two lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
# Combine the two lists using the '+' operator
list3 = list1 + list2
print(list3)  # Prints a new list that combines elements of list1 and list2
# Add each element of list2 to list1 using a for loop and append()
for x in list2:
  list1.append(x)  # Appends each element of list2 to the end of list1
print(list1)  # Prints list1 with elements of list2 added
# Extend list1 by adding all elements of list2 using the extend() method
list1.extend(list2)
print(list1)  # Prints list1 with elements of list2 added again


