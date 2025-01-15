#string #Integer #float # boolean
name="kai vanos"
age=32
gpa=4.42
print("Hello kai vanos")
print(f"Age is {age} ! welcome!")
print(f"GPA is {gpa}!")
wealthy =True
if wealthy:
    print("I am wealthy")
else:
    print("I am not wealthy")
print("--------------------------------------------------------")
x,y,z="kai vanos" ,32 ,"wealthy"
print(x)
print(y)
print(z)
print("--------------------------------------------------------")
#list
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
print("--------------------------------------------------------")
a=5
b=10
print(f"The value is {a+b}")
print("--------------------------------------------------------")
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()
print("--------------------------------------------------------")
x = 5
print(type(x))

#Type casting
gpa=4.0 #float type
print(gpa)#float
print(int(gpa)) #print as an Int

name="kai vanos"
name = bool(name)
print(name)
name2="kai vanos"
print(bool(name2))
name3=""
print(bool(name3))
print("--------------------------------------------------------")
a = "Hello, World!"
print(a[1])
print(a[2])
#Get the characters from position 2 to position 5 (not included):
b = "Hello, World!"
print(b[2:5])
#Get the characters from the start to position 5 (not included):
b = "Hello, World!"
print(b[:5])
print(b[:-2])
#in
txt = "The best things in life are free!"
print("free" in txt)
#no
txt = "The best things in life are free!"
print("expensive" not in txt)