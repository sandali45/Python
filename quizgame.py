#1D array
question = [("what is the capital of France?"),#00
            ("what is 2 + 2?")#10
          ] 

#2D array 
Answers = [("A) London", "B) Berlin", "C) Paris", "D) Madrid"), #00
           ("A) 3", "B) 4", "C) 5", "D) 6") #10
          ]

correct_answers = ["C", "B"]
score=0;

#1D array
for x in question:      
    print("------------------------")
    print(x, "\n")

#2D array
    for y in Answers:
        for z in y:
            print(z)
        break
    
    user_answer = input("\nYour answer (A/B/C/D): ").upper()
    if user_answer == correct_answers[question.index(x)]:
        print("Correct!")
        score += 1
    else:
        print("Wrong! The correct answer is", correct_answers[question.index(x)])
print()

print("Your total score is:", score, "out of", len(question))
        
  

  