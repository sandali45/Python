# Sorting a list of strings in ascending (alphabetical) order
thislist = ["kai", "vanos", "choi", "soobin", "ishi"]
thislist.sort()
print(thislist)  # Output: ['choi', 'ishi', 'kai', 'soobin', 'vanos']

# Sorting a list of numbers in ascending order (from smallest to largest)
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)  # Output: [23, 50, 65, 82, 100]

# Sorting a list of strings in descending (reverse alphabetical) order
thislist = ["kai", "vanos", "choi", "soobin", "ishi"]
thislist.sort(reverse = True)
print(thislist)  # Output: ['vanos', 'soobin', 'kai', 'ishi', 'choi']

# Custom sorting using a function:
# Sort based on how close each number is to 50 (smallest difference comes first)
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)  # Output: [50, 65, 23, 82, 100]

# Sorting again alphabetically
thislist = ["kai", "vanos", "choi", "soobin", "ishi"]
thislist.sort()
print(thislist)  # Output: ['choi', 'ishi', 'kai', 'soobin', 'vanos']

# Sorting using str.lower ensures consistent sorting when some elements may have uppercase letters
thislist = ["kai", "vanos", "choi", "soobin", "ishi"]
thislist.sort(key = str.lower)
print(thislist)  # Output: ['choi', 'ishi', 'kai', 'soobin', 'vanos']

# Reversing the order of the list (note: this is not sorting, just flipping the order)
thislist = ["kai", "vanos", "choi", "soobin", "ishi"]
thislist.reverse()
print(thislist)  # Output: ['ishi', 'soobin', 'choi', 'vanos', 'kai']
