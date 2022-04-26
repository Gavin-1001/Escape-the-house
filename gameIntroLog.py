from forest import beginForestPath
from graveyard import beginGraveyardPath
from helperFunctions import terminal_typing_effect, TERMINAL_TYPING_SPEED
from house import beginHousePath


def game_intro_log():
    terminal_typing_effect("Welcome to ESCAPE THE ATTIC \n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("Created by Gavin Shelley\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("You approach the drive to the house\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect('"How did the drone end up here?"\n', TERMINAL_TYPING_SPEED)
    terminal_typing_effect("The house has been vaciant for 50 years or so\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("I vaguely remember the story in the newspaper about the newly wed couple who bought the "
                           "hosue \n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("They looked so happy in the newspaper\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("And now they're dead", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("But I need to find the drone, before it gets dark!", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("Which path will I choose", TERMINAL_TYPING_SPEED)
    start_game_chose_path()

def start_game_chose_path():
    terminal_typing_effect("1. The Forest", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("2. The House", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("3. The Graveyard", TERMINAL_TYPING_SPEED)
    firstUserInput = input("Choose a path")

    if(firstUserInput == '1'):
        beginForestPath()
    elif(firstUserInput == '2'):
        beginHousePath()
    elif(firstUserInput == '3'):
        beginGraveyardPath()
    else:
        terminal_typing_effect("ENTER A PATH", TERMINAL_TYPING_SPEED)