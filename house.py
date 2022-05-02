from helperFunctions import terminal_typing_effect, TERMINAL_TYPING_SPEED, door_art, door_open, house_staircase, \
    inventory_array, print_inventory, search_dining_room


def begin_house_path():
    terminal_typing_effect("You begin walking up to the steps towards the moss covered door\n", TERMINAL_TYPING_SPEED)
    door_art()
    terminal_typing_effect('"This door looks like it has been shut for a long time"\n', TERMINAL_TYPING_SPEED)
    terminal_typing_effect("The door creeks open\n", TERMINAL_TYPING_SPEED)
    door_open()
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
    house_entrance_options()

def house_entrance_options():
    terminal_typing_effect("Choose from the options below \n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("#1. Do you want to go into the dining room?\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("#2. Or should we explore upstairs\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("#3. Go outside\n", TERMINAL_TYPING_SPEED)
    houseFirstInput = input("Choose 1/2/3 \n")

    if(houseFirstInput == '1'):
        house_path_1()
    elif(houseFirstInput == '2'):
        house_path_2()
    elif (houseFirstInput == '3'):
        from gameIntroLog import start_game_chose_path
        start_game_chose_path()
    else:
        terminal_typing_effect("ENTER A PATH\n", TERMINAL_TYPING_SPEED)
        house_entrance_options()

def house_path_1():
    terminal_typing_effect("The door opens \n", TERMINAL_TYPING_SPEED)
    door_open()
    terminal_typing_effect("You walk into the dining room\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("There is a large dining table in the middle of the room\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("You notice on the wall a dagger\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect('"This might be handy in the future\n"', TERMINAL_TYPING_SPEED)
    terminal_typing_effect("Do you want to equip the dagger?\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("#1. Equip the dagger\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("#2. Leave the dagger\n", TERMINAL_TYPING_SPEED)
    
    daggerInput = input("Choose 1/2\n")
    if("dagger" in inventory_array):
        terminal_typing_effect("You already have the dagger in your inventory!\n", TERMINAL_TYPING_SPEED)
    else:
        if(daggerInput == '1'):
            inventory_array.append("dagger")
            #print(inventory_array)
            print_inventory()
        elif(daggerInput == '2'):
            terminal_typing_effect("Ok, no dagger for you\n", TERMINAL_TYPING_SPEED)
        else:
            terminal_typing_effect("ENTER A PATH\n", TERMINAL_TYPING_SPEED)
            house_path_1()

    terminal_typing_effect("You continue searching around the dining room\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("There is a set of drawers to your left, do you want to open them\n", TERMINAL_TYPING_SPEED)
    search_dining_room()

def house_path_2():
    terminal_typing_effect("You take a minute to admire the grand staircase that is before you\n", TERMINAL_TYPING_SPEED)
    house_staircase()
    terminal_typing_effect("You get to the top of the stairs\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("There are 3 rooms here\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("Would you like to explore the rooms\n", TERMINAL_TYPING_SPEED)
    explore_rooms_go_downstairs()

def explore_rooms_go_downstairs():
    terminal_typing_effect("1. Explore the rooms\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("2. No, take me back downstairs\n", TERMINAL_TYPING_SPEED)
    houseUpstairsInput = input("Choose 1/2\n")
    if(houseUpstairsInput == '1'):
        doors_upstairs()

    elif(houseUpstairsInput == '2'):
        house_entrance_options()

    else:
        terminal_typing_effect("ENTER A PATH\n", TERMINAL_TYPING_SPEED)
        explore_rooms_go_downstairs()

def doors_upstairs():
    terminal_typing_effect("Which door do you want to open?\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("#1.Open door 1\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("#2.Open door 2\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("#3.Open door 3\n", TERMINAL_TYPING_SPEED)

    exploreDoorInput = input("Choose door 1/2/3\n")

    if(exploreDoorInput == '1'):
        open_door_1()
        #this key doesn't fit the door
    elif(exploreDoorInput == '2'):
        open_door_2()
        #this room has a mob
    elif(exploreDoorInput == '3'):
        open_door_3()
        #this room has the map to the end
    else:
        terminal_typing_effect("ENTER A PATH\n", TERMINAL_TYPING_SPEED)
        doors_upstairs()


def open_door_1():
    terminal_typing_effect("You try and open the first door\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("You push the door\n But it does not seem to open\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("After all that pushing you see something blocking the door\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("It doesn't look like this door will open\n", TERMINAL_TYPING_SPEED)
    doors_upstairs()


def open_door_2():
    terminal_typing_effect("You open the second door\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("There doesn't seem to be anything in here\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("You come back out into the landing\n", TERMINAL_TYPING_SPEED)
    doors_upstairs()

def open_door_3():
    if("key" in inventory_array):
        terminal_typing_effect("You enter the room 3, and see a map in the room\n", TERMINAL_TYPING_SPEED)
        terminal_typing_effect("There is nothing in this room\n", TERMINAL_TYPING_SPEED)
        terminal_typing_effect("You return back onto the upstairs landing\n", TERMINAL_TYPING_SPEED)
        doors_upstairs()
        #
    else:
        terminal_typing_effect("You do not have the key in your inventory. Find the key to open this door\n", TERMINAL_TYPING_SPEED)
        print("Inventory: ", inventory_array)
        terminal_typing_effect("You need a key to enter this room!!\n", TERMINAL_TYPING_SPEED)
        terminal_typing_effect("Go find the key!\n", TERMINAL_TYPING_SPEED)
        explore_rooms_go_downstairs()
#create function that brings user to three doors downstairs
