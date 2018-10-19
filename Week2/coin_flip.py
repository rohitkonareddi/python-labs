print("Welcome to coin flip!!")
import random
i=1
hnum=0
tnum=0
result= ("H", "T")
while i<=100:
    f_result=random.choice(result)
    if f_result == "H":
        hnum+=1
    else:
        tnum+=1
    i+=1

print ("The number of heads is:", hnum)
print ("The number of tails is:", tnum)