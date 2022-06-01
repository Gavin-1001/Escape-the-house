import os
import sys
import time

inventory_array = []

'#TYPING_SPEED'
TYPING_SPEED = 0.025


def typing_effect(text, speed):
    '#https://stackoverflow.com/questions/20302331/typing-effect-in-python'
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)


def beginning_title():
    print()
    typing_effect("#######################################\n", TYPING_SPEED)
    typing_effect("#                                     #\n", TYPING_SPEED)
    typing_effect("#                                     #\n", TYPING_SPEED)
    typing_effect("#                                     #\n", TYPING_SPEED)
    typing_effect("#           ESCAPE THE HOUSE          #\n", TYPING_SPEED)
    typing_effect("#                                     #\n", TYPING_SPEED)
    typing_effect("#            Gavin Shelley            #\n", TYPING_SPEED)
    typing_effect("#                                     #\n", TYPING_SPEED)
    typing_effect("#                                     #\n", TYPING_SPEED)
    typing_effect("#                                     #\n", TYPING_SPEED)
    typing_effect("#######################################\n", TYPING_SPEED)
    print()


def door_art():
    '#https://ascii.co.uk/art/doors'
    typing_effect(
        " __________ \n"
        "|  __  __  |\n"
        "| |  ||  | |\n"
        "| |  ||  | |\n"
        "| |__||__| |\n"
        "|  __  __()|\n"
        "| |  ||  | |\n"
        "| |  ||  | |\n"
        "| |  ||  | |\n"
        "| |  ||  | |\n"
        "| |__||__| |\n"
        "|__________|\n",
        TYPING_SPEED)
    print()


def door_open():
    '#https://ascii.co.uk/art/doors'
    typing_effect(
        " ______________   \n"
        "|\ ___________ /| \n"
        "| |  /|,| |   | | \n"
        "| | |,x,| |   | | \n"
        "| | |,x,' |   | | \n"
        "| | |,x   ,   | | \n"
        "| | |/    |%==| | \n"
        "| |    /] ,   | | \n"
        "| |   [/ ()   | | \n"
        "| |       |   | | \n"
        "| |       |   | | \n"
        "| |       |   | | \n"
        "| |      ,'   | | \n"
        "| |   ,'      | | \n"
        "|_|,'_________|_| \n",
        TYPING_SPEED)
    print()


def house_staircase():
    '#https://ascii.co.uk/art/stairs'
    typing_effect(
        "         -     -                 .      :                          \n"
        "         -     -     -                  |          -               \n"
        " -           -     -    .      .      |    -     -     -           \n"
        "         -     -     -    |      .      |    -     -     -         \n"
        "   -     -     -     -    |      :      |    -     -     -         \n"
        "   -     -     -     -   .|     _|_     |.         -     -         \n"
        "   -     -     -       ._-|             |-_.       -     -         \n"
        "   -     -     -     ._-  |     .       |  -_.     -     -         \n"
        "-.--.--.--.--.--. _ _-_ _ |   E-1-2-3   | _ _-_ _ .--.--.--.--.--.-\n"
        " |  |  |  |  |  |`.| | | ||   _______   || | | |.'|  |  |  |  |  | \n"
        "8888888888888888L_|`.88888|  |   |   |  |88888.'|_J8888888888888888\n"
        "       |:     `888L_|`.|  |  |   |   |  | :|.'|_J888'    :|        \n"
        "       |:       `888L_|`. |  |   |   |: | .'|_J888'      :|        \n"
        "       |:        |`888L_|`.  |   |   |  .'|_J888'        :|        \n"
        "_______<:________|:_`888L_|) |   |   | (|_J888':|________:|________\n"
        "       |:        |:   `888L. |___|___| .J888'  :|        :|        \n"
        "       |:        |:     `88|/_________\|88'    :|        :|        \n"
        " __..--       _.-'        ,|L_________J|.      `-._      ``--..__  \n"
        "'         _.-'            |/___________\|          `-._          ``\n"
        "                        .c|L___________J|c.            `-.         \n"
        "                      .' |/_____________\| `.                      \n"
        "                    .'|  |L_____________J|  |`.                    \n"
        "                  .'  | _/               \_ |  `.                  \n"
        "                .'|   _//                 \\_   |`.                \n"
        "              .'  | _///                   \\\_ |  `.              \n"
        "          _______________________________________________          \n"
        "        .'                                               `.        \n"
        "     .'                                                   `.       \n"
        "    .'                                                       `.\n",
        TYPING_SPEED)


def you_died():
    '#Change the font and text size'
    '##http://www.network-science.de/ascii/'
    '#Ascii character generator'
    typing_effect(
        "__     ______  _    _ \n"
        "\ \   / / __ \| |  | |\n"
        " \ \_/ / |  | | |  | |\n"
        "  \   /| |  | | |  | |\n"
        "   | | | |__| | |__| |\n"
        "   |_|  \____/ \____/ \n", TYPING_SPEED)
    print()
    typing_effect(
        "_____ _____ ______ _____   \n"
        "|  __ \_   _|  ____|  __ \ \n"
        "| |  | || | | |__  | |  | |\n"
        "| |  | || | |  __| | |  | |\n"
        "| |__| || |_| |____| |__| |\n"
        "|_____/_____|______|_____/ \n", TYPING_SPEED)
    from classes import exit_message
    exit_message()


def show_graves():
    '#https://ascii.co.uk/art/graves'
    print(",-=-.   ,-=-.   ,-=-.   ,-=-.   ,-=-.     _     ,-=-.   ,-=-.   \n")
    print("/  +  \ /  +  \ /  +  \ /  +  \ /  +  \  _|1|_  /  +  \ /  +  \ \n")
    print("| ~~~ | | ~~~ | | ~~~ | | ~~~ | | ~~~ | |_ H _| | ~~~ | | ~~~ | \n")
    print("|R.I.P| |R.I.P| |R.I.P| |R.I.P| |R.I.P|   |S|   |R.I.P| |R.I.P| \n")
    print("|_____| |_____| |_____| |_____| |_____|   |_|   |_____| |_____| \n")

    print(",-=-.   ,-=-.   ,-=-.   ,-=-.   ,-=-.   ,-=-.   ,-=-.   ,-=-.  \n")
    print("/  +  \ /  +  \ /  +  \ /  +  \ /  +  \ /  +  \ /  +  \ /  +  \ \n")
    print("| ~~~ | | ~~~ | | ~~~ | | ~~~ | | ~~~ | | ~~~ | | ~~~ | | ~~~ | \n")
    print("|R.I.P| |R.I.P| |R.I.P| |R.I.P| |R.I.P| |R.I.P| |R.I.P| |R.I.P| \n")
    print("|_____| |_____| |_____| |_____| |_____| |_____| |_____| |_____| \n")


def print_inventory():
    print("You inventory:", inventory_array)


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def you_win():
    '#http://www.network-science.de/ascii/'
    # Ascii character generator
    typing_effect(
        "                            _       \n"
        "                           (_)      \n"
        " _   _  ___  _   _    _ _ _ _ ____  \n"
        "| | | |/ _ \| | | |  | | | | |  _ \ \n"
        "| |_| | |_| | |_| |  | | | | | | | |\n"
        " \__  |\___/|____/    \___/|_|_| |_|\n"
        "(____/                              \n",
        TYPING_SPEED)


def graveyard_entrance_gate():
    '#https://ascii.co.uk/art/gates'
    typing_effect(
        "                  _  /)                         \n"
        "                 mo / )                         \n"
        "                 |/)\)                          \n"
        "                  /\_                           \n"
        "                  \__|=                         \n"
        "                 (    )                         \n"
        "                 __)(__                         \n"
        "_________+______/      \______+__________       \n"
        "  __--   |       R.I.P.       |-_-- __          \n"
        "_-- -    | ___ __________ ___ |                 \n"
        "-_-- __  || | | | {|    /| | || __---   -_      \n"
        " --__-   || | | | {|   /|| | ||--        -      \n"
        "         || | | | {|  /||| | ||__--             \n"
        " __-- -__|| | | | {| |}||| | ||--   __--        \n"
        "         ||_|_|_|_{| |}|||_|_||  -__            \n"
        " --__-  -|| | | | {& |}||/ | ||---   __--       \n"
        "         || | | | {| |}|/| | ||-__              \n"
        "--   __--|| | | | {| |}/|| | ||__-- -___        \n"
        "  --     || | | | {| &}||| | ||   __            \n"
        "---   __-|| | | | {| |}||| | ||_---__-   --     \n"
        " -  -_   || | | | {| |}||| | || --              \n"
        " __ejm 97|| | | | {| |}||| | ||_--__-   _---    \n"
        "_________||_|_|_|_{| |}|||_|_||______________   \n"
        "                     |}|/                       \n"
        "                     |}/                        \n"
        "                     |/                         \n",
        TYPING_SPEED)


def search_dining_room():
    typing_effect("There is a set of drawers to your left\n", TYPING_SPEED)
    typing_effect("do you want to open them\n", TYPING_SPEED)
    typing_effect("#1. Yes\n", TYPING_SPEED)
    typing_effect("#2. No\n", TYPING_SPEED)
    openRoomInDiningRoom = input("Chose 1/2\n")

    if (openRoomInDiningRoom == '1'):
        typing_effect("#1.Top drawer\n", TYPING_SPEED)
        typing_effect("#2.Middle drawer\n", TYPING_SPEED)
        typing_effect("#3.Bottom drawer\n", TYPING_SPEED)
        typing_effect("Which drawer would you like to open?\n", TYPING_SPEED)
        chooseDrawerInput = input("Chose one from above\n")

        if (chooseDrawerInput == '1'):
            open_drawer_1()  # drawer is locked
        elif (chooseDrawerInput == '2'):
            ope_drawer_2()  # mob in room
        elif (chooseDrawerInput == '3'):
            open_drawer_3()  # key in this room
        else:
            typing_effect("Please choose 1/2/3\n", TYPING_SPEED)
            typing_effect("to open the drawer\n", TYPING_SPEED)
            search_dining_room()
    elif (openRoomInDiningRoom == '2'):
        typing_effect("You exit the dining room\n", TYPING_SPEED)
        typing_effect("back into the main hall\n",  TYPING_SPEED)
        '#maybe add an option to allow the user to'
        '#exit the house and check the graveyard path'
        from house import house_entrance_options
        house_entrance_options()
    else:
        typing_effect("Please enter 1/2 only please\n", TYPING_SPEED)
        search_dining_room()


def open_drawer_1():
    typing_effect("You go to open the 1st drawer\n", TYPING_SPEED)
    typing_effect("The drawer does not open\n", TYPING_SPEED)
    search_dining_room()


def ope_drawer_2():
    typing_effect("You open the second drawer to\n", TYPING_SPEED)
    typing_effect("find some candles\n", TYPING_SPEED)
    typing_effect("let's check the next drawer\n", TYPING_SPEED)
    print()
    search_dining_room()


def open_drawer_3():
    typing_effect("In this drawer you find a key\n", TYPING_SPEED)
    typing_effect("Put the key in your inventory?\n", TYPING_SPEED)
    typing_effect("#1. Yes, key in inventory\n", TYPING_SPEED)
    typing_effect("#2. No, Leave the key\n", TYPING_SPEED)
    putKeyInInventory = input("Choose 1/2 from above\n")

    if ("key" in inventory_array):
        typing_effect("Key is already in inventory\n", TYPING_SPEED)

    else:
        if (putKeyInInventory == '1'):
            inventory_array.append("key")
            typing_effect("The key is in your inventory\n", TYPING_SPEED)
            print_inventory()
            # if statement to check if the player already has the key in
            # inventory incase they come back again

        elif (putKeyInInventory == '2'):
            typing_effect("You have chosen to leave the key\n", TYPING_SPEED)
        else:
            typing_effect("Enter 1/2 only from the option!\n", TYPING_SPEED)
            open_drawer_3()

    typing_effect("You walk out of the dining room\n", TYPING_SPEED)
    typing_effect("and back into the hall\n", TYPING_SPEED)
    typing_effect("Go back into the dining room?\n", TYPING_SPEED)
    typing_effect("Or continue upstairs?\n", TYPING_SPEED)
    from house import house_entrance_options
    house_entrance_options()


def read_the_rules():
    typing_effect("RULES:\n", TYPING_SPEED)
    typing_effect("1. All user inputs are numerical or Y/N\n", TYPING_SPEED)
    typing_effect("2. All Y/N answers are NOT case sensitive\n", TYPING_SPEED)
    typing_effect("the user can use y/n or Y/N\n", TYPING_SPEED)
    typing_effect("3. Have fun!\n", TYPING_SPEED)
    print()
