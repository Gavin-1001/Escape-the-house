# -- Write your code to expect a terminal of 80 characters wide and 24 rows high --

#Important
#ToDo:
# -- N.B heroku requires all inputs and print statements to have a newline character to work with heroku config --
#Colours in terminal
#RED text = player died
#GREEN text =
#BLUE text =


from colorama import Fore, Back, Style

def welcome_message():
    """
        This function is the initial function that is called when the user plays the game.
        It introduces the user to the game and provides a storyline,
    """
    while True:
        username = input("Hello player, enter your name to begin \n")
        print(Fore.YELLOW + f"Hello {username}, can you escape the attic")

        if username == "":
            print("Hello are you there, please enter your name to begin an adventure!")
            continue
        else:
            break

welcome_message()

