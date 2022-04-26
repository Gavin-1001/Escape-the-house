from helperFunctions import you_died, terminal_typing_effect, TERMINAL_TYPING_SPEED
from gameIntroLog import start_game_chose_path


class player:
    health = 100
    attack = 10

class mob():
    health = 20
    attack = 2

    def show(self):
        print(self.health)
        print(self.attack)


def startFight():
    terminal_typing_effect("You see a mob in the distance \n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("The mobs health is ", mob.health, "with an attack of ", mob.attack, TERMINAL_TYPING_SPEED)
    terminal_typing_effect("Your current health is ", player.health, "with an attack of", player.attack, TERMINAL_TYPING_SPEED)

    terminal_typing_effect("Would you like to FIGHT the mob or RUN", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("#1 Fight", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("#2 Run", TERMINAL_TYPING_SPEED)
    print()
    forestFightMob = input("Choose 1/2")
    if(forestFightMob == '1'):
        terminal_typing_effect("The troll begins to attack", TERMINAL_TYPING_SPEED)
        attack()
    elif(forestFightMob == '2'):
        terminal_typing_effect("Phew that was close", TERMINAL_TYPING_SPEED)
        terminal_typing_effect("You run back to the start of the trail", TERMINAL_TYPING_SPEED)
        start_game_chose_path()

def attack():
    while mob.health > 0:
        terminal_typing_effect("You attack the mob", TERMINAL_TYPING_SPEED)
        mob.health = mob.health - player.attack
        terminal_typing_effect("The mob has ", mob.health, "points left", TERMINAL_TYPING_SPEED)

        if(mob.health <= 0):
            terminal_typing_effect("You have killed the mob, your health is", player.health, TERMINAL_TYPING_SPEED)
        elif(player.health <= 0):
            you_died()