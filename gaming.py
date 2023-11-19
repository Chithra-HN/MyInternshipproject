while True:

    answer = input("What would you like to play?  [YES/NO]")

    if answer.lower().strip() == "yes":

        answer = input("You have Started the game, Would you like to go LEFT or RIGHT?").lower().strip()

        if answer.lower().strip() == "left":
            answer = input("You Encountered a MONSTER, Would you like to Attack or RUN.").lower().strip()

            if answer == "attack":
                answer = input("Choose your weapon between GUN and STICK..").lower().strip()

                if answer == "stick":
                    print("That was not a great IDEA!,,, You LOST")
                elif answer == "gun":
                    print("GOOD CHOICE!...")
                    print("you killed the MONSTER")
                else:
                    print("Time up.... you died!!")

            elif answer == "run":
                print("Run Faster till you reach a parking lot")
                answer = input("You see a car and a plane. Which would like to take?").lower().strip()

                if answer == "plane":
                    print("unfortunately you do not know how to fly game over...")

                else:
                    print("Speed up till 120km/hr to reach the exit")
                    answer = input("Enter the current speed ")
                    if int(answer) >= 120:
                        print("Finally..... YOU MADE IT!!!!")
                    else:
                        print("MONSTER CAUGHT YOU....")

            else:
                print("Time up.....oops you died")


        elif answer == "right":
            print("you encountered a puzzel, would you like to solve it")
            answer = input("Enter your CHOICE [YES/NO]").lower().strip()

            if answer == "yes":
                print("55555558555555")
                answer = input("Enter the position of the different number")
                if int(answer) == 8:
                    print("YES YOU MADE IT!......")
                    print("YOU SOLVED THE PUZZEL AND WON!!!!")
                else:
                    print("Sorry .... You lost!")

            elif answer == "no":
                print("You Are walking aimlessely to right and fall on a fire well...!, You are Injured!......, YOU cannot continue")

            else:
                print("Invalid Choice, You are LOST!")

        else:
            print("Sorry there is no way in the direction of up and down")
    elif answer == "no":
        print("That is bad!......Wanna try again?")
    else:
        print("That is BAD!")