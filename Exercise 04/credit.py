
credit_num =input("Enter your credit card number: ")


length_num = len(credit_num)

if  length_num < 13:
    print("Invalid input")

else:
    print(f"xxxx-xxxx-xxxx{credit_num[-5:]}")


print(f"The number: {credit_num[::-1]}")