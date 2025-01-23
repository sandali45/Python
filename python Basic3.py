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
