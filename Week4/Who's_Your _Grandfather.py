import random

daddy=[
    "Mattew Bates", "Robert Dickson", "Tony Stark", "Petar Peychev", "Ice Homoseksualac", "Lovro Hident"
]
daddy_daddy=["John Cena", "Randy Dunk", "Donald Greggs", "Dumpston Dump", "Badump dus"]

son_daddy={}

while True:
    print("1. Add son-father pair\n2. Replace son-father pairs\n3.delete son-father pairs\n4.view son-father pairs\n5.Grandfather name\n6. Exit")
    choice=int(input("So what do you want to do? "))
    if choice == 1:
        son_name=input("Give the son's name: ")
        if son_name not in son_daddy:
            daddy_name=random.choice(daddy)
            daddy.remove(daddy_name)
            son_daddy[son_name]=daddy_name
            print("Added successfully\n")
        else:
            print("Son already exists!\n")
    elif choice == 2:
        son_name=input("Give me the son's name: ")
        daddy_name=input("Give me the new daddy's name: ")
        if son_name in son_daddy:
            son_daddy[son_name]=daddy_name
            print("Replaced successfully\n")
        else:
            print("Son doesnt exist!!\n")
    elif choice == 3:
        son_name=input ("Give me the son's name: ")
        del son_daddy[son_name]
        print("Deleted successfully\n")
    elif choice ==4:
        son_name = input("Give me the son's name: ")
        if son_name in son_daddy:
            print(son_daddy[son_name], "\n")
        else:
            print("Son doesnt exist!!\n")
    elif choice == 5:
        son_name = input("Give me the son's name: ")
        if son_name in son_daddy:
            dad = son_daddy[son_name]
            if dad not in son_daddy:
                granddad= random.choice(daddy_daddy)
                daddy_daddy.remove(granddad)
                son_daddy[dad]=granddad
                print(son_daddy[dad], "\n")
            else:
                print(son_daddy[dad], "\n")
        else:
            print("Son Doesnt Exit!!\n")
    else:
        exit()