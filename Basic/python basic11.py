# Create a dictionary with brand, model, and year
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)  # Prints the entire dictionary

# Access a specific value using its key
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])  # Outputs: Ford

# If duplicate keys exist, the last one will overwrite the earlier one
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)  # The key "year" will be 2020 (not 1964)

# Use type() to check that it is a dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))  # Outputs: <class 'dict'>

# Create a dictionary using the dict() constructor
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)  # Outputs: {'name': 'John', 'age': 36, 'country': 'Norway'}

#update
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

kid1 = {
  "name" : "Emil",
  "year" : 2004
}
kid2 = {
  "name" : "Tobias",
  "year" : 2007
}
kid3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "kid1" : kid1,
  "kid2" : kid2,
  "kid3" : kid3,
}

print(myfamily)


a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

  a = 33
b = 200

if b > a:
  pass