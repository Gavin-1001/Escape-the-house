from classes import startFight
import os
from helperFunctions import terminal_typing_effect, TERMINAL_TYPING_SPEED, inventory_array, printInventory
    #clearTerminal

#from gameIntroLog import start_game_chose_path




def beginForestPath():
    #clearTerminal()
    terminal_typing_effect("Entering the forest, gotta be careful for wild animals as it gets dark",
                           TERMINAL_TYPING_SPEED)
    terminal_typing_effect("I don't think the kite ended up this far, but maybe it did\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("HUH\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("That's strange\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect(
        "I have walked this path so many times before, and now all of a sudden there are two paths ahead\n",
        TERMINAL_TYPING_SPEED)
    terminal_typing_effect("Ok, but which one will I choose\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("1. Path to the right\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("2. Path to the left\n", TERMINAL_TYPING_SPEED)
    print()

    forestInputOne = input("Choose from one of the above 1/2\n")
    if (forestInputOne == '1'):
        forestPath1()
    elif (forestInputOne == '2'):
        forestPath2()


def forestPath1(): #Use left and right
    terminal_typing_effect("DEAD END\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("Ok, let's try the first path to find this stupid drone\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("Oh damn it is stating to get dark, better hurry up!\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("You reach the end of the path, it's a dead end, you need to turn back\n",
                           TERMINAL_TYPING_SPEED)
    terminal_typing_effect("Do you wish to continue back ot the start or check the second path \n",
                           TERMINAL_TYPING_SPEED)
    terminal_typing_effect("1. Check the other path in the forest?\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("2. Go back to the start of the paths and try search in the graveyard/house\n",
                           TERMINAL_TYPING_SPEED)

    forestInputTwo = input("Choose 1/2\n")

    if (forestInputTwo == '1'):
        forestPath2()
    elif (forestInputTwo == '2'):
        from gameIntroLog import start_game_chose_path  # Don't know why but this works, but doesn't work globally, if this cannot be fixed put it down as a bug
        start_game_chose_path()


def forestPath2():
    terminal_typing_effect("PATH WITH FLASHLIGHT\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("YOU FOUND A FLASH LIGHT\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("FLASH LIGHT STORED IN INVENTORY\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("Maybe this path will be the one\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("As it gets dark it is harder to see \n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("You see a flash light lying on the floor\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("Do you want to keep the torch \n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("1. To keep the torch\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("2. To leave the torch on the floor\n", TERMINAL_TYPING_SPEED)
    print()

    forestInputThree = input("Choose 1/2\n")
    if('torch' in inventory_array):
        terminal_typing_effect("You already have the torch in your inventory!", TERMINAL_TYPING_SPEED)

    else:
        if (forestInputThree == '1'):
            terminal_typing_effect("You have put the torch in your pocket\n", TERMINAL_TYPING_SPEED)
            inventory_array.append("torch")
            printInventory()
        elif (forestInputThree == '2'):
            terminal_typing_effect("You left the torch\n", TERMINAL_TYPING_SPEED)

    terminal_typing_effect("The end of the path nears, you see a mob in the distance\n", TERMINAL_TYPING_SPEED)
    startFight()

    terminal_typing_effect("Do you want to go back to the start?", TERMINAL_TYPING_SPEED)
    from gameIntroLog import start_game_chose_path
    start_game_chose_path()




    # Maybe add pick up pieces of the drone, so it can be put back together at the end of the game

    # Make a story to aquire the torch
    # The torch/flashlight will just be listed as an option in if statement. Use a dict in the future
