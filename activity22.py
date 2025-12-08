#MODULES -- Python management

import random

print("GUESSING GAME . . . . . ")
print("+=+=+=+=+=+=+=+=+=+=+=+=+=+\n")

#Setting up random values
ran_val = random.randint(1,5) #Generate random integer value (start m stop)
trying = 0
go = True

while go == True:
    num = eval(input("Guess a random number from 1 to 50 -->"))
    
    trying += 1
    if num == ran_val:
        print("WinWin, SEND PAYMAYA")
        print(f"Random Values is {ran_val}")
        break
    else:
        print("Incorrect, TRY AGAIN")
        continue
print(f"You guessed {trying} times")
