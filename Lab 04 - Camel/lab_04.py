done = False

def main():
    print("A. Drink from your canteen")
    print("B. Ahead moderate speed")
    print("C. Ahead full speed")
    print("D. Stop for the night")
    print("E. Status check")
    print("Q. Quit")

while done == False:
    main()
    player_choice = input("What is your choice? ")
    if player_choice == "Q" or "q":
        yn = input("Quit? y/n ")
        if yn == "y" or "Y":
            done = True