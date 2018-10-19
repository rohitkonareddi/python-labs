print ("WELCOME TO FORTUNE COOKIE!!")

import random

fortune= ("A friend asks only for your time not your money.",
          "Your high-minded principles spell success", "Your shoes will make you happy today.",
          "Now is the time to try something new.", "Your ability for accomplishment will follow with success")

print ("Your fortune for today is....")

t_for=random.choice(fortune)

print (t_for)