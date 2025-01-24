
name = input("Como te llamas? ")
if name == "Max":
    print("Who let you out of your cage ")
else:
    repeat = True
    while repeat:
        age2 = input(f"How old are you {name}? ")
        try:
            age2 = int(age2)
            check = input(f"{name}, where you born in {2024-age2}? ")
            if check == "yes":
                print("Nice")
                repeat = False
            else:
                print("you're wrong")
                repeat = False
        except:
            print("Fuck you,Invalid Response")
            print("integers only")
            Again = input("Do you want to try again? ")
            if Again == "yes":
                print("Okay")
            else:
                print(":(")
                repeat = False

# repeat = True
# while repeat:
#     user_input = input("Enter 'exit' to quit: ")
#     if user_input == "exit":
#         repeat = False
#     else:
#         print("You entered:", user_input)


