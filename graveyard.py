from helperFunctions import terminal_typing_effect, TERMINAL_TYPING_SPEED, show_graves, inventory_array, you_died, \
    you_win, graveyard_entrance_gate


def begin_graveyard_path():
    terminal_typing_effect("You approach the entrance of the graveyard\n", TERMINAL_TYPING_SPEED)
    show_graves()
    terminal_typing_effect("It is really dark, would you like to use your flashlight?\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("#1. Use flashlight\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("#2. Don't use flashlight\n", TERMINAL_TYPING_SPEED)

    useFlashlight = input("Choose 1/2\n")
    if (useFlashlight == '1'):
        if ("torch" in inventory_array):
            terminal_typing_effect("You turn on the torch\n", TERMINAL_TYPING_SPEED)
            terminal_typing_effect('"Ah, better I can see clearer"', TERMINAL_TYPING_SPEED)
        else:
            terminal_typing_effect("You do not have a torch in your inventory\n", TERMINAL_TYPING_SPEED)
    elif (useFlashlight == '2'):
        terminal_typing_effect("You chose not to use a torch\n", TERMINAL_TYPING_SPEED)
    else:
        terminal_typing_effect("ENTER A PATH\n", TERMINAL_TYPING_SPEED)
        begin_graveyard_path()

    terminal_typing_effect("As you look around, you realize the size of the graveyard \n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect('The drone had to of landed in here\n', TERMINAL_TYPING_SPEED)
    terminal_typing_effect("You continue walking along the main road in the graveyard\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect('"This graveyard goes on for miles"\n', TERMINAL_TYPING_SPEED)
    terminal_typing_effect("As you get deeper into the graveyard you come to a crossroads in the graveyard\n",
                           TERMINAL_TYPING_SPEED)
    terminal_typing_effect("You fiddle with the controller of the drone so you can hear where it is.\n",
                           TERMINAL_TYPING_SPEED)
    terminal_typing_effect("But you can hear it coming from the north east direction\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("But there are three paths in front of you\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("Do you want to listen out for the drone? Y/N\n", TERMINAL_TYPING_SPEED)

    graveyardMainListenForDrone = input("Listen for drone Y/N\n").lower()
    if (graveyardMainListenForDrone == 'y'):
        droneBattery()
        terminal_typing_effect("The drone sounds like it is coming from the north east\n", TERMINAL_TYPING_SPEED)
    elif (graveyardMainListenForDrone == 'n'):
        terminal_typing_effect("Sure, best to save the battery until you get closer\n", TERMINAL_TYPING_SPEED)
        graveyard_paths()
    else:
        terminal_typing_effect("ENTER A PATH\n", TERMINAL_TYPING_SPEED)
        begin_graveyard_path()


def graveyard_paths():
    terminal_typing_effect("Which path do you want to try?\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("#1. WEST\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("#2. NORTH\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("#3. EAST\n", TERMINAL_TYPING_SPEED)

    # while loop checks input for numeric chars only.
    # If alpha chars entered, the user is asked to enter numeric chars again
    while True:
        graveyardInputPath = input("Choose from the paths above 1/2/3 \n").lower()
        if graveyardInputPath.isnumeric():
            break
        terminal_typing_effect("No alpha characters, Try again\n", TERMINAL_TYPING_SPEED)

    if (graveyardInputPath == '1'):
        graveyard_west_path()
    elif graveyardInputPath == '2':
        graveyard_north_path()
    elif (graveyardInputPath == '3'):
        graveyard_east_path()
    else:
        terminal_typing_effect("ENTER A PATH\n", TERMINAL_TYPING_SPEED)
        graveyard_paths()


def graveyard_west_path():
    terminal_typing_effect("WEST PATH\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("You have chosen to try the WEST path\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("After walking down the path\n", TERMINAL_TYPING_SPEED)
    graveyard_west_path_1()


def graveyard_west_path_1():
    terminal_typing_effect("You chose to walk down the right path\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("The tree line covers moon light\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("The batteries in the torch suddenly die\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("Do you want to continue walking? Y/N\n", TERMINAL_TYPING_SPEED)

    continueWalking = input("Choose Y/N\n").lower()

    if (continueWalking == 'y'):
        terminal_typing_effect("You continue walking in the dark\n", TERMINAL_TYPING_SPEED)
        terminal_typing_effect("You fall in a hole in the ground and die\n", TERMINAL_TYPING_SPEED)
        you_died()
    elif (continueWalking == 'n'):
        terminal_typing_effect("You turn around and proceed to walk back to where the paths fork\n",
                               TERMINAL_TYPING_SPEED)
        terminal_typing_effect(
            "You trip over rock on the ground and split your head open, lose consciousness and die\n ",
            TERMINAL_TYPING_SPEED)
        you_died()
    else:
        terminal_typing_effect("ENTER A PATH\n", TERMINAL_TYPING_SPEED)
        graveyard_west_path_1()


def graveyard_north_path():
    terminal_typing_effect("You chose the NORTH path\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("As you get closer to the drone, you see that the signal is getting stronger\n",
                           TERMINAL_TYPING_SPEED)
    terminal_typing_effect("You find the drone by pushing the throttle and listening out for it\n",
                           TERMINAL_TYPING_SPEED)
    terminal_typing_effect("Do you want to listen out for the drone?\n", TERMINAL_TYPING_SPEED)
    listenForDrone = input("Y/N\n").lower()
    # put a check on this if/elif block to check alpha character only
    if (listenForDrone == 'y'):
        droneBattery()
    elif (listenForDrone == 'n'):
        terminal_typing_effect("Ok\n", TERMINAL_TYPING_SPEED)
    else:
        terminal_typing_effect("ENTER A PATH\n", TERMINAL_TYPING_SPEED)
        graveyard_north_path()


def droneBattery():
    droneBattery = 100
    batteryDepleted = 20
    droneBattery = droneBattery - batteryDepleted
    if (droneBattery <= 0):
        terminal_typing_effect("Drone battery is dead\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("You need to be careful when using the drone battery\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect(f"Battery charge {droneBattery}\n", TERMINAL_TYPING_SPEED)

    terminal_typing_effect("After listening for the drone, it seems to be coming from the east path\n",
                           TERMINAL_TYPING_SPEED)
    terminal_typing_effect("You carefully walk back to the main paths\n", TERMINAL_TYPING_SPEED)
    graveyard_paths()
    exit()

def graveyard_east_path():

    terminal_typing_effect("You continue walking, you come to a fork in the road\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("Which path do you want to follow\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("#1. Left\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("#2. Right\n", TERMINAL_TYPING_SPEED)

    eastPathChoosePath = input("Choose 1/2\n")

    if (eastPathChoosePath == '1'):
        terminal_typing_effect("You continue walking down the path\n", TERMINAL_TYPING_SPEED)
        found_drone()
    elif (eastPathChoosePath == '2'):
        terminal_typing_effect("You continue down this path. You hear movement in the bushes\n", TERMINAL_TYPING_SPEED)
        terminal_typing_effect("A shake bites you\n", TERMINAL_TYPING_SPEED)
        you_died()
    else:
        terminal_typing_effect("ENTER A PATH\n", TERMINAL_TYPING_SPEED)
        graveyard_east_path()


def found_drone():
    terminal_typing_effect("You walk further down and notice it in a tree\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect('"I found it!!"\n', TERMINAL_TYPING_SPEED)
    terminal_typing_effect("Ok, lets try and get out of here \n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("You continue down the path and come to a fork in the path\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("You just want to get out of here\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("Choose a path\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("#1. Left\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("#2. Right\n", TERMINAL_TYPING_SPEED)

    foundDroneInput = input("Choose a path\n")

    if (foundDroneInput == '1'):
        terminal_typing_effect("Now that you have found the drone it is time to get out of here\n",
                               TERMINAL_TYPING_SPEED)
        terminal_typing_effect('"The flashlight is running out of battery, so I better hurry"\n', TERMINAL_TYPING_SPEED)
        terminal_typing_effect("You begin to run, before the flash light runs out\n", TERMINAL_TYPING_SPEED)
        terminal_typing_effect("While running you trip on your shoe laces and die of a concussion\n",
                               TERMINAL_TYPING_SPEED)
        you_died()

    elif (foundDroneInput == '2'):
        terminal_typing_effect("You turn on your flashlight\n", TERMINAL_TYPING_SPEED)
        terminal_typing_effect("You approach the graveyard gates\n", TERMINAL_TYPING_SPEED)
        graveyard_entrance_gate()
        terminal_typing_effect("With the drone in your hand you push the cemetery gate open, and vow never to return\n",
                               TERMINAL_TYPING_SPEED)
        terminal_typing_effect("Congratulations you win!\n", TERMINAL_TYPING_SPEED)
        you_win()

    else:
        terminal_typing_effect("ENTER A PATH\n", TERMINAL_TYPING_SPEED)
        print("There  was an error", ValueError)
        found_drone()
