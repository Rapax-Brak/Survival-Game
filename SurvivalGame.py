#!/usr/bin/env python3
import random

# Content won't change so tuples are used to make sure it doesn't
weapon_list = ("sword","knife","gun","stick")
locations = ("forest","beach")

print("""Survival game by Underground Tech

How long can you survive?""")

# Loop untill told to break
while True:
    weapon_choice = input("\nWhat weapon would you like? (Enter 'l' to list weapons): ")
    if weapon_choice.lower() == "l":
        for item in weapon_list:
            print("\n> {weapon}".format(weapon=item))
    elif weapon_choice in weapon_list:
        attack_damage = random.randint(1, 100)
        break
    else:
        print("\n{non_valid_weapon} is not a weapon you can use!".format(non_valid_weapon=weapon_choice))

print("\nYou have picked a {weapon}. Let's go!".format(weapon=weapon_choice))

# Loop untill told to break
while True:
    location  = input("\nWhere do you want to go first? (Enter 'l' to list locations): ")
    if location.lower() == "l":
        for item in locations:
            print("\n> {location}".format(location=item))
    elif location in locations:
        print("\nOkay, we're heading to the {location}.".format(location=location))
        break
