from helperFunctions import typing_effect,\
    TYPING_SPEED, door_art, door_open, house_staircase,\
    inventory_array, print_inventory, search_dining_room


def begin_house_path():
    typing_effect("You begin walking up to the\n", TYPING_SPEED)
    typing_effect("steps towards the moss  covered doors \n", TYPING_SPEED)
    door_art()
    typing_effect('"This door has been shut for sometime"\n', TYPING_SPEED)
    typing_effect("The door creeks open\n", TYPING_SPEED)
    door_open()
    typing_effect("You enter the house\n", TYPING_SPEED)
    typing_effect('"Whoa, this house is huge!"\n', TYPING_SPEED)
    typing_effect("You step into the house\n", TYPING_SPEED)
    typing_effect("The large hallway greets you along with\n", TYPING_SPEED)
    typing_effect("the staircase leading to the next above\n", TYPING_SPEED)
    typing_effect("You wonder around the hall and see\n", TYPING_SPEED)
    typing_effect("A large oil painting on the wall\n", TYPING_SPEED)
    typing_effect('"Must be the owner of the house"\n', TYPING_SPEED)
    typing_effect('"Those eyes seem to follow me" you whisper\n', TYPING_SPEED)
    typing_effect('"Damn, all the doors are locked"\n', TYPING_SPEED)
    typing_effect('"let me try this last one"\n', TYPING_SPEED)
    typing_effect('"A ha" you shout\n', TYPING_SPEED)
    typing_effect("You opened the dining room door\n", TYPING_SPEED)
    print()
    house_entrance_options()


def house_entrance_options():
    typing_effect("Choose from the options below \n", TYPING_SPEED)
    typing_effect("#1. Go into the dining room?\n", TYPING_SPEED)
    typing_effect("#2. Or should we explore upstairs\n", TYPING_SPEED)
    typing_effect("#3. Go outside\n", TYPING_SPEED)
    houseFirstInput = input("Choose 1/2/3 \n")

    if(houseFirstInput == '1'):
        house_path_1()
    elif(houseFirstInput == '2'):
        house_path_2()
    elif (houseFirstInput == '3'):
        from gameIntroLog import start_game_chose_path
        start_game_chose_path()
    else:
        typing_effect("Enter 1/2/3 only please\n", TYPING_SPEED)
        house_entrance_options()


def house_path_1():
    typing_effect("The door opens \n", TYPING_SPEED)
    door_open()
    typing_effect("You walk into the dining room\n", TYPING_SPEED)
    typing_effect("There is a large dining table in the room\n", TYPING_SPEED)
    typing_effect("You notice on the wall a dagger\n", TYPING_SPEED)
    typing_effect('"This might be handy in the future"\n', TYPING_SPEED)
    typing_effect("Do you want to equip the dagger?\n", TYPING_SPEED)
    typing_effect("#1. Equip the dagger\n", TYPING_SPEED)
    typing_effect("#2. Leave the dagger\n", TYPING_SPEED)
    daggerInput = input("Choose 1/2\n")
    if("dagger" in inventory_array):
        typing_effect("The dagger is already in inventory!\n", TYPING_SPEED)
    else:
        if(daggerInput == '1'):
            inventory_array.append("dagger")
            # print(inventory_array)
            print_inventory()
        elif(daggerInput == '2'):
            typing_effect("Ok, no dagger for you\n", TYPING_SPEED)
        else:
            typing_effect("Please enter 1/2 only\n", TYPING_SPEED)
            house_path_1()

    typing_effect("You continue searching the dining room\n", TYPING_SPEED)
    search_dining_room()


def house_path_2():
    typing_effect("You admire the grand staircase\n", TYPING_SPEED)
    house_staircase()
    typing_effect("You get to the top of the stairs\n", TYPING_SPEED)
    typing_effect("There are 3 rooms here\n", TYPING_SPEED)
    typing_effect("Would you like to explore the rooms\n", TYPING_SPEED)
    explore_rooms_go_downstairs()


def explore_rooms_go_downstairs():
    typing_effect("1. Explore the rooms\n", TYPING_SPEED)
    typing_effect("2. No, take me back downstairs\n", TYPING_SPEED)
    houseUpstairsInput = input("Choose 1/2\n")
    if(houseUpstairsInput == '1'):
        doors_upstairs()

    elif(houseUpstairsInput == '2'):
        house_entrance_options()

    else:
        typing_effect("Please enter 1/2 from the options only\n", TYPING_SPEED)
        explore_rooms_go_downstairs()


def doors_upstairs():
    typing_effect("Which door do you want to open?\n", TYPING_SPEED)
    typing_effect("#1.Open door 1\n", TYPING_SPEED)
    typing_effect("#2.Open door 2\n", TYPING_SPEED)
    typing_effect("#3.Open door 3\n", TYPING_SPEED)
    typing_effect("#4.Go downstairs\n", TYPING_SPEED)

    exploreDoorInput = input("Choose door 1/2/3/4\n")

    if(exploreDoorInput == '1'):
        open_door_1()
        # this key doesn't fit the door
    elif(exploreDoorInput == '2'):
        open_door_2()
        # this room has a mob
    elif(exploreDoorInput == '3'):
        open_door_3()
        # this room has the map to the end
    elif(exploreDoorInput == '4'):
        explore_rooms_go_downstairs()
    else:
        typing_effect("Please enter 1/2/3/4\n", TYPING_SPEED)
        typing_effect("From the options above only!\n", TYPING_SPEED)
        doors_upstairs()


def open_door_1():
    typing_effect("You try and open the first door\n", TYPING_SPEED)
    typing_effect("You push the door\n", TYPING_SPEED)
    typing_effect("But it does not seem to open\n", TYPING_SPEED)
    typing_effect("After all that pushing\n", TYPING_SPEED)
    typing_effect("You see something blocking the door\n", TYPING_SPEED)
    typing_effect("It doesn't look like this door will open\n", TYPING_SPEED)
    doors_upstairs()


def open_door_2():
    typing_effect("You open the second door\n", TYPING_SPEED)
    typing_effect("There doesn't seem to be anything in here\n", TYPING_SPEED)
    typing_effect("You come back out into the landing\n", TYPING_SPEED)
    typing_effect("1. Explore other rooms?\n", TYPING_SPEED)
    typing_effect("2. Go downstairs\n", TYPING_SPEED)
    goDownstairs = input("Choose 1/2\n")
    if (goDownstairs == '1'):
        doors_upstairs()
    elif(goDownstairs == '2'):
        explore_rooms_go_downstairs()


def open_door_3():
    if("key" in inventory_array):
        typing_effect("You enter the third room\n", TYPING_SPEED)
        typing_effect("and see a note on the table\n", TYPING_SPEED)
        print()
        typing_effect('"The sun rises in the EAST"\n', TYPING_SPEED)
        print()
        typing_effect("You return back onto the landing\n", TYPING_SPEED)
        doors_upstairs()
    else:
        typing_effect("You don't have the key in your inventory\n", TYPING_SPEED)
        typing_effect("Find the  key to open this door\n", TYPING_SPEED)
        print("Inventory: ", inventory_array)
        typing_effect("You need a key to enter this room!!\n", TYPING_SPEED)
        typing_effect("Go find the key!\n", TYPING_SPEED)
        explore_rooms_go_downstairs()
