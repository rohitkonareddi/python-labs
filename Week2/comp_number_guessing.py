print("WELCOME TO THE NUMBER GUESSING!!")
import random
i=0
n=1
m=100
while i<11:
    pnum=random.randint(n, m)
    print("Is your number..", pnum, "?")
    uin= input("y/n")
    if uin=="y":
        print("I win!!")
        quit()
    else:
        hin= input("Is your number higher or lower(h/l)?")
        if hin=="h":
            n=pnum
        else:
            m=pnum
    i+=1
print("I feel terrible loosing...goodbye!!")