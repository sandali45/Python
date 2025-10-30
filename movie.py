
tickets = { "The NUN :$45",
            "The Conjuring :$35",
            "Annabelle :$25",
            "IT :$40"
           }
total = 0

print("Movie Ticket and prices:")
print("-------------------------")
for tip in tickets:
    print(tip)
print("-------------------------")

while True:
    ans= input("Enter the movie name you want to watch (or type 'q' to finish): ").lower()
    if ans == 'q':
        break
    elif ans == "the nun":
        total += 45
    elif ans == "the conjuring":
        total += 35
    elif ans == "annabelle":
        total += 25
    elif ans == "it":
        total += 40
    
    
print("-------------------------")
print(f"Your total ticket cost is: ${total}")
