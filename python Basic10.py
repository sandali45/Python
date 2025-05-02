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
