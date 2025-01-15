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