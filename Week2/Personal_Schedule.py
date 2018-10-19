print("WELCOME TO PERSONAL SCHEDULE")

day=None

while day!="holiday":
    uin=input("Enter the day:")
    day=uin.lower()
    if day=="monday":
        print("MONDAY- That's the Python lecture.")
    elif day=="tuesday":
        print("TUESDAY- That's the Technical lecture.")
    elif day=="wednesday":
        print("WEDNESDAY- That's the networking lab.")
    elif day=="thursday":
        print("THURSDAY- That's the STRANDS day.")
    elif day=="friday":
        print("FRIDAY- That's the shopping night.")
    elif day=="saturday":
        print("SATURDAY- That's the party night.")
    elif day=="sunday":
        print("SUNDAY- That's the NETFLIX day.")
    else:
        continue
print("""
        |     |   /-----\   /----\   /----\      --      \    /  
        |     |   |     |   |    |   |    |    /    \     \  /
        |-----|   |     |   |----/   |----/   /------\     \/
        |     |   |     |   | \      | \     /        \    /
        |     |   \-----/   |   \    |   \  /          \  /      """)