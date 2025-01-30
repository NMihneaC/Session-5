repeat = True
while repeat:
    try:
        gross = input("input your gross monthly salary: ")
        gross = int(gross)
        repeat = False
        childYN = input("Do you have any children? (yes/no) ")
        if childYN == "yes":
            repeat = True
            while repeat:
                try:
                    children = input("How many? (integer only) ")
                    children = int(children)
                    if gross <= 1000:
                        net = gross * (0.9 + (0.01 * children))
                        print(net, "is your net income")
                        repeat = False
                    elif gross <= 2000:
                        net = gross * (0.88 + (0.01 * children))
                        print(net, "is your net income")
                        repeat = False
                    elif gross < 4000:
                        net = gross * (0.86 + (0.005 * children))
                        print(net, "is your net income")
                        repeat = False
                    else:
                        net = gross * (0.82 + (0.005 * children))
                        print(net, "is your net income")
                        repeat = False
                except:
                    print("try again, this time input an numerals (integers)")
                    repeat = True
        else:
            if gross <= 1000:
                net = gross * 0.9
                print(net, "is your net income")
                repeat = False
            elif gross <= 2000:
                net = gross * 0.88
                print(net, "is your net income")
                repeat = False
            elif gross < 4000:
                net = gross * 0.86
                print(net, "is your net income")
                repeat = False
            else:
                net = gross * 0.82
                print(net, "is your net income")
                repeat = False
    except:
        print("I asked you to input an integer, please do so")
        repeat = True