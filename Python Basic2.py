a = "kai vanos!"
print(f"lower case: {a.lower()}")
print(f"upper case: {a.upper()}")#place holder 
# f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations
print(a.strip())
print(a.replace("a", "s"))#all same letters replace by this all äs in this will be replaced
print(a.split(","))
print("----------------------------------------------------------------")
a = "kai"
b = "vanos"
c = a + b
print(c)
a = "kai"
b = "vanos"
c = a + " " + b
print(c)
print("----------------------------------------------------------------")
age = 32
txt = "My name is " + c + ", I am " + str(age)
print(txt)
print(f"the total is:{20+20}")
print("----------------------------------------------------------------")
a = 'It\'s alright.' #Single Quote
print(a) 
print("----------------------------------------------------------------")#boolean
print(10 > 9)
print(10 == 9)
print(10 < 9)
#the all are false [output]
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
print("----------------------------------------------------------------")
def myFunction() :
  return False    #false =no | True =Yes

if myFunction():
  print("YES!")
else:
  print("NO!")

print("----------------------------------------------------------------")
  #operations
print((6 + 3) - (6 + 2))
print(100 + 5 * 3)
print(5 + 4 - 7 + 3)

print("----------------------------------------------------------------")
#list
thislist = ["sua", "kai", "soobin"]
print(thislist)

It = ["sua", "kai", "soobin"]
print(len(It))

thislist = list(("sua", "kai", "soobin")) # note the double round-brackets
print(thislist)

#Assess the lists
thislist = ["sua", "kai", "soobin"]
print(f"The index:"+thislist[1]);
print(thislist[:1]);#add: #expect 1 before all shows
print(thislist[1:]);#incuing 1 and all after that
print(thislist[0:2]);#first one inluded but not second and show all other between this range
print(thislist[-2]); #-1:soobin -2:kai -1:sua
thislist = ["sua", "kai", "soobin"]
if "sua" in thislist:
  print("Yes, 'sua' is in the  list")
print("----------------------------------------------------------------")
thislist = ["sua", "kai", "soobin"]
thislist.append("vanos")
print(thislist)
thislist.insert(4, "choi")
print(thislist)
thislist = ["sua", "kai", "soobin"]
tropical = ["Ishi", "vanos", "choi"]
thislist.extend(tropical)
print(thislist)
print("----------------------------------------------------------------")
thislist = ["Ishi", "vanos", "choi"]
thislist.pop(1)  # Removes the element at index 1 ("vanos")
print(thislist)  # Output: ["Ishi", "choi"]

thislist.pop()  # Removes the last element ("choi")
print(thislist)  # Output: ["Ishi"]

del thislist[0]  # Removes the element at index 0 ("Ishi")
print(thislist)  # Output: []

thislist.clear()  # Clears all elements from the list
print(thislist)  # Output: []

del thislist  # Deletes the list


print("----------------------------------------------------------------")
# Create a list of names
thislist = ["Ishi", "vanos", "choi"]
# Iterate through the list using a for loop and print each element
for x in thislist:
  print(x)
print("----------------------------------------------------------------")
# Recreate the list of names
thislist = ["Ishi", "vanos", "choi"]
# Use a for loop with the range and length of the list to access elements by their index
for i in range(len(thislist)):
  print(thislist[i])
print("----------------------------------------------------------------")
# Recreate the list of names
thislist = ["Ishi", "vanos", "choi"]
# Use a while loop to iterate through the list until the end
i = 0  # Initialize the index
while i < len(thislist):  # Loop while the index is less than the list's length
  print(thislist[i])  # Print the current element
  i = i + 1  # Increment the index
print("----------------------------------------------------------------")
# Create another list of names
thislist = ["sua", "kai", "soobin"]
# Use a list comprehension to print each element in the list
[print(x) for x in thislist]
print("----------------------------------------------------------------")
# Create a list of names
names = ["sua", "kai", "soobin", "Ishi", "vanos"]
newlist = []# Initialize an empty list
# Loop through the names and check if 'a' is in each name
for x in names:
  if "a" in x:  # If 'a' is found in the name
    newlist.append(x)  # Add the name to the new list
# Print the new list containing names with 'a'
print(newlist)
# Use a list comprehension to create a new list with names containing 'o'
newlist = [x for x in names if "o" in x]
print(newlist)
# Use a list comprehension to create a new list excluding the name 'sua'
newlist = [x for x in names if x != "sua"]
print(newlist)
# Use a list comprehension to create a list of numbers from 0 to 9
newlist = [x for x in range(10)]
print(newlist)
# Use a list comprehension to create a list of numbers from 0 to 9 where x is less than 5
newlist = [x for x in range(10) if x < 5]
# Use a list comprehension to create a list where every element is the string 'soobie'
newlist = ['soobie' for x in names]
print(newlist)
# Use a conditional expression inside a list comprehension
# Replace 'kai' with 'kailove' in the list, keeping all other names unchanged
newlist = [x if x != "kai" else "kailove" for x in names]
print(newlist)
