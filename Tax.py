

from random import randint

check2 = input("Do you want to play a game? ")
if check2 == "yes":
    repeat = True
    lives = 3
    while repeat:
        if lives > 0:
            roll = randint(1, 6) #don't input "a:" or "b:"
            if roll == 6:
                print(f"You rolled a {roll}! Congrats, you won!")
                repeat = False
            else:
                print(f"You rolled a {roll}! which is not a 6, you lose a life")
                lives -= 1
                print(f"lives left: {lives}")
                check1 = input("write 'roll' to roll again or 'stop' to end the game ")
                if check1 == "roll":
                    repeat = True
                else:
                    print("Goodbye :(")
                    repeat = False

        elif lives == 0:
            print("You lost :(")
            repeat = False
else:
    print("Goodbye :(")
    repeat = False
