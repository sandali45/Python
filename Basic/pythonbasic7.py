name = ["kai", "vanos", "soobin", "kim", "choi"]
newlist = []

for x in name:
  if "a" in x:
    newlist.append(x)

print(newlist)
newlist = [x for x in name if "a" in x]
print(newlist)
newlist = [x for x in name if x != "kai"]
print(newlist)
newlist = [x for x in range(10) if x < 5]
print(newlist)
newlist = [x.upper() for x in name]
print(newlist)
newlist = ['ishi' for x in name]
print(newlist)
newlist = [x if x != "kai" else "soobin" for x in name]
print(newlist)