def add_points():
    attribute_choice = input("\nWhich attribute? Strength, Health, Wisdom or Dexterity?\n").lower()
    if attribute_choice in character.keys():
        amount_points = int(input("By how much?"))
        if (amount_points > character['points']) or (character['points'] <= 0):
            print("Not enough points!")
        else:
            character[attribute_choice] += amount_points
            character['points'] -= amount_points
    else:
        print("\nThat attribute doesn't exist!\n")


def withdraw_points():
    attribute_choice = input("\nWhich attribute? Strength, Health, Wisdom or Dexterity?\n").lower()
    if attribute_choice in character.keys():
        amount_points = int(input("How much?"))
        if character[attribute_choice] < amount_points:
            print("Not enough points!")
        else:
            character[attribute_choice] -= amount_points
            character['points'] += amount_points
    else:
        print("\nThat attribute doesn't exist!\n")


def print_character():
    for attribute in character.keys():
        print(attribute, " : ", character[attribute])


print("WELCOME TO CHARACTER CREATING PROGRAM")
print("Create a character of your choice using the allotted points to increase the attributes!!")

character = {'name': '', 'strength': 0, 'health': 0, 'wisdom': 0, 'dexterity': 0, 'points': 30}
play = True

character['name'] = input("What is your character's name? ")

while play:
    print("\nYou have ", character['points'], " points left.\n")
    print("1. Add points\n2. Withdraw points\n3. See current attributes\n4. Exit\n")
    choice = input("Choice:")
    if choice == "1":
        add_points()
    elif choice == "2":
        withdraw_points()
    elif choice == "3":
        print_character()
    elif choice == "4":
        play = False
    else:
        pass
