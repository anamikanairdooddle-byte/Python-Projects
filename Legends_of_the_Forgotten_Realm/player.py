
# ==========================================
# LEGENDS OF THE FORGOTTEN REALM
# File: player.py
# Purpose: Create and manage the player
# ==========================================

import copy

from data import CLASSES, WEAPONS, ARMORS


# 1. CREATE A NEW PLAYER

def create_player(name, class_name):

    # Get the selected character's starting abilities.
    character = CLASSES[class_name]

    # Give the player a starting weapon and armor.
    starting_weapon = copy.deepcopy(WEAPONS[0])
    starting_armor = copy.deepcopy(ARMORS[0])

    # Calculate starting health and mana.
    max_hp = character["hp"] + starting_armor["hp"]
    max_mana = character["mana"] + starting_armor["mana"]

    player = {
        "name": name,
        "class": class_name,

        "level": 1,
        "exp": 0,
        "exp_to_next": 100,

        "hp": max_hp,
        "max_hp": max_hp,

        "mana": max_mana,
        "max_mana": max_mana,

        "attack": character["attack"],
        "defense": character["defense"],

        "crit_chance": character["crit_chance"],
        "crit_damage": character["crit_damage"],

        "equipped_weapon": starting_weapon,
        "equipped_armor": starting_armor,

        "inventory": {
            "weapons": [],
            "armors": [],
            "potions": [],
            "materials": [],
            "quest_items": []
        },

        "potions": {
            "Small Health Potion": 3,
            "Small Mana Potion": 2
        },

        "gold": 100,

        "bosses_defeated": 0,
        "enemies_defeated": 0,

        "rare_items_found": 0,
        "weapons_collected": 1,

        "unlocked_region": 0,

        "buffs": {
            "attack": 0,
            "defense": 0,
            "crit": 0,
            "turns": 0
        },

        "passives": []
    }

    return player


# 2. CALCULATE PLAYER ATTACK

def player_attack(player):

    weapon = player["equipped_weapon"]

    weapon_damage = 0

    if weapon:
        weapon_damage = int(
            weapon["damage"] * weapon["damage_multiplier"]
        )

    total_attack = (
        player["attack"]
        + weapon_damage
        + player["buffs"]["attack"]
    )

    return total_attack


# 3. CALCULATE PLAYER DEFENSE

def player_defense(player):

    armor = player["equipped_armor"]

    armor_defense = 0

    if armor:
        armor_defense = armor["defense"]

    total_defense = (
        player["defense"]
        + armor_defense
        + player["buffs"]["defense"]
    )

    return total_defense


# 4. CALCULATE CRITICAL CHANCE

def player_critical_chance(player):

    weapon = player["equipped_weapon"]

    weapon_bonus = 0

    if weapon:
        weapon_bonus = weapon["critical_bonus"]

    total_critical = (
        player["crit_chance"]
        + weapon_bonus
        + player["buffs"]["crit"]
    )

    if total_critical > 100:
        total_critical = 100

    return total_critical


# 5. LEVEL UP THE PLAYER

def level_up(player):

    player["level"] += 1

    # Increase the player's basic abilities.
    player["max_hp"] += 20
    player["max_mana"] += 10

    player["hp"] = player["max_hp"]
    player["mana"] = player["max_mana"]

    player["attack"] += 4
    player["defense"] += 2

    # Increase the EXP required for the next level.
    player["exp_to_next"] = player["level"] * 100

    print("\n================================")
    print("       LEVEL UP!")
    print("================================")

    print("New Level:", player["level"])
    print("Maximum HP increased!")
    print("Maximum Mana increased!")
    print("Attack increased!")
    print("Defense increased!")

    # Give a passive bonus every five levels.
    if player["level"] % 5 == 0:

        player["passives"].append(
            "Level " + str(player["level"]) + " Bonus"
        )

        print("You unlocked a new passive bonus!")

    print("================================")


# 6. GAIN EXPERIENCE POINTS

def gain_exp(player, amount):

    player["exp"] += amount

    print("\nYou gained", amount, "EXP!")

    # The player cannot pass the next boss milestone
    # until that boss has been defeated.
    level_limit = min(
        100,
        (player["bosses_defeated"] + 1) * 10
    )

    while (
        player["exp"] >= player["exp_to_next"]
        and player["level"] < level_limit
    ):

        player["exp"] -= player["exp_to_next"]

        level_up(player)


# 7. DISPLAY PLAYER INFORMATION

def display_player(player):

    print("\n================================")
    print("         PLAYER PROFILE")
    print("================================")

    print("Name:", player["name"])
    print("Class:", player["class"])

    print("Level:", player["level"])

    print(
        "EXP:",
        player["exp"],
        "/",
        player["exp_to_next"]
    )

    print("Health:", player["hp"], "/", player["max_hp"])
    print("Mana:", player["mana"], "/", player["max_mana"])

    print("Attack:", player_attack(player))
    print("Defense:", player_defense(player))

    print("Gold:", player["gold"])

    print("Enemies Defeated:", player["enemies_defeated"])
    print("Bosses Defeated:", player["bosses_defeated"])

    print("================================")
