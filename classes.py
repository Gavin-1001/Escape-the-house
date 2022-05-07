from helperFunctions import you_died, terminal_typing_effect, TERMINAL_TYPING_SPEED

class Player():
    def __init__(self, health, attack):
        self.health = health
        self.attack = attack


player = Player(100, 10)
mob = Player(20, 2)


def start_fight():
    print("The mobs health is ", mob.health, "with an attack of ", mob.attack, '\n')
    print("Your current health is ", player.health, "with an attack of", player.attack, '\n')

    terminal_typing_effect("Would you like to FIGHT the mob or RUN\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("#1 Fight\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("#2 Run\n", TERMINAL_TYPING_SPEED)
    print()
    forestFightMob = input("Choose 1/2\n")
    if (forestFightMob == '1'):
        terminal_typing_effect("The troll begins to attack\n", TERMINAL_TYPING_SPEED)
        attack()
    elif (forestFightMob == '2'):
        terminal_typing_effect("Phew that was close\n", TERMINAL_TYPING_SPEED)
        terminal_typing_effect("You run back to the start of the trail\n", TERMINAL_TYPING_SPEED)
        from gameIntroLog import start_game_chose_path
        start_game_chose_path()


def attack():
    while mob.health > 0:
        terminal_typing_effect("You attack the mob\n", TERMINAL_TYPING_SPEED)
        mob.health = mob.health - player.attack
        print("The mob has ", mob.health, "points left", TERMINAL_TYPING_SPEED, '\n')

        if (mob.health <= 0):
            print("You have killed the mob, your health is", player.health, '\n')
        elif (player.health <= 0):
            you_died()

def exit_message():
    terminal_typing_effect("Thanks for playing!!\n", TERMINAL_TYPING_SPEED)

    playAgain = input("Do you want to play again? Y/N\n").lower()
    if(playAgain == 'y'):
        from run import start_game
        start_game()
    elif(playAgain == 'n'):
        terminal_typing_effect("Thanks for playing!\n", TERMINAL_TYPING_SPEED)
        type(exit)
