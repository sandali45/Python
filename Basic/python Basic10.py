# Basic unpacking: Number of variables matches the number of tuple elements
fruits = ("kai", "vanos", "soobin")
(green, yellow, red) = fruits
print(green)   # Output: kai
print(yellow)  # Output: vanos
print(red)     # Output: soobin

# Using * to collect remaining items into a list
fruits = ("kai", "vanos", "soobin", "ishi", "choi")
(green, yellow, *red) = fruits
print(green)   # Output: kai
print(yellow)  # Output: vanos
print(red)     # Output: ['soobin', 'ishi', 'choi']

# Using * in the middle to collect multiple middle values
fruits = ("kai", "vanos", "soobin", "choi", "ishi")
(green, *tropic, red) = fruits
print(green)   # Output: kai
print(tropic)  # Output: ['vanos', 'soobin', 'choi']
print(red)     # Output: ishi

# Looping through a tuple using a for loop (direct element access)
thistuple = ("kai", "vanos", "soobin")
for x in thistuple:
  print(x)  # Prints each item one by one: kai, vanos, soobin

# Looping through the tuple using range and indexing
thistuple = ("kai", "vanos", "soobin")
for i in range(len(thistuple)):
  print(thistuple[i])  # Prints elements using index: kai, vanos, soobin

# Looping using while loop with manual index
thistuple = ("kai", "vanos", "soobin")
i = 0
while i < len(thistuple):
  print(thistuple[i])  # Prints each item: kai, vanos, soobin
  i = i + 1
