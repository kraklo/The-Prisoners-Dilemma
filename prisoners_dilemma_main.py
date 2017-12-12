from random import randint

try:
    input = raw_input
except NameError:
    pass

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
last_last = 0
usr_score = 0
com_score = 0


def easy():
    return randint(0,1)

def normal():
    if this_round == 0:
        return 1
    elif (com_last == 1 and usr_last == 0) or (com_last == 0 and usr_last == 0):
        return 0
    else:
        return 1


def hard():
    if this_round == 0:
        return 1
    return usr_last


def extreme():
    if this_round == 0 or this_round == 1:
        return 1
    elif usr_last == 0 and last_last == 1:
        return 1
    else:
        return usr_last


def impossible():
    if this_round == 0:
        return 1
    elif (usr_last == 1 and com_last == 1) or (usr_last == 0 and com_last == 0):
        return 1
    else:
        return 0


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


ok = ['c', 'e', 'n', 'h', 'x', 'i']
valid = False

while not valid:
    difficulty = input("Select a difficulty - (c)akewalk, (e)asy, (n)ormal, (h)ard, e(x)treme or (i)mpossible: ")
    if difficulty in ok:
        valid = True
    else:
        print("That is not a valid difficulty.")

valid = False
rounds = 0

while not valid:
    try:
        rounds = int(input("Select a number of rounds to play: "))
        valid = True
    except ValueError:
        print("That is not a number.")


for x in range(rounds):
    usr_choice = cycle()
    com_choice = 0

    if difficulty == 'e':
        com_choice = easy()
    elif difficulty == 'n':
        com_choice = normal()
    elif difficulty == 'h':
        com_choice = hard()
    elif difficulty == 'x':
        com_choice = extreme()
    elif difficulty == 'i':
        com_choice = impossible()
    elif difficulty == 'c':
        com_choice = 1

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