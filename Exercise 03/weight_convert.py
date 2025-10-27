import math
print("Enter the weight with the value")
weight = input("Enter the weight")
print( "The weight is (KG or Pound)")
st = input("Enter the weight unit(KG or Pound):") 
if st == "KG":
    converted = float(weight) * 2.20462
    print(f"The weight in Pound is: {converted} Pounds")        
elif st == "Pound":
    converted = float(weight) / 2.20462
    print(f"The weight in KG is: {converted} KG")
else:   
    print("Invalid unit. Please enter either 'KG' or 'Pound'.")
