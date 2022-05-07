import os
import sys
import time

inventory_array = []

TERMINAL_TYPING_SPEED = 0.025



def terminal_typing_effect(text, speed):
    # https://stackoverflow.com/questions/20302331/typing-effect-in-python
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)


def beginning_title():
    print()
    terminal_typing_effect("#######################################\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("#                                     #\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("#                                     #\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("#                                     #\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("#           ESCAPE THE HOUSE          #\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("#                                     #\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("#            Gavin Shelley            #\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("#                                     #\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("#                                     #\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("#                                     #\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("#######################################\n", TERMINAL_TYPING_SPEED)
    print()


def door_art():
    # https://ascii.co.uk/art/doors
    terminal_typing_effect("            __________ \n"
                           "           |  __  __  |\n"
                           "           | |  ||  | |\n"
                           "           | |  ||  | |\n"
                           "           | |__||__| |\n"
                           "           |  __  __()|\n"
                           "           | |  ||  | |\n"
                           "           | |  ||  | |\n"
                           "           | |  ||  | |\n"
                           "           | |  ||  | |\n"
                           "           | |__||__| |\n"
                           "           |__________|\n", TERMINAL_TYPING_SPEED)
    print()


def door_open():
    # https://ascii.co.uk/art/doors
    terminal_typing_effect(" ______________   \n"
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
                           "|_|,'_________|_| \n", TERMINAL_TYPING_SPEED)
    print()


def house_staircase():
    # https://ascii.co.uk/art/stairs
    terminal_typing_effect(
        "         -     -                 .      :                              \n"
        "         -     -     -                  |          -                   \n"
        " -           -     -    .      .      |    -     -     -               \n"
        "         -     -     -    |      .      |    -     -     -             \n"
        "   -     -     -     -    |      :      |    -     -     -             \n"
        "   -     -     -     -   .|     _|_     |.         -     -             \n"
        "   -     -     -       ._-|             |-_.       -     -             \n"
        "   -     -     -     ._-  |     .       |  -_.     -     -             \n"
        "-.--.--.--.--.--. _ _-_ _ |   E-1-2-3   | _ _-_ _ .--.--.--.--.--.-    \n"
        " |  |  |  |  |  |`.| | | ||   _______   || | | |.'|  |  |  |  |  |     \n"
        "8888888888888888L_|`.88888|  |   |   |  |88888.'|_J8888888888888888    \n"
        "       |:     `888L_|`.|  |  |   |   |  | :|.'|_J888'    :|            \n"
        "       |:       `888L_|`. |  |   |   |: | .'|_J888'      :|            \n"
        "       |:        |`888L_|`.  |   |   |  .'|_J888'        :|            \n"
        "_______<:________|:_`888L_|) |   |   | (|_J888':|________:|________    \n"
        "       |:        |:   `888L. |___|___| .J888'  :|        :|            \n"
        "       |:        |:     `88|/_________\|88'    :|        :|            \n"
        " __..--       _.-'        ,|L_________J|.      `-._      ``--..__      \n"
        "'         _.-'            |/___________\|          `-._          ``    \n"
        "                        .c|L___________J|c.            `-.             \n"
        "                      .' |/_____________\| `.                          \n"
        "                    .'|  |L_____________J|  |`.                        \n"
        "                  .'  | _/               \_ |  `.                      \n"
        "                .'|   _//                 \\_   |`.                    \n"
        "              .'  | _///                   \\\_ |  `.                  \n"
        "          _______________________________________________              \n"
        "        .'                                               `.            \n"
        "     .'                                                   `.           \n"
        "    .'                                                       `.        \n", TERMINAL_TYPING_SPEED)


def you_died():
    # Change the font and text size
    ##http://www.network-science.de/ascii/
    # Ascii character generator
    terminal_typing_effect(
        "__     ______  _    _ \n"
        "\ \   / / __ \| |  | |\n"
        " \ \_/ / |  | | |  | |\n"
        "  \   /| |  | | |  | |\n"
        "   | | | |__| | |__| |\n"
        "   |_|  \____/ \____/ \n", TERMINAL_TYPING_SPEED)
    print()
    terminal_typing_effect(
        "_____ _____ ______ _____   \n"
        "|  __ \_   _|  ____|  __ \ \n"
        "| |  | || | | |__  | |  | |\n"
        "| |  | || | |  __| | |  | |\n"
        "| |__| || |_| |____| |__| |\n"
        "|_____/_____|______|_____/ \n", TERMINAL_TYPING_SPEED)
    from classes import exit_message
    exit_message()


def show_graves():
    print("      ,-=-.   ,-=-.   ,-=-.   ,-=-.   ,-=-.     _     ,-=-.   ,-=-.      \n")
    print("     /  +  \ /  +  \ /  +  \ /  +  \ /  +  \  _|1|_  /  +  \ /  +  \     \n")
    print("     | ~~~ | | ~~~ | | ~~~ | | ~~~ | | ~~~ | |_ H _| | ~~~ | | ~~~ |     \n")
    print("     |R.I.P| |R.I.P| |R.I.P| |R.I.P| |R.I.P|   |S|   |R.I.P| |R.I.P|     \n")
    print("     |_____| |_____| |_____| |_____| |_____|   |_|   |_____| |_____|     \n")

    print("      ,-=-.   ,-=-.   ,-=-.   ,-=-.   ,-=-.   ,-=-.   ,-=-.   ,-=-.      \n")
    print("     /  +  \ /  +  \ /  +  \ /  +  \ /  +  \ /  +  \ /  +  \ /  +  \     \n")
    print("     | ~~~ | | ~~~ | | ~~~ | | ~~~ | | ~~~ | | ~~~ | | ~~~ | | ~~~ |     \n")
    print("     |R.I.P| |R.I.P| |R.I.P| |R.I.P| |R.I.P| |R.I.P| |R.I.P| |R.I.P|     \n")
    print("     |_____| |_____| |_____| |_____| |_____| |_____| |_____| |_____|     \n")


def print_inventory():
    print("You inventory:", inventory_array)


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def you_win():
    ##http://www.network-science.de/ascii/
    # Ascii character generator
    terminal_typing_effect(""
                           "                            _       \n"
                           "                           (_)      \n"
                           " _   _  ___  _   _    _ _ _ _ ____  \n"
                           "| | | |/ _ \| | | |  | | | | |  _ \ \n"
                           "| |_| | |_| | |_| |  | | | | | | | |\n"
                           " \__  |\___/|____/    \___/|_|_| |_|\n"
                           "(____/                              \n", TERMINAL_TYPING_SPEED)


def graveyard_entrance_gate():
    # https://ascii.co.uk/art/gates
    terminal_typing_effect(""
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
                           "                     |/                         \n"
                           , TERMINAL_TYPING_SPEED)


def search_dining_room():
    terminal_typing_effect("There is a set of drawers to your left, do you want to open them\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("#1. Yes\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("#2. No\n", TERMINAL_TYPING_SPEED)
    openRoomInDiningRoom = input("Chose 1/2\n")

    if (openRoomInDiningRoom == '1'):
        terminal_typing_effect("#1.Top drawer\n", TERMINAL_TYPING_SPEED)
        terminal_typing_effect("#2.Middle drawer\n", TERMINAL_TYPING_SPEED)
        terminal_typing_effect("#3.Bottom drawer\n", TERMINAL_TYPING_SPEED)
        terminal_typing_effect("Which drawer would you like to open?\n", TERMINAL_TYPING_SPEED)
        chooseDrawerInput = input("Chose one from above\n")

        if (chooseDrawerInput == '1'):
            open_drawer_1()  # drawer is locked
        elif (chooseDrawerInput == '2'):
            ope_drawer_2()  # mob in room
        elif (chooseDrawerInput == '3'):
            open_drawer_3()  # key in this room
        else:
            terminal_typing_effect("Choose a number\n", TERMINAL_TYPING_SPEED)
    elif (openRoomInDiningRoom == '2'):
        terminal_typing_effect("You exit the dining room, back into the main hall\n", TERMINAL_TYPING_SPEED)
        # maybe add an option to allow the user to exit the house and check the graveyard path
        from house import house_entrance_options
        house_entrance_options()
    else:
        terminal_typing_effect("ENTER A PATH\n", TERMINAL_TYPING_SPEED)
        search_dining_room()


def open_drawer_1():
    terminal_typing_effect("You go to open the 1st drawer\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("The drawer does not open\n", TERMINAL_TYPING_SPEED)
    search_dining_room()


def ope_drawer_2():
    terminal_typing_effect("You open the second drawer to find some candles\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("let's check the next drawer\n", TERMINAL_TYPING_SPEED)
    print()
    search_dining_room()


def open_drawer_3():
    terminal_typing_effect("In this drawer you find a key\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("Do you want to put the key in your inventory\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("#1. Put key in inventory\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("#2. Leave the key\n", TERMINAL_TYPING_SPEED)
    putKeyInInventory = input("Choose 1/2 from above\n")

    if ("key" in inventory_array):
        terminal_typing_effect("You already have the key in your inventory\n", TERMINAL_TYPING_SPEED)

    else:
        if (putKeyInInventory == '1'):
            inventory_array.append("key")
            terminal_typing_effect("The key is in your inventory\n", TERMINAL_TYPING_SPEED)
            print_inventory()
            # if statement to check if the player already has the key in inventory, incase they come back again

        elif (putKeyInInventory == '2'):
            terminal_typing_effect("You have chosen to leave the key there\n", TERMINAL_TYPING_SPEED)
        else:
            terminal_typing_effect("ENTER A PATH\n", TERMINAL_TYPING_SPEED)
            open_drawer_3()

    terminal_typing_effect("You walk out of the dining room, and back into the hall\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("Do you want to go back into the dining room again? Or continue upstairs?\n",
                           TERMINAL_TYPING_SPEED)
    from house import house_entrance_options
    house_entrance_options()


def read_the_rules():
    terminal_typing_effect("RULES:\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("1. All user inputs are numerical or Y/N\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("2. All Y/N answers are NOT case sensitive, the user can use y/n or Y/N\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("3. Have fun!\n", TERMINAL_TYPING_SPEED)
    print()

