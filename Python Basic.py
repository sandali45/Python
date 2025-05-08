# Set with mixed data types (note: True is treated as 1, so duplicates may be removed)
thisset = {"kai", "vanos", "soobin", True, 1, 2}
print(thisset)  # Output may have True or 1, but not both because they are the same in a set

# Another set with boolean values; False is treated as 0, True as 1
thisset = {"kai", "vanos", "soobin", False, True, 0}
print(thisset)  # Will show unique values only, False and 0 are treated the same

# Getting the length of a set
thisset = {"kai", "vanos", "soobin"}
print(len(thisset))  # Output: 3

# Creating different sets
set1 = {"kai", "vanos", "soobin"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}  # Only unique values remain

print(set1)  # Output: {'kai', 'vanos', 'soobin'}
print(set2)  # Output: {1, 3, 5, 7, 9}
print(set3)  # Output: {False, True}

# Checking the data type of a set
myset = {"kai", "vanos", "soobin"}
print(type(myset))  # Output: <class 'set'>

# Creating a set using the set() constructor and tuple
thisset = set(("kai", "vanos", "soobin"))  # double brackets: tuple inside set()
print(thisset)  # Output: {'kai', 'vanos', 'soobin'}
