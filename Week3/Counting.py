print("WELCOME TO THE COUNTING PROGRAM!!")

start=int(input("Start: "))
end=int(input("End: "))
num=int(input("Count by: "))

print("Counting: ")
for i in range(start, end, num):
    print(i, end=" ")

input("\nPress any key to exit....")
