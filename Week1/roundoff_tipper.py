import math

Tot_bill= float(input("Total Bill:"))
Total=round(Tot_bill)
print("Your bill amount(rounded off)=", Total)

input("Press enter to continue....")

tip1= (Total*15)/100
tip2= (Total*20)/100


Tota1 = Tot_bill+tip1
Tota2 = Tot_bill+tip2


print("Your first tip amount=", tip1)
print ("Total amount(incl. tip) =", round(Tota1))

input("Press enter to continue....")

print ("Your second tip amount=", tip2)
print ("Total amount(incl. tip)=", round(Tota2))

