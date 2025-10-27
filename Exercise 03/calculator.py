import math

print("Welcome to the Calculator!")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

operator = input("Enter operator (+, -, *, /, ^): ")

if operator == '+':
    answer =num1+num2
    print("The answer is: " + str(answer))

elif operator == '-':
    answer =num1-num2
    print("The answer is: " + str(answer))
elif operator == '*':
    answer =num1*num2
    print("The answer is: " + str(answer))
elif operator == '/':
    answer =num1/num2
    print("The answer is: " + str(answer))
elif operator == '^':
    answer =num1**num2
    print("The answer is: " + str(answer))
else:
    print ("Invalid operator")

 

