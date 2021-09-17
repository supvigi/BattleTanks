from tanks.cls import *
import random


def tank_shoot(tank_num, damage):
    if tank_num == "Tank1":
        if damage <= Tank2.armor:
            print("You got the armor! Your actual damage is", damage, ". Second user didn't get any damage.")
        else:
            Tank2.health -= damage
            print("You hit second user with", damage, "damage! He's left with only", Tank2.health, "health!")
    elif tank_num == "Tank2":
        if damage <= Tank1.armor:
            print("You got the armor! Your actual damage is", damage, ". First user didn't get any damage.")
        else:
            Tank1.health -= damage
            print("You hit first user with", damage, "damage! He's left with only", Tank1.health, "health!")


Tank1 = Tank(50, 2)
Tank2 = Tank(50, 2)

while True:
    Tank1_turn = input("It's first user's turn! What will you do?(You can use command 'Shoot'): ")
    if Tank1_turn == "Shoot":
        tank_shoot("Tank1", random.randint(1, 5))
    Tank2_turn = input("It's second user's turn! What will you do?(You can use command 'Shoot'): ")
    if Tank2_turn == "Shoot":
        tank_shoot("Tank2", random.randint(1, 5))
    if Tank1.health <= 0:
        print("Second user won!")
        break
    elif Tank2.health <= 0:
        print("First user won!")
        break
