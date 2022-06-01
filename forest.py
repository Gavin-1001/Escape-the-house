from classes import start_fight
from helperFunctions import typing_effect, \
    TYPING_SPEED, inventory_array, print_inventory


def begin_forest_path():
    typing_effect("Entering the forest, gotta be careful for\n", TYPING_SPEED)
    typing_effect("wild animals as it gets dark\n", TYPING_SPEED)
    typing_effect("I don't think the drone ended up this far\n", TYPING_SPEED)
    typing_effect("HUH\n", TYPING_SPEED)
    typing_effect("That's strange\n", TYPING_SPEED)
    typing_effect("I have walked this path many times before\n", TYPING_SPEED)
    typing_effect("All of a sudden there are two paths ahead\n", TYPING_SPEED)
    typing_effect("Ok, but which one will I choose\n", TYPING_SPEED)
    typing_effect("1. Path to the right\n", TYPING_SPEED)
    typing_effect("2. Path to the left\n", TYPING_SPEED)
    print()

    forestInputOne = input("Choose from one of the above 1/2\n")
    if (forestInputOne == '1'):
        forest_path_1()
    elif (forestInputOne == '2'):
        forest_path_2()
    else:
        typing_effect("Enter 1/2  only please\n", TYPING_SPEED)
        begin_forest_path()


def forest_path_1():  # Use left and right
    print()
    typing_effect("Ok, let's try the first path\n", TYPING_SPEED)
    typing_effect("to find this stupid drone\n", TYPING_SPEED)
    typing_effect("Oh damn it is stating to get dark\n", TYPING_SPEED)
    typing_effect(" better hurry up!\n", TYPING_SPEED)
    typing_effect("You reach the end of the path\n", TYPING_SPEED)
    typing_effect("it's a dead end you need to turn back!\n", TYPING_SPEED)
    typing_effect("Do you wish to continue back to the start\n", TYPING_SPEED)
    typing_effect("or check the second path\n", TYPING_SPEED)
    print()
    typing_effect("1. Check the other path in the forest?\n", TYPING_SPEED)
    typing_effect("2. Go back to the start of the paths\n", TYPING_SPEED)
    typing_effect("and try search in the graveyard/house\n", TYPING_SPEED)
    print()
    forestInputTwo = input("Choose 1/2\n")

    if (forestInputTwo == '1'):
        forest_path_2()
    elif (forestInputTwo == '2'):
        "# Don't know why but this works, but doesn't work globally"
        '#if this cannot be fixed put it down as a bug'
        from gameIntroLog import start_game_chose_path
        start_game_chose_path()
    else:
        typing_effect("Please enter 1/2 only please!\n", TYPING_SPEED)
        forest_path_1()


def forest_path_2():
    print()
    typing_effect("YOU FOUND A FLASH LIGHT\n", TYPING_SPEED)
    typing_effect("FLASH LIGHT STORED IN INVENTORY\n", TYPING_SPEED)
    typing_effect("Maybe this path will be the one\n", TYPING_SPEED)
    typing_effect("As it gets dark it is harder to see \n", TYPING_SPEED)
    typing_effect("You see a flash light lying on the floor\n", TYPING_SPEED)
    print()
    typing_effect("Do you want to keep the torch \n", TYPING_SPEED)
    print()
    typing_effect("1. To keep the torch\n", TYPING_SPEED)
    typing_effect("2. To leave the torch on the floor\n", TYPING_SPEED)
    print()

    forestInputThree = input("Choose 1/2\n")
    if ('torch' in inventory_array):
        typing_effect("Torch already in inventory!\n", TYPING_SPEED)

    else:
        if (forestInputThree == '1'):
            typing_effect("Torch is in inventory\n", TYPING_SPEED)
            inventory_array.append("torch")
            print_inventory()
        elif (forestInputThree == '2'):
            typing_effect("You left the torch\n", TYPING_SPEED)
        else:
            typing_effect("Enter from the options 1/2 only\n", TYPING_SPEED)
            forest_path_2()

    typing_effect("The end of the path nears\n", TYPING_SPEED)
    typing_effect("you see a mob in the distance\n", TYPING_SPEED)
    start_fight()
    print()
    typing_effect("Do you want to go back to the start?\n", TYPING_SPEED)
    from gameIntroLog import start_game_chose_path
    start_game_chose_path()
