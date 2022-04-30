from helperFunctions import terminal_typing_effect, TERMINAL_TYPING_SPEED, showGraves, inventory_array


def beginGraveyardPath():
    terminal_typing_effect("You approach the entrance of the graveyard\n", TERMINAL_TYPING_SPEED)
    showGraves()
    terminal_typing_effect("It is really dark, would you like to use your flashlight?\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("#1. Use flashlight\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("#2. Don't use flashlight\n",TERMINAL_TYPING_SPEED)

    #If the user has the flashlight in the inventory, then the user can equip the flash light, otherwise tell the user they do not have the flash light
        #check the user has a flashlight if(inventory contains flash light -> then use

    useFlashlight = input("choose 1/2\n")
    if(useFlashlight == '1'):
        if("torch" in inventory_array):
            terminal_typing_effect("You turn on the torch\n", TERMINAL_TYPING_SPEED)
            terminal_typing_effect('"Ah, better I can see clearer"', TERMINAL_TYPING_SPEED)
        else:
            terminal_typing_effect("You do not have a torch in your inventory\n", TERMINAL_TYPING_SPEED)
    elif(useFlashlight == '2'):
        terminal_typing_effect("You chose not to use a torch", TERMINAL_TYPING_SPEED)
        

        
