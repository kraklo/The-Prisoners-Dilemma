print()
print("  _______   _                _____           _                                       _       ")
print(" |__   __| | |              |  __ \         (_)                                     ( )      ")
print("    | |    | |__     ___    | |__) |  _ __   _   ___    ___    _ __     ___   _ __  |/   ___ ")
print("    | |    | '_ \   / _ \   |  ___/  | '__| | | / __|  / _ \  | '_ \   / _ \ | '__|     / __|")
print("    | |    | | | | |  __/   | |      | |    | | \__ \ | (_) | | | | | |  __/ | |        \__ \\")
print("    |_|    |_| |_|  \___|   |_|      |_|    |_| |___/  \___/  |_| |_|  \___| |_|        |___/")
print()
print("  _____    _   _                                        ")
print(" |  __ \  (_) | |                                       ")
print(" | |  | |  _  | |   ___   _ __ ___    _ __ ___     __ _ ")
print(" | |  | | | | | |  / _ \ | '_ ` _ \  | '_ ` _ \   / _` |")
print(" | |__| | | | | | |  __/ | | | | | | | | | | | | | (_| |")
print(" |_____/  |_| |_|  \___| |_| |_| |_| |_| |_| |_|  \__,_|")
print()
print("                                                        By kraklo")
print()

this_round = 0
com_last = 0
usr_last = 0
usr_score = 0
com_score = 0


def hard():
    if this_round == 0:
        return 1
    return usr_last


def cycle():
    while True:
        choice = input("Choose to (c)ooperate or (d)efect: ")
        choice = choice.lower()
        if choice == 'c':
            return 1
        elif choice == 'd':
            return 0
        else:
            print("Invalid choice.")


for x in range(25):
    usr_choice = cycle()
    com_choice = hard()

    if usr_choice == 1 and com_choice == 1:
        print("You both cooperated! You both earn 3 points!")
        usr_score += 3
        com_score += 3
    elif usr_choice == 1 and com_choice == 0:
        print("You cooperated and the computer defected! You earn nothing!")
        com_score += 5
    elif usr_choice == 0 and com_choice == 1:
        print("You defected and the computer cooperated! You earn 5 points! Very sneaky...")
        usr_score += 5
    elif usr_choice == 0 and com_choice == 0:
        print("You both defected! You both earn a point!")
        usr_score += 1
        com_score += 1
    else:
        print("You aren't supposed to see this. Something must've gone wrong...")

    last_last = usr_last
    usr_last = usr_choice
    com_last = com_choice
    this_round += 1


print("All rounds are now finished.")

if usr_score > com_score:
    print("Congratulations! You win!")
elif usr_score < com_score:
    print("Oh no! You lose!")
else:
    print("It's a tie!")

print("Final scores:")
print("You: {}".format(usr_score))
print("Computer: {}".format(com_score))