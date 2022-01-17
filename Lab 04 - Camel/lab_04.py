done = False
miles_traveled = 0
drinks_in_canteen = 5
camel_tiredness = 0
natives_behind = -20

print("Welcome to Camel!")
print("You have stolen a camel to make your way across the great Mobi desert.")
print("The natives want their camel back and are chasing you down! Survive your \ndesert trek and out run the natives.\n")

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

    elif player_choice == "E" or "e":
        yn = n
        print("Miles Traveled: " + miles_traveled)
        print("Drinks in canteen" + drinks_in_canteen)
        print("The natives are " + 0 - natives_behind + " miles behind you")
