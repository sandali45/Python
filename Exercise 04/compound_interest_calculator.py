
Total_balance = 0
interest_rate =3.25
Time_period =5

while Total_balance <= 0: #True
    Total_balance = float(input("Enter the total balance: "))
    if Total_balance <= 0:
        print("Invalid input. Please enter a positive number.")


Final_amount = Total_balance * (1+ interest_rate/100) ** Time_period

print(f"The final amount after {Time_period} years is: ${Final_amount:.2f}")