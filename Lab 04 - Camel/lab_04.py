done = False
miles_traveled = 0
drinks_in_canteen = 5
camel_tiredness = 0
natives_behind = -20
player_choice = ""
print("Welcome to Camel!")
print("You have stolen a camel to make your way across the great Mobi desert.")
print("The natives want their camel back and are chasing you down! Survive your \ndesert trek and out run the natives.\n")

def main():
    global player_choice
    print("A. Drink from your canteen")
    print("B. Ahead moderate speed")
    print("C. Ahead full speed")
    print("D. Stop for the night")
    print("E. Status check")
    print("Q. Quit")
    player_choice = input("What is your choice? ").upper()

while done == False:
    main()

    if player_choice == "Q":
        yn = input("Quit? y/n ").upper()
        if yn == "Y":
            done = True