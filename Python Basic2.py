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