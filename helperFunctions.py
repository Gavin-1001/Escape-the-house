import sys
import time
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
    terminal_typing_effect("#           Gavin Shelley             #\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("#                                     #\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("#######################################\n", TERMINAL_TYPING_SPEED)
    print()


def doorArt():
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
    terminal_typing_effect(
                            "         -     -                 .      :"
                            "         -     -     -                  |          -"
                            " -           -     -    .      .      |    -     -     -"
                            "         -     -     -    |      .      |    -     -     -"
                            "   -     -     -     -    |      :      |    -     -     -"
                            "   -     -     -     -   .|     _|_     |.         -     -"
                            "   -     -     -       ._-|             |-_.       -     -"
                            "   -     -     -     ._-  |     .       |  -_.     -     -"
                            "-.--.--.--.--.--. _ _-_ _ |   E-1-2-3   | _ _-_ _ .--.--.--.--.--.-"
                            " |  |  |  |  |  |`.| | | ||   _______   || | | |.'|  |  |  |  |  |"
                            "8888888888888888L_|`.88888|  |   |   |  |88888.'|_J8888888888888888"
                            "       |:     `888L_|`.|  |  |   |   |  | :|.'|_J888'    :|"
                            "       |:       `888L_|`. |  |   |   |: | .'|_J888'      :|"
                            "       |:        |`888L_|`.  |   |   |  .'|_J888'        :|"
                            "_______<:________|:_`888L_|) |   |   | (|_J888':|________:|________"
                            "       |:        |:   `888L. |___|___| .J888'  :|        :|"
                            "       |:        |:     `88|/_________\|88'    :|        :|"
                            " __..--       _.-'        ,|L_________J|.      `-._      ``--..__"
                            "'         _.-'            |/___________\|          `-._          ``"
                            "                        .c|L___________J|c.            `-."
                            "                      .' |/_____________\| `."
                            "                    .'|  |L_____________J|  |`."
                            "                  .'  | _/               \_ |  `."
                            "                .'|   _//                 \\_   |`."
                            "              .'  | _///                   \\\_ |  `."
                            "          _______________________________________________"
                            "        .'                                               `."
                            "     .'                                                   `."
                            "    .'                                                       `."
                           ,TERMINAL_TYPING_SPEED)


















def you_died():

    terminal_typing_effect(
                        "__     ______  _    _ \n"
                        "\ \   / / __ \| |  | |\n"
                        " \ \_/ / |  | | |  | |\n"
                        "  \   /| |  | | |  | |\n"
                        "   | | | |__| | |__| |\n"
                        "   |_|  \____/ \____/ \n"
                        , TERMINAL_TYPING_SPEED)
    terminal_typing_effect(
                        "_____ _____ ______ _____   \n"
                        "|  __ \_   _|  ____|  __ \ \n"
                        "| |  | || | | |__  | |  | |\n"
                        "| |  | || | |  __| | |  | |\n"
                        "| |__| || |_| |____| |__| |\n"
                        "|_____/_____|______|_____/ \n"
                        ,TERMINAL_TYPING_SPEED)