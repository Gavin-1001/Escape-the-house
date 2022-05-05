# -- Write your code to expect a terminal of 80 characters wide and 24 rows high --

# Important
# to-do:
# - heroku requires all inputs and print statements to have a newline character to work with heroku config --
# Colours in terminal
# RED text = player died
# GREEN text =
# BLUE text =
# Add a would you like to play


from colorama import Fore, Back, Style

from gameIntroLog import game_intro_log
from helperFunctions import terminal_typing_effect, TERMINAL_TYPING_SPEED, beginning_title, read_the_rules

print(Back.CYAN)
print(Fore.BLACK)

global playerName
def start_game():
    startGame = input("Would you like to start the game Y/N\n").lower()

    if (startGame == 'y'):
        terminal_typing_effect("Would you like to read the rules?\n", TERMINAL_TYPING_SPEED)
        readRules = input("READ RULES\n").lower()
        if(readRules == 'y'):
            read_the_rules()
        elif(readRules == 'n'):
            terminal_typing_effect("Ok, no rules for you!\n", TERMINAL_TYPING_SPEED)
        while True:
            playerName = input("Please enter your name\n").lower()
            if playerName.isalpha():
                break
            terminal_typing_effect("Please only enter characters a-z \n", TERMINAL_TYPING_SPEED)

        terminal_typing_effect(f"Welcome {playerName}, good luck!\n", TERMINAL_TYPING_SPEED)
        beginning_title()
        game_intro_log()
    elif (startGame == 'n'):
        terminal_typing_effect("Ok, maybe next time!\n", TERMINAL_TYPING_SPEED)

    else:
        terminal_typing_effect("ENTER A PATH\n", TERMINAL_TYPING_SPEED)
        startGame()


start_game()
