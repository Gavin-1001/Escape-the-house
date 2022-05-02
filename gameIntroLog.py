from forest import begin_forest_path
from graveyard import begin_graveyard_path
from helperFunctions import terminal_typing_effect, TERMINAL_TYPING_SPEED, clear_terminal
from house import begin_house_path


def game_intro_log():
    terminal_typing_effect("Welcome to ESCAPE THE ATTIC \n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("Created by Gavin Shelley\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("You approach the drive to the house\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect('"How did the drone end up here?"\n', TERMINAL_TYPING_SPEED)
    terminal_typing_effect("The house has been vacant for 50 years or so\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("I vaguely remember the story in the newspaper about the newly wed couple who bought the "
                           "house \n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("They looked so happy in the newspaper\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("And now they're dead\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("But I need to find the drone, before it gets dark!\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("Which path will I choose\n", TERMINAL_TYPING_SPEED)
    start_game_chose_path()


def start_game_chose_path():
    print()
    terminal_typing_effect("1. The Forest\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("2. The House\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("3. The Graveyard\n", TERMINAL_TYPING_SPEED)
    firstUserInput = input("Choose a path\n")

    if (firstUserInput == '1'):
        begin_forest_path()
    elif (firstUserInput == '2'):
        begin_house_path()
    elif (firstUserInput == '3'):
        begin_graveyard_path()
    else:
        terminal_typing_effect("ENTER A PATH\n", TERMINAL_TYPING_SPEED)
        start_game_chose_path()
    clear_terminal()
    print()
