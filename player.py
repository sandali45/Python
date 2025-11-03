import random

option =("rock ","paper","sissors")
player =0
computer = random.choice(option)

player = input("enter your choice (rock, paper, sissors): ").lower()


print(f"player choice is: {player}")
print(f"computer choice is: {computer}")

if player == computer:
    print("It's a tie!")
elif (player == "rock" and computer == "sissors") or \
     (player == "paper" and computer == "rock") or \
     (player == "sissors" and computer == "paper"):
    print("You win!")
else:           
    print("Computer wins!")
    