import random
import tkinter


class Tank:
    def __init__(self, hp, ap, hlp):
        self.health = hp
        self.armor = ap
        self.heal = hlp


def tank_shoot(tank_num, damage):
    if tank_num == "Tank1":
        if random.randint(1, 2) == 1:
            if damage <= Tank2.armor:
                print("You got the armor! Your actual damage is", str(damage) + ". Second user didn't get any damage.")
            else:
                Tank2.health -= damage
                print("You hit second user with", damage, "damage! He's left with only", Tank2.health, "health!")
        else:
            print("You miss!")
    elif tank_num == "Tank2":
        if random.randint(1, 4) == 1 or 2 or 3:
            if damage <= Tank1.armor:
                print("You got the armor! Your actual damage is", str(damage) + ". First user didn't get any damage.")
            else:
                Tank1.health -= damage
                print("You hit first user with", damage, "damage! He's left with only", Tank1.health, "health!")
def tank_heal(tank_num, heal):
    if tank_num == "Tank1":
        Tank1.health += heal
        print("Mechanic of first user's tank has fixed it and it has plus", Tank1.heal, "to health! He is now got", Tank1.health, end=".")
    if tank_num == "Tank2":
        Tank2.health += heal
        print("Mechanic of second user's tank has fixed it and it has plus", Tank2.heal, "to health! He is now got", Tank2.health, end = ".")


Tank1 = Tank(50, 4, 5)
Tank2 = Tank(50, 4, 5)

while True:
    Tank1_turn = input("It's first user's turn! What will you do?(You can use commands 'Stop', 'Shoot', 'Heal': ")
    if Tank1_turn == "Shoot":
        tank_shoot("Tank1", random.randint(1, 5))
    elif Tank1_turn == "Stop":
        print("I'm glad you checked out my tanks game, thank you, bye!")
        exit(0)
    elif Tank1_turn == "Heal":
        tank_heal("Tank1", Tank1.heal)
    else:
        print("Such a noob! You mistyped the command and now lost your time to move!")
    Tank2_turn = input("It's second user's turn! What will you do?(You can use commands 'Stop', 'Shoot', 'Heal': ")
    if Tank2_turn == "Shoot":
        tank_shoot("Tank2", random.randint(1, 10))
    elif Tank2_turn == "Stop":
        print("I'm glad you checked out my tanks game, thank you, bye!")
        exit(0)
    elif Tank2_turn == "Heal":
        tank_heal("Tank2", Tank2.heal)
    else:
        print("Such a noob! You mistyped the command and now lost your time to move!")
    if Tank1.health <= 0:
        print("Second user won!")
        break
    elif Tank2.health <= 0:
        print("First user won!")
        break
