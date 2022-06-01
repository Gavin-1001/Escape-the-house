'#Write your code to expect a terminal of 80 characters wide and 24 rows high'

# Important
# to-do:
# heroku requires all inputs and print statements to
# have a newline character to work with heroku config
# Colours in terminal
# RED text = player died
# GREEN text =
# BLUE text =
# Add a would you like to play

from gameIntroLog import game_intro_log
from helperFunctions import typing_effect, \
    TYPING_SPEED, beginning_title, read_the_rules

global playerName


def start_game():
    startGameInput = input("Would you like to start the game? Y/N\n").lower()
    if(startGameInput == 'y'):
        beginGame()
    elif(startGameInput == 'n'):
        print("You exited the game\n")
        exit()
    else:
        typing_effect("Please enter y/n only!! \n", TYPING_SPEED)
        start_game()


def getUserName():
    while True:
        playerName = input("Please enter your name\n")
        if playerName.isalpha():
            break
        typing_effect("Please only enter characters a-z \n", TYPING_SPEED)

    typing_effect(f"Welcome {playerName}, good luck!\n", TYPING_SPEED)


def beginGame():
    readGameRules = input("Would you like to read the game rules? Y/N\n").lower()

    if (readGameRules == 'y'):
        read_the_rules()
        getUserName()
        beginning_title()
        game_intro_log()

    elif(readGameRules == 'n'):
        typing_effect("Ok, no rules for you!\n", TYPING_SPEED)
        getUserName()
        beginning_title()
        game_intro_log()

    else:
        typing_effect("Please enter y/n to read the rules! \n", TYPING_SPEED)
        beginGame()

start_game()
