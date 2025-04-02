fruits = ["kai", "vanos", "choi", "soobin", "ishi"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
fruits = ["kai", "vanos", "choi", "soobin", "ishi"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
