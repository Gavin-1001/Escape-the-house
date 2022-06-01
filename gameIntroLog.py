from forest import begin_forest_path
from graveyard import begin_graveyard_path
from helperFunctions import typing_effect, TYPING_SPEED, clear_terminal
from house import begin_house_path


def game_intro_log():
    typing_effect("Welcome to ESCAPE THE ATTIC\n", TYPING_SPEED)
    typing_effect("Created by Gavin Shelley\n", TYPING_SPEED)
    typing_effect("You approach the drive to the house\n", TYPING_SPEED)
    typing_effect('"How did the drone end up here?"\n', TYPING_SPEED)
    typing_effect("The house has been vacant for 50 years\n", TYPING_SPEED)
    typing_effect("I remember the story in the newspaper\n", TYPING_SPEED)
    typing_effect("About the couple who bought the house\n", TYPING_SPEED)
    typing_effect("They looked so happy in the newspaper\n", TYPING_SPEED)
    typing_effect("And now they're dead\n", TYPING_SPEED)
    typing_effect("But I need to find the drone\n", TYPING_SPEED)
    typing_effect("Before it gets dark!\n", TYPING_SPEED)
    typing_effect("Which path will I choose\n", TYPING_SPEED)
    start_game_chose_path()


def start_game_chose_path():
    print()
    typing_effect("1. The Forest\n", TYPING_SPEED)
    typing_effect("2. The House\n", TYPING_SPEED)
    typing_effect("3. The Graveyard\n", TYPING_SPEED)
    firstUserInput = input("Choose a path 1/2/3\n")

    if (firstUserInput == '1'):
        begin_forest_path()
    elif (firstUserInput == '2'):
        begin_house_path()
    elif (firstUserInput == '3'):
        begin_graveyard_path()
    else:
        typing_effect("Enter 1/2/3 only please!\n", TYPING_SPEED)
        start_game_chose_path()
    clear_terminal()
    print()
