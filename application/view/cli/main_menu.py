def menu():
    print("*" * 50)
    print("Welcome to the APP")
    print("*" * 50)
    print()
    print("1. Add record")
    print("2. Show all records")
    print("3. Delete records")
    print()
    print("9. Quit")
    while True:
        pick = input("> ")
        if pick in "1239":
            break
        print("Valid options are 1, 2, 3, or 9")
    return pick
