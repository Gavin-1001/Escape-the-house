import os
import sys
import time



inventory_array = []

TERMINAL_TYPING_SPEED = 0.0025

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
    terminal_typing_effect("#           ESCAPE THE ATTIC          #\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("#                                     #\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("#            Gavin Shelley            #\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("#                                     #\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("#                                     #\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("#                                     #\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("#######################################\n", TERMINAL_TYPING_SPEED)
    print()


def doorArt():
    #https://ascii.co.uk/art/doors
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
                           "           |__________|\n"
                           , TERMINAL_TYPING_SPEED)
    print()

def doorOpen():
    #https://ascii.co.uk/art/doors
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
                           "|_|,'_________|_| \n"
                           , TERMINAL_TYPING_SPEED)
    print()


def house_staircase():
    #https://ascii.co.uk/art/stairs
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
                            "    .'                                                       `.        \n"
                           ,TERMINAL_TYPING_SPEED)
def you_died():
#Change the font and text size
##http://www.network-science.de/ascii/
# Ascii character generator
    terminal_typing_effect(
                        "__     ______  _    _ \n"
                        "\ \   / / __ \| |  | |\n"
                        " \ \_/ / |  | | |  | |\n"
                        "  \   /| |  | | |  | |\n"
                        "   | | | |__| | |__| |\n"
                        "   |_|  \____/ \____/ \n"
                        , TERMINAL_TYPING_SPEED)
    print()
    terminal_typing_effect(
                        "_____ _____ ______ _____   \n"
                        "|  __ \_   _|  ____|  __ \ \n"
                        "| |  | || | | |__  | |  | |\n"
                        "| |  | || | |  __| | |  | |\n"
                        "| |__| || |_| |____| |__| |\n"
                        "|_____/_____|______|_____/ \n"
                        ,TERMINAL_TYPING_SPEED)
    from classes import exitMessage
    exitMessage()

def showGraves():
    print("      ,-=-.   ,-=-.   ,-=-.   ,-=-.   ,-=-.     _     ,-=-.   ,-=-.      ")
    print("     /  +  \ /  +  \ /  +  \ /  +  \ /  +  \  _|1|_  /  +  \ /  +  \     ")
    print("     | ~~~ | | ~~~ | | ~~~ | | ~~~ | | ~~~ | |_ H _| | ~~~ | | ~~~ |     ")
    print("     |R.I.P| |R.I.P| |R.I.P| |R.I.P| |R.I.P|   |S|   |R.I.P| |R.I.P|     ")
    print("     |_____| |_____| |_____| |_____| |_____|   |_|   |_____| |_____|     ")



    print("      ,-=-.   ,-=-.   ,-=-.   ,-=-.   ,-=-.   ,-=-.   ,-=-.   ,-=-.      ")
    print("     /  +  \ /  +  \ /  +  \ /  +  \ /  +  \ /  +  \ /  +  \ /  +  \     ")
    print("     | ~~~ | | ~~~ | | ~~~ | | ~~~ | | ~~~ | | ~~~ | | ~~~ | | ~~~ |     ")
    print("     |R.I.P| |R.I.P| |R.I.P| |R.I.P| |R.I.P| |R.I.P| |R.I.P| |R.I.P|     ")
    print("     |_____| |_____| |_____| |_____| |_____| |_____| |_____| |_____|     ")




def printInventory():
    print("You inventory:",inventory_array)
    

def clearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def you_win():
    ##http://www.network-science.de/ascii/
    #Ascii character generator
    terminal_typing_effect(""
                           "                            _       "
                           "                           (_)      "
                           " _   _  ___  _   _    _ _ _ _ ____  "
                           "| | | |/ _ \| | | |  | | | | |  _ \ "
                           "| |_| | |_| | |_| |  | | | | | | | |"
                           " \__  |\___/|____/    \___/|_|_| |_|"
                           "(____/                              "
                           , TERMINAL_TYPING_SPEED)

def graveyard_entrance_gate():
    #https://ascii.co.uk/art/gates
    terminal_typing_effect(""
                           "                  _  /)"
                           "                 mo / )"
                           "                 |/)\)"
                           "                  /\_"
                           "                  \__|="
                           "                 (    )"
                           "                 __)(__"
                           "_________+______/      \______+__________"
                           "  __--   |       R.I.P.       |-_-- __"
                           "_-- -    | ___ __________ ___ |"
                           "-_-- __  || | | | {|    /| | || __---   -_"
                           " --__-   || | | | {|   /|| | ||--        -"
                           "         || | | | {|  /||| | ||__--"
                           " __-- -__|| | | | {| |}||| | ||--   __--"
                           "         ||_|_|_|_{| |}|||_|_||  -__"
                           " --__-  -|| | | | {& |}||/ | ||---   __--"
                           "         || | | | {| |}|/| | ||-__"
                           "--   __--|| | | | {| |}/|| | ||__-- -___"
                           "  --     || | | | {| &}||| | ||   __"
                           "---   __-|| | | | {| |}||| | ||_---__-   --"
                           " -  -_   || | | | {| |}||| | || --"
                           " __ejm 97|| | | | {| |}||| | ||_--__-   _---"
                           "_________||_|_|_|_{| |}|||_|_||______________"
                           "                     |}|/"
                           "                     |}/"
                           "                     |/"
                           , TERMINAL_TYPING_SPEED)






