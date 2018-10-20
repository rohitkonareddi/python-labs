print("WELCOME TO WORD GUESSING GAME!!")

print("To give up at any point in the game, type 'exit'\n")

words=("python", "pneumonoultramicroscopicsilicovolcanoconiosis", "knife", "biology", "artificial", "technology")

import random

t_point=0
t_num=0


def tot_point(point):
    global t_point
    t_point += point
    return t_point


def tot_num(num):
    global t_num
    t_num+=num
    return t_num


play=True

while play:
    guess_w=[]
    player_w=None
    join_w=None
    guess_l=[]
    num=0
    i=0
    original=random.choice(words)
    for letter in original:
        guess_w.append("*")
    while "*" in guess_w:
        i+=1
        join_w=" ".join(guess_w)
        print(join_w)
        guess_l.append(player_w)
        player_w=input("Enter an alphabet from a-z: ")
        if player_w == "exit":
            break
        else:
            for letter in range(len(original)):
                if player_w==original[letter]:
                    guess_w[letter]=player_w

    if "*" not in guess_w:
        num_guess=i-len(original)
        if num_guess > 2:
            point=50
        else:
            point=100
        print("Congratulations!! {} was the chosen word!".format(original))
        print("Your score is", point)
    else:
        point=0
        print("YOu lost!! The word was {}".format(original))
        print("Your score is", point)
    num+=1
    t_num=tot_num(num)
    t_point=tot_point(point)
    user=input("Play again? ")
    if user not in ("yes" or "y"):
        play=False

print("Your total score is", t_point, "out of", t_num*100)