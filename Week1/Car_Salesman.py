Tot_price= int(input("Total price of the car:"))
x= int(input("percentage:"))
Dealerprep = 5000
destcharge = 2000
taxlin= (Tot_price*x)/100

Total= Tot_price+taxlin+Dealerprep+destcharge


print("dealer preparation amount=", Dealerprep)
print ("Destination Charge =", destcharge)
print("Tax and license amount =", taxlin)

print("The Total Amount to be paid =", Total)
