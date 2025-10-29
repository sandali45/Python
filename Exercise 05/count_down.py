import time

user_time = input("Enter the time in minutes for countdown: ")

sec = int(user_time) * 60
#hr = sec // 3600
#min = (sec % 3600) // 60
for x in range(sec, 0, -1):

    print(f"00:{min:02}:{x:02}")
    time.sleep(1) # the system wait time if i add 5 system after done 60 5s wait for to be 59
    
print("Time's up!")