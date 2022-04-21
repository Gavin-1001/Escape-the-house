# -- Write your code to expect a terminal of 80 characters wide and 24 rows high --

#Important
#to-do:
# - heroku requires all inputs and print statements to have a newline character to work with heroku config --
#Colours in terminal
#RED text = player died
#GREEN text =
#BLUE text =
#Add a would you like to play



from colorama import Fore, Back, Style

# imports from helperFunctions.py
from helperFunctions import terminal_typing_effect, game_complete, you_died

#Global variables
TERMINAL_TYPING_SPEED = 0.025
isDaggerEquipped = True

def startGame():
    print()

def attic_window():
    print("You chose path 1")

def attic_door_1():
    print("You open the attic door")
    Floor_3()


def Floor_3():
    terminal_typing_effect("You descend down the creeky stairs to the third floor\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("You are standing in front of a moss covered door\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("You push to open the door\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("After wrestling to open the door, you open it wide enough to squeeze through\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("The room you\'re standing in is pitch black\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("You can see the moonlight lighting up the room\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("You notice on the floor something shining in the moons reflection\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("You walk over to take a closer look\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("As you get closer your eyes begin to adjust and you can see the outline of the object\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("You ask yourself what it could be\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("It is a DAGGER\n", TERMINAL_TYPING_SPEED)

    equipDagger = input("Do you want to equip the dagger Y/N\n")

    if equipDagger == 'y' or equipDagger == 'Y':
        terminal_typing_effect("You decide to put the dagger on your belt\n", TERMINAL_TYPING_SPEED)
        isDaggerEquipped == True
        #GIVE THE DAGGER A NAME
    elif equipDagger == 'n' or equipDagger == 'N':
        terminal_typing_effect("You leave the dagger where it is\n", TERMINAL_TYPING_SPEED)
        isDaggerEquipped == False


    terminal_typing_effect("You search around using your hands to look for a way out\n", TERMINAL_TYPING_SPEED)

    #Add a while loop to so the player can search around the room, and then leave
    terminal_typing_effect("You eventually found what feels like a door\n", TERMINAL_TYPING_SPEED)

    Floor_3_Door_1 = input("Would you like to open the door and continue? Y/N \n")

    if Floor_3_Door_1 == 'Y' or Floor_3_Door_1 == 'y':
        Floor2()
    elif Floor_3_Door_1 == 'N' or Floor_3_Door_1 == 'N':
        terminal_typing_effect("OK continue exploring the room \n", TERMINAL_TYPING_SPEED)


def Floor2():
    terminal_typing_effect("You again push the door open and squeeze through\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("You mumble 'More creeeky stairs' and make your way down the stairs\n",TERMINAL_TYPING_SPEED)
    terminal_typing_effect("FLOOR2 \n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("You reach the end of the stairs and face another dark room\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("You enter the room\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("You hear a noise in the corner of the landing and creep over to investigate\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("You enter one of the bedrooms to find a MOB standing in front of you\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("The MOB begin running towards you\n", TERMINAL_TYPING_SPEED)

    if isDaggerEquipped == True:
        terminal_typing_effect("You take out your dagger and kill the MOB\n", TERMINAL_TYPING_SPEED)
    #if dagger is equipped kill the MOB
    elif isDaggerEquipped == False:
        terminal_typing_effect("The MOB kills you\n", TERMINAL_TYPING_SPEED)
        print("You DIED")
        you_died()

    terminal_typing_effect("Phew you survived that attack, that was a close one!", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("Notice the door in the middle of the room", TERMINAL_TYPING_SPEED)

    leaveFloorTwo = input("Do you want to continue downstairs")

    if leaveFloorTwo == 'y' or leaveFloorTwo == 'Y':
        groundFloor()
    elif leaveFloorTwo == 'n' or leaveFloorTwo == 'N':
        #allow the user to explore the rooms
        terminal_typing_effect("Continue exploring the rooms", TERMINAL_TYPING_SPEED)


def groundFloorDoorFront():
    terminal_typing_effect("You have exited the house ALIVE", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("Well done", TERMINAL_TYPING_SPEED)
    game_complete()


def groundFloorDoorBack():
    print()
    #In order to escape through the back door to get a weapon or just escape the player needs a key to unlock the door
    #Hide the key in one of the rooms



def groundFloor():
    terminal_typing_effect("You climb down the ladder to the ground floor", TERMINAL_TYPING_SPEED)
    #equip the lighter so the user can see
    terminal_typing_effect("You see a door to the front of the house", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("You step futher into the room and see a door that leads out the back of the house", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("Chose a door", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("#1 Front door", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("#2 Back door", TERMINAL_TYPING_SPEED)

    groundFloorDoor = input("Which door do you want to exit through 1/2")

    if groundFloorDoor == '1':
        groundFloorDoorFront()
    elif groundFloorDoor == '2':
        groundFloorDoorBack()






def attic_door_2():
    print("attic door 2")


def game_intro_log():
    terminal_typing_effect("WELCOME TO ESCAPE THE ATTIC\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("CREATED BY GAVIN SHELLEY\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("ADD SOME MORE CONTENT HERE LATER\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("You light a match to find two door and a window\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("Which exit would you like to take\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("Path 1: The window\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("Path 2: Door 1\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("Path 3: Door 2\n", TERMINAL_TYPING_SPEED)

    atticDoorInput = input("Choose one: window/1/2 \n")
    if atticDoorInput == 'window':
        print()
        attic_window()
    elif atticDoorInput == '1':
        print()
        attic_door_1()
    elif atticDoorInput == '2':
        print()
        attic_door_2()



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

startGame = input("Would you like to play the game Y/N \n")

if startGame == 'n' or startGame == 'N':
    print("Maybe next time eh...\n")
elif startGame == 'y' or startGame == 'Y':
    game_intro_log()

