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