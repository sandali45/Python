food = []
price = []
total = 0

while True:
    item = input("Enter the food item you want to add to the cart (or type 0 to finish): ")
    if item == '0':
        break
    cost = float(input(f"Enter the price of {item}: "))
    #this code needed this the user input item we put to list
    food.append(item)
    price.append(cost)
    
    total += cost

print(f"The total price of items in your cart is: ${total:.2f}")
print("------------Your cart-----------------")

for x in food:
    print(x)
print(f"Total price: ${total:.2f}")
