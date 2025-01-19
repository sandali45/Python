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