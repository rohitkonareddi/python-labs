print("WELCOME TO WORD JUMBLE")

words=("book","pneumonoultramicroscopicsilicovolcanoconiosis","python","biology","knife","university")

import random

point=100
play=True
while play:
    word=random.choice(words)
    original=word

    jumble=" "
    while word:
        position=random.randrange(len(word))
        jumble +=word[position]
        word=word[:position]+word[(position+1):]

    print("Guess the word below: \n", jumble)

    i=0

    while i<6:
        guess=input("Enter your guess: ")
        if guess==original:
            print("HOORAY!! You nailed it!")
            break
        else:
            uh=input("Do you want a hint?(y/n): ")
            if uh=="y":
                point=point-10
                if original=="book":
                    print("It,s a everyday accessory!")
                elif original=="pneumonoultramicroscopicsilicovolcanoconiosis":
                    print("It's a lung disease caused dut to silica dust!")
                elif original=="python":
                    print("It's a popular programming language!")
                elif original=="biology":
                    print("It's the study of living things!")
                elif original=="knife":
                    print("It's a kitchen tool!")
                else:
                    print("A place to pursue your higher education!")
        i+=1
        if i==6:
            print("The word is {}!".format(original))
    user_c=input("Do you want to play again? ")
    if user_c not in ("yes" or"y"):
        play=False
print("Your total points is ", point)