import random
print("WELCOME!!\n")

words = ("python", "google", "pneumonoultramicroscopicsilicovolcanoconiosis", "database", "artificial", "intelligence", "biology")

play = True
while play:
    original = random.choice(words)
    num_l = len(original)
    print("It's a ", num_l,"letters word")
    turn = 0
    while turn < 5:
        user_l = input("Enter a letter to check if the letter is in the chosen word: ")
        if user_l in original:
            print("Yes")
        else:
            print("No")
        turn += 1
    user_w = input("Now guess the chosen word: ")
    if user_w == original:
        print("Congratulations!! The chosen word was {}!".format(original), "\n")
    else:
        print("Unlucky!! The chosen word was {}!".format(original), "\n")
    user_c = input("Do you want to play again? ")
    if user_c not in ("yes" or "y"):
        play = False

input("Press any key to exit....")