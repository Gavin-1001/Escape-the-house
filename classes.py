from helperFunctions import you_died, typing_effect, TYPING_SPEED


class Player():
    def __init__(self, health, attack):
        self.health = health
        self.attack = attack


player = Player(100, 10)
mob = Player(20, 2)


def start_fight():
    print("The mobs health is ", mob.health, '\n')
    print("with an attack of ", mob.attack, '\n')
    print("Your current health is ", player.health, '\n')
    print("with an attack of", player.attack, '\n')

    typing_effect("Would you like to FIGHT the mob or RUN\n", TYPING_SPEED)
    typing_effect("#1 Fight\n", TYPING_SPEED)
    typing_effect("#2 Run\n", TYPING_SPEED)
    print()
    forestFightMob = input("Choose 1/2\n")
    if (forestFightMob == '1'):
        typing_effect("The troll begins to attack\n", TYPING_SPEED)
        attack()
    elif (forestFightMob == '2'):
        typing_effect("Phew that was close\n", TYPING_SPEED)
        typing_effect("You run back to the start of the trail\n", TYPING_SPEED)
        from gameIntroLog import start_game_chose_path
        start_game_chose_path()


def attack():
    while mob.health > 0:
        typing_effect("You attack the mob\n", TYPING_SPEED)
        mob.health = mob.health - player.attack
        print("The mob has ", mob.health, "points left", TYPING_SPEED, '\n')

        if (mob.health <= 0):
            print("You have killed the mob, your health:", player.health, '\n')
        elif (player.health <= 0):
            you_died()


def exit_message():
    typing_effect("Thanks for playing!!\n", TYPING_SPEED)

    playAgain = input("Do you want to play again? Y/N\n").lower()
    if(playAgain == 'y'):
        from run import start_game
        start_game()
    elif(playAgain == 'n'):
        typing_effect("Thanks for playing!\n", TYPING_SPEED)
        type(exit)
