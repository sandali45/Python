
item = int(input("Enter the number of items you want to buy: "))
price = float(input("Enter the price per item: "))
quautity = int(input("Enter the quantity of each item: "))  

total_cost = item * price * quautity
print(f"If you bought{item} to {quautity}")
print(f"The total cost of your shopping cart is: ${total_cost}")

