from helperFunctions import typing_effect, \
    TYPING_SPEED, show_graves, inventory_array, you_died, \
    you_win, graveyard_entrance_gate


def begin_graveyard_path():
    typing_effect("You approach the entrance of the graveyard\n", TYPING_SPEED)
    show_graves()
    typing_effect("It is really dark\n", TYPING_SPEED)
    typing_effect("Do you want to use the flash light?\n", TYPING_SPEED)
    typing_effect("#1. Use flashlight\n", TYPING_SPEED)
    typing_effect("#2. Don't use flashlight\n", TYPING_SPEED)

    useFlashlight = input("Choose 1/2\n")
    if (useFlashlight == '1'):
        if ("torch" in inventory_array):
            typing_effect("You turn on the torch\n", TYPING_SPEED)
            typing_effect('"Ah, better I can see clearer"\n', TYPING_SPEED)
        else:
            typing_effect("No torch in your inventory\n", TYPING_SPEED)
    elif (useFlashlight == '2'):
        typing_effect("You chose not to use a torch\n", TYPING_SPEED)
    else:
        typing_effect("Enter 1/2 only!\n", TYPING_SPEED)
        begin_graveyard_path()

    typing_effect("As you look around\n", TYPING_SPEED)
    typing_effect("You  realize the size of the graveyard\n", TYPING_SPEED)
    typing_effect('The drone had to of landed in here\n', TYPING_SPEED)
    typing_effect("You continue walking into the graveyard\n", TYPING_SPEED)
    typing_effect('"This graveyard goes on for miles"\n', TYPING_SPEED)
    typing_effect("As you get further into the graveyard\n", TYPING_SPEED)
    typing_effect("You come to a crossroads in the graveyard\n", TYPING_SPEED)
    typing_effect("You mess with the controller of the drone\n", TYPING_SPEED)
    typing_effect("So you can hear where it is\n", TYPING_SPEED)
    typing_effect("But you can hear it coming\n", TYPING_SPEED)
    typing_effect("From the north east direction\n", TYPING_SPEED)
    typing_effect("But there are three paths in front of you\n", TYPING_SPEED)
    typing_effect("Do you want to listen out for the drone?\n", TYPING_SPEED)

    graveyardMainListenForDrone = input("Listen for drone Y/N\n").lower()
    if (graveyardMainListenForDrone == 'y'):
        droneBattery()
        typing_effect("The drone sounds like it is coming\n", TYPING_SPEED)
        typing_effect("From the north east\n", TYPING_SPEED)
    elif (graveyardMainListenForDrone == 'n'):
        typing_effect("Sure, best to save the\n", TYPING_SPEED)
        typing_effect("battery until you get closer\n", TYPING_SPEED)
        graveyard_paths()
    else:
        typing_effect("Enter y/n only!\n", TYPING_SPEED)
        begin_graveyard_path()


def graveyard_paths():
    typing_effect("Which path do you want to try?\n", TYPING_SPEED)
    typing_effect("#1. WEST\n", TYPING_SPEED)
    typing_effect("#2. NORTH\n", TYPING_SPEED)
    typing_effect("#3. EAST\n", TYPING_SPEED)

    # while loop checks input for numeric chars only.
    # If alpha chars entered, the user is asked to enter numeric chars again
    while True:
        graveyardPath = input("Choose from the options above 1/2/3 \n").lower()
        if graveyardPath.isnumeric():
            break
        typing_effect("No alpha characters, Try again\n", TYPING_SPEED)

    if (graveyardPath == '1'):
        graveyard_west_path()
    elif (graveyardPath == '2'):
        graveyard_north_path()
    elif (graveyardPath == '3'):
        graveyard_east_path()
    else:
        typing_effect("Enter 1/2/3 only please!\n", TYPING_SPEED)
        graveyard_paths()


def graveyard_west_path():
    typing_effect("WEST PATH\n", TYPING_SPEED)
    typing_effect("You have chosen to try the WEST path\n", TYPING_SPEED)
    typing_effect("After walking down the path\n", TYPING_SPEED)
    graveyard_west_path_1()


def graveyard_west_path_1():
    typing_effect("You chose to walk down the right path\n", TYPING_SPEED)
    typing_effect("The tree line covers moon light\n", TYPING_SPEED)
    typing_effect("The batteries in the torch suddenly die\n", TYPING_SPEED)
    typing_effect("Do you want to continue walking? Y/N\n", TYPING_SPEED)

    continueWalking = input("Choose Y/N\n").lower()

    if (continueWalking == 'y'):
        typing_effect("You continue walking in the dark\n", TYPING_SPEED)
        typing_effect("You fall in a hole and die\n", TYPING_SPEED)
        you_died()
    elif (continueWalking == 'n'):
        typing_effect("You turn around and proceed\n", TYPING_SPEED)
        typing_effect("to walk back to where the paths fork\n", TYPING_SPEED)
        typing_effect("You trip over rock on the ground and\n ", TYPING_SPEED)
        typing_effect("split your head open\n", TYPING_SPEED)
        typing_effect("lose consciousness and die\n", TYPING_SPEED)
        you_died()
    else:
        typing_effect("Enter Y/N only!\n", TYPING_SPEED)
        graveyard_west_path_1()


def graveyard_north_path():
    typing_effect("You chose the NORTH path\n", TYPING_SPEED)
    typing_effect("As you get closer to the drone\n", TYPING_SPEED)
    typing_effect("the signal is getting stronger\n", TYPING_SPEED)
    typing_effect("You find the drone by pushing\n", TYPING_SPEED)
    typing_effect("the throttle and listening out for it\n", TYPING_SPEED)
    typing_effect("Do you want to listen out for the drone?\n", TYPING_SPEED)
    listenForDrone = input("Y/N\n").lower()
    # put a check on this if/elif block to check alpha character only
    if (listenForDrone == 'y'):
        droneBattery()
    elif (listenForDrone == 'n'):
        typing_effect("Ok\n", TYPING_SPEED)
    else:
        typing_effect("Enter y/n only please!\n", TYPING_SPEED)
        graveyard_north_path()


def droneBattery():

    '#-initial drone battery is 100%. Each time the function is called,'
    '#the drone battery is set to the current battery - 20.'
    '#Then displays the battery level.'
    '#-If battery is 0. Battery cannot be used'
    droneBattery = 100
    batteryDepleted = 20
    droneBattery = droneBattery - batteryDepleted
    if (droneBattery <= 0):
        typing_effect("Drone battery is dead\n", TYPING_SPEED)
    typing_effect("Be careful when using the drone battery\n", TYPING_SPEED)
    typing_effect(f"Battery charge {droneBattery}\n", TYPING_SPEED)

    typing_effect("After listening for the drone, it seems to\n", TYPING_SPEED)
    typing_effect("Be coming from the east\n", TYPING_SPEED)
    typing_effect("You carefully walk back to the main paths\n", TYPING_SPEED)
    graveyard_paths()
    exit()


def graveyard_east_path():
    typing_effect("You continue walking\n", TYPING_SPEED)
    typing_effect("you come to a fork in the road\n", TYPING_SPEED)
    typing_effect("Which path do you want to follow\n", TYPING_SPEED)
    typing_effect("#1. Left\n", TYPING_SPEED)
    typing_effect("#2. Right\n", TYPING_SPEED)

    eastPathChoosePath = input("Choose 1/2\n")

    if (eastPathChoosePath == '1'):
        typing_effect("You continue walking down the path\n", TYPING_SPEED)
        found_drone()
    elif (eastPathChoosePath == '2'):
        typing_effect("You continue down this path\n", TYPING_SPEED)
        typing_effect("You hear movement in the bushes\n", TYPING_SPEED)
        typing_effect("A shake bites you\n", TYPING_SPEED)
        you_died()
    else:
        typing_effect("Enter 1/2 only please\n", TYPING_SPEED)
        graveyard_east_path()


def found_drone():
    typing_effect("You walk further down the path\n", TYPING_SPEED)
    typing_effect("You see the drone in a tree\n", TYPING_SPEED)
    typing_effect('"I found it!!"\n', TYPING_SPEED)
    typing_effect("Ok, lets try and get out of here \n", TYPING_SPEED)
    typing_effect("You continue down the path\n", TYPING_SPEED)
    typing_effect("and come to a fork in the path\n", TYPING_SPEED)
    typing_effect("You just want to get out of here\n", TYPING_SPEED)
    typing_effect("Choose a path\n", TYPING_SPEED)
    typing_effect("#1. Left\n", TYPING_SPEED)
    typing_effect("#2. Right\n", TYPING_SPEED)

    foundDroneInput = input("Choose a path\n")

    if (foundDroneInput == '1'):
        typing_effect("Now that you have found the drone it\n", TYPING_SPEED)
        typing_effect("is time to get out of here\n", TYPING_SPEED)
        typing_effect('"The torch is running out of battery"\n', TYPING_SPEED)
        typing_effect("so I better hurry\n", TYPING_SPEED)
        typing_effect("You begin to run\n", TYPING_SPEED)
        typing_effect("before the torch battery dies\n", TYPING_SPEED)
        typing_effect("While running you trip on your\n", TYPING_SPEED)
        typing_effect("shoe laces and die of a concussion\n", TYPING_SPEED)
        you_died()

    elif (foundDroneInput == '2'):
        typing_effect("You turn on your flashlight\n", TYPING_SPEED)
        typing_effect("You approach the graveyard gates\n", TYPING_SPEED)
        graveyard_entrance_gate()
        typing_effect("With the drone in your hand\n", TYPING_SPEED)
        typing_effect("You push the cemetery gate open\n", TYPING_SPEED)
        typing_effect("And vow never to return\n", TYPING_SPEED)
        typing_effect("Congratulations you win!\n", TYPING_SPEED)
        you_win()

    else:
        typing_effect("Enter 1/2 only please!\n", TYPING_SPEED)
        print("There  was an error", ValueError)
        found_drone()
