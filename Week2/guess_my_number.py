print ("WELCOME TO GUESS MY NUMBER GAME!!")
print ("You have 5 chances to guess the number....BEST OF LUCK!!")
import random

cnum=random.randint(1,100)

i=0
while i<5:
    unum=int(input("Enter your guess:"))
    if cnum==unum:
        print("Congratulations!! You guessed the number right!")
        quit()
    elif cnum>unum:
        print ("Go higher....")
    else:
        print ("Go lower....")
    i+=1
print("You are unworthy of playing the game, get out of here!!")