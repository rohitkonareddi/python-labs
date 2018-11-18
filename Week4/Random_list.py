import random

print("WELCOME TO LIST PRINTING PROGRAM!!")

words = ["python", "pneumonoultramicroscopicsilicovolcanoconiosis", "artificial", "intelligence", "neuroscience"]
index=[0, 1, 2, 3, 4]

while index:
    new_index = random.choice(index)
    print(words[new_index])
    index.remove(new_index)

input("Press any key to exit......")