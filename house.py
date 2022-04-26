from classes import startFight
from helperFunctions import terminal_typing_effect, TERMINAL_TYPING_SPEED, doorArt, doorOpen, house_staircase


def beginHousePath():
    terminal_typing_effect("You begin walking up to the steps towards the moss covered door\n", TERMINAL_TYPING_SPEED)
    doorArt()
    terminal_typing_effect('"This door looks like it has been shut for a long time"\n', TERMINAL_TYPING_SPEED)
    terminal_typing_effect("The door creeks open\n", TERMINAL_TYPING_SPEED)
    doorOpen()
    terminal_typing_effect("You enter the house\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect('"Whoa, this house is huge!"\n', TERMINAL_TYPING_SPEED)
    terminal_typing_effect("You step into the house\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("The large hallway greets you along with the winding staircase leading to the floor above\n",
                           TERMINAL_TYPING_SPEED)
    terminal_typing_effect("You wonder around the hall and notice a large oil painting on the hall\n",
                           TERMINAL_TYPING_SPEED)
    terminal_typing_effect('"Must be the owner of the house"\n', TERMINAL_TYPING_SPEED)
    terminal_typing_effect('"Those eyes seem to follow me" you whisper\n', TERMINAL_TYPING_SPEED)
    terminal_typing_effect('"Damn, all the doors are locked, let me try this last one"\n', TERMINAL_TYPING_SPEED)
    terminal_typing_effect('"A ha" you shout\n', TERMINAL_TYPING_SPEED)
    terminal_typing_effect("It looks like you opened the dining room door\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("Choose from the options below \n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("#1. Do you want to go in?\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("#2. Or should we explore upstairs\n", TERMINAL_TYPING_SPEED)
    houseFirstInput = input("Choose 1/2 \n")

    if(houseFirstInput == '1'):
        house_path_1()
    elif(houseFirstInput == '2'):
        house_path_2()

def house_path_1():
    terminal_typing_effect("The door opens \n", TERMINAL_TYPING_SPEED)
    doorOpen()
    terminal_typing_effect("You walk into the dining room\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("There is a large dining table in the middle of the room\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("You notice on the walll a dagger\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect('"This might be handy in the future\n"', TERMINAL_TYPING_SPEED)
    terminal_typing_effect("You equip the dagger\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("There doesn't seem to be anything of interest in the dining room\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("You continue back into the main hall\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("You check another room, and encounter a mob\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("Do you want to fight the mob\n", TERMINAL_TYPING_SPEED)
    startFight()


def house_path_2():
    terminal_typing_effect("You take a minute to admire the grand staircase that is before you\n", TERMINAL_TYPING_SPEED)
    house_staircase()
    terminal_typing_effect("You get to the top of the stairs\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("There are multiple doors here\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("Would you like to explore the rooms\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("1. I would like to explore\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("2. No, take me back to the start page\n", TERMINAL_TYPING_SPEED)

    houseUpstairsInput = input("Choose 1/2\n")

    if(houseUpstairsInput == '1'):
        doorsUpstairs()


    elif(houseUpstairsInput == '2'):
        from gameIntroLog import start_game_chose_path
        start_game_chose_path()

def doorsUpstairs():
    terminal_typing_effect("Which door do you want to open?\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("#1.Open door 1\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("#2.Open door 2\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("#3.Open door 3\n", TERMINAL_TYPING_SPEED)

    exploreDoorInput = input("Choose door 1/2/3\n")

    if(exploreDoorInput == '1'):
        openDoor1()
    elif(exploreDoorInput == '2'):
        openDoor2()
    elif(exploreDoorInput == '3'):
        openDoor3()


def openDoor1():
    terminal_typing_effect("You open the first door\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("The room has a large bed and a musty smell\n", TERMINAL_TYPING_SPEED)


def openDoor2():
    terminal_typing_effect("You open the second door\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("The room has a large bed and a musty smell\n", TERMINAL_TYPING_SPEED)

def openDoor3():
    terminal_typing_effect("You open the third door\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("The room has a large bed and a musty smell\n", TERMINAL_TYPING_SPEED)

