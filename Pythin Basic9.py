# Accessing specific tuple item using positive index (index starts at 0)
thistuple = ("kai", "soobin", "vanos")
print(thistuple[1])  # Output: 'soobin' (index 1 is the second item)

# Accessing tuple item using negative index (index starts at -1 for the last item)
thistuple = ("kai", "soobin", "vanos")
print(thistuple[-1])  # Output: 'vanos' (index -1 is the last item)

# Slicing the tuple to get a range of elements (from index 2 to 4, not including 5)
thistuple = ("kai", "vanos", "ishi", "soobin", "choi", "bg", "kim")
print(thistuple[2:5])  # Output: ('ishi', 'soobin', 'choi') - index 2 to 4

# Slicing the tuple to get the first 4 elements (up to index 4, not including 4)
print(thistuple[:4])  # Output: ('kai', 'vanos', 'ishi', 'soobin') - first four items

# Slicing the tuple from index 2 to the end
print(thistuple[2:])  # Output: ('ishi', 'soobin', 'choi', 'bg', 'kim')

# Slicing the tuple with negative indexing, from -4 to -1 (not including -1)
print(thistuple[-4:-1])  # Output: ('soobin', 'choi', 'bg') - last four items but not the last

# Checking if an item exists in the tuple using 'in' keyword
thistuple = ("kai", "vanos", "choi")
if "kai" in thistuple:
  print("Yes, 'kai' is in the fruits tuple")  # Output: Yes, 'kai' is in the fruits tuple

# Original tuple
thistuple = ("kai", "vanos", "soobin")

# Convert tuple to list to modify it (tuples are immutable)
y = list(thistuple)

# Add an item to the list
y.append("kai")

# Convert list back to tuple
thistuple = tuple(y)
# thistuple now is: ('kai', 'vanos', 'soobin', 'kai')


# Start again with the original tuple
thistuple = ("kai", "vanos", "soobin")

# Create a new tuple with one item
y = ("kai",)

# Concatenate the tuples
thistuple += y
# thistuple now is: ('kai', 'vanos', 'soobin', 'kai')

# Print the updated tuple
print(thistuple)  # Output: ('kai', 'vanos', 'soobin', 'kai')


# Start again with the original tuple
thistuple = ("kai", "vanos", "soobin")

# Convert to list to modify
y = list(thistuple)

# Remove 'kai' from the list
y.remove("kai")

# Convert back to tuple
thistuple = tuple(y)
# thistuple now is: ('vanos', 'soobin')
