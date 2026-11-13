
# ==========================================
# LEGENDS OF THE FORGOTTEN REALM
# File: systems.py
# Purpose: Main gameplay systems
# ==========================================

import random
import copy

from data import (
    WEAPONS,
    ARMORS,
    POTIONS,
    ENEMIES,
    BOSSES,
    REGIONS,
    CLASS_SKILLS,
    RARITY_DROP_CHANCES
)

from player import (
    player_attack,
    player_defense,
    player_critical_chance,
    gain_exp,
    display_player
)


# ==========================================
# 1. INPUT VALIDATION
# ==========================================

def ask_choice(message, options):

    print("\n" + message)

    for number, option in enumerate(options, 1):
        print(str(number) + ". " + option)

    while True:

        choice = input("Enter your choice: ")

        if choice.isdigit():

            choice = int(choice)

            if choice >= 1 and choice <= len(options):
                return choice

        print("Invalid choice. Please try again.")


# ==========================================
# 2. DISPLAY PLAYER STATISTICS
# ==========================================

def show_stats(player):

    display_player(player)

    weapon = player["equipped_weapon"]
    armor = player["equipped_armor"]

    if weapon:
        print("Weapon:", weapon["name"])
    else:
        print("Weapon: Nothing equipped")

    if armor:
        print("Armor:", armor["name"])
    else:
        print("Armor: Nothing equipped")

    print("Critical Chance:", player_critical_chance(player), "%")


# ==========================================
# 3. INVENTORY DISPLAY
# ==========================================

def show_inventory(player):

    inventory = player["inventory"]

    print("\n========== INVENTORY ==========")

    print("\nWEAPONS")

    if len(inventory["weapons"]) == 0:
        print("No weapons collected.")

    for item in inventory["weapons"]:
        print(item["name"], "-", item["rank"])

    print("\nARMOR")

    if len(inventory["armors"]) == 0:
        print("No armor collected.")

    for item in inventory["armors"]:
        print(item["name"], "-", item["rank"])

    print("\nPOTIONS")

    for name, quantity in player["potions"].items():

        if quantity > 0:
            print(name, "x", quantity)

    print("\nMATERIALS")

    if len(inventory["materials"]) == 0:
        print("No materials collected.")

    for item in inventory["materials"]:
        print(item)

    print("\nQUEST ITEMS")

    if len(inventory["quest_items"]) == 0:
        print("No quest items collected.")

    for item in inventory["quest_items"]:
        print(item)

    print("\nGold:", player["gold"])
    print("===============================")


# ==========================================
# 4. EQUIP WEAPON
# ==========================================

def equip_weapon(player):

    weapons = player["inventory"]["weapons"]

    if len(weapons) == 0:
        print("\nYou don't have any extra weapons.")
        return

    print("\n========== WEAPONS ==========")

    for number, weapon in enumerate(weapons, 1):

        print(
            number,
            ".",
            weapon["name"],
            "-",
            weapon["rank"],
            "- Damage:",
            weapon["damage"]
        )

    print("0. Cancel")

    choice = input("Choose a weapon: ")

    if choice.isdigit():

        choice = int(choice)

        if choice == 0:
            return

        if choice >= 1 and choice <= len(weapons):

            weapon = weapons[choice - 1]

            if player["level"] < weapon["required_level"]:
                print("Your level is too low to use this weapon.")
                return

            old_weapon = player["equipped_weapon"]

            if old_weapon:
                weapons.append(old_weapon)

            player["equipped_weapon"] = weapons.pop(choice - 1)

            print("Equipped:", player["equipped_weapon"]["name"])

            return

    print("Invalid weapon choice.")


# ==========================================
# 5. EQUIP ARMOR
# ==========================================

def equip_armor(player):

    armors = player["inventory"]["armors"]

    if len(armors) == 0:
        print("\nYou don't have any extra armor.")
        return

    print("\n========== ARMOR ==========")

    for number, armor in enumerate(armors, 1):

        print(
            number,
            ".",
            armor["name"],
            "-",
            armor["rank"],
            "- Defense:",
            armor["defense"]
        )

    print("0. Cancel")

    choice = input("Choose armor: ")

    if choice.isdigit():

        choice = int(choice)

        if choice == 0:
            return

        if choice >= 1 and choice <= len(armors):

            armor = armors[choice - 1]

            if player["level"] < armor["required_level"]:
                print("Your level is too low to use this armor.")
                return

            old_armor = player["equipped_armor"]

            if old_armor:
                armors.append(old_armor)

            player["equipped_armor"] = armors.pop(choice - 1)

            print("Equipped:", player["equipped_armor"]["name"])

            return

    print("Invalid armor choice.")


# ==========================================
# 6. UNEQUIP ITEMS
# ==========================================

def unequip_items(player):

    choice = ask_choice(
        "What do you want to unequip?",
        ["Weapon", "Armor", "Cancel"]
    )

    if choice == 1:

        if player["equipped_weapon"]:

            player["inventory"]["weapons"].append(
                player["equipped_weapon"]
            )

            player["equipped_weapon"] = None

            print("Weapon unequipped.")

        else:
            print("You don't have a weapon equipped.")

    elif choice == 2:

        if player["equipped_armor"]:

            player["inventory"]["armors"].append(
                player["equipped_armor"]
            )

            player["equipped_armor"] = None

            print("Armor unequipped.")

        else:
            print("You don't have armor equipped.")


# ==========================================
# 7. USE POTION
# ==========================================

def use_potion(player):

    potions = player["potions"]

    available = []

    print("\n========== POTIONS ==========")

    for name, quantity in potions.items():

        if quantity > 0:

            print(name, "x", quantity)
            available.append(name)

    if len(available) == 0:

        print("You don't have any potions.")
        return False

    print("0. Cancel")

    choice = input("Choose a potion: ")

    if not choice.isdigit():
        print("Invalid choice.")
        return False

    choice = int(choice)

    if choice == 0:
        return False

    if choice < 1 or choice > len(available):
        print("Invalid choice.")
        return False

    potion_name = available[choice - 1]

    potion = None

    for item in POTIONS:

        if item["name"] == potion_name:
            potion = item
            break

    if potion is None:
        print("Potion information not found.")
        return False

    if potion["type"] == "health":

        if potion["value"] == "full":
            player["hp"] = player["max_hp"]

        else:
            player["hp"] += potion["value"]

            if player["hp"] > player["max_hp"]:
                player["hp"] = player["max_hp"]

        print("Health restored!")

    elif potion["type"] == "mana":

        if potion["value"] == "full":
            player["mana"] = player["max_mana"]

        else:
            player["mana"] += potion["value"]

            if player["mana"] > player["max_mana"]:
                player["mana"] = player["max_mana"]

        print("Mana restored!")

    elif potion["type"] == "mixed":

        player["hp"] += potion["health"]
        player["mana"] += potion["mana"]

        if player["hp"] > player["max_hp"]:
            player["hp"] = player["max_hp"]

        if player["mana"] > player["max_mana"]:
            player["mana"] = player["max_mana"]

        print("Health and mana restored!")

    elif potion["type"] == "buff":

        effect = potion["effect"]

        player["buffs"][effect] += potion["value"]

        player["buffs"]["turns"] = potion["duration"]

        print(effect.title(), "increased for 3 turns!")

    potions[potion_name] -= 1

    return True


# ==========================================
# 8. DROP OR SELL INVENTORY ITEMS
# ==========================================

def manage_item(player, action):

    choice = ask_choice(
        "Choose an item category:",
        ["Weapons", "Armor", "Cancel"]
    )

    if choice == 3:
        return

    if choice == 1:
        items = player["inventory"]["weapons"]
    else:
        items = player["inventory"]["armors"]

    if len(items) == 0:
        print("No items available.")
        return

    for number, item in enumerate(items, 1):
        print(number, ".", item["name"], "-", item["rank"])

    print("0. Cancel")

    selected = input("Choose an item: ")

    if not selected.isdigit():
        print("Invalid choice.")
        return

    selected = int(selected)

    if selected == 0:
        return

    if selected < 1 or selected > len(items):
        print("Invalid choice.")
        return

    item = items[selected - 1]

    if action == "drop":

        items.pop(selected - 1)

        print(item["name"], "dropped.")

    elif action == "sell":

        sell_price = int(item["price"] * 0.5)

        player["gold"] += sell_price

        items.pop(selected - 1)

        print("Item sold for", sell_price, "gold.")


# ==========================================
# 9. INVENTORY MENU
# ==========================================

def inventory_menu(player):

    while True:

        choice = ask_choice(
            "========== INVENTORY MENU ==========",
            [
                "View Inventory",
                "Equip Weapon",
                "Equip Armor",
                "Unequip Item",
                "Use Potion",
                "Drop Item",
                "Sell Item",
                "Return"
            ]
        )

        if choice == 1:
            show_inventory(player)

        elif choice == 2:
            equip_weapon(player)

        elif choice == 3:
            equip_armor(player)

        elif choice == 4:
            unequip_items(player)

        elif choice == 5:
            use_potion(player)

        elif choice == 6:
            manage_item(player, "drop")

        elif choice == 7:
            manage_item(player, "sell")

        elif choice == 8:
            break


# ==========================================
# 10. VILLAGE SHOP
# ==========================================

def shop(player):

    while True:

        choice = ask_choice(
            "========== VILLAGE SHOP ==========",
            [
                "Buy Weapons",
                "Buy Armor",
                "Buy Potions",
                "Sell Items",
                "Leave Shop"
            ]
        )

        if choice == 1:

            available = []

            for weapon in WEAPONS:

                if player["level"] >= weapon["required_level"]:
                    available.append(weapon)

            for number, weapon in enumerate(available, 1):

                print(
                    number,
                    ".",
                    weapon["name"],
                    "-",
                    weapon["rank"],
                    "-",
                    weapon["price"],
                    "Gold"
                )

            print("0. Cancel")

            selected = input("Choose a weapon: ")

            if selected.isdigit():

                selected = int(selected)

                if selected >= 1 and selected <= len(available):

                    weapon = copy.deepcopy(available[selected - 1])

                    if player["gold"] >= weapon["price"]:

                        player["gold"] -= weapon["price"]

                        player["inventory"]["weapons"].append(weapon)

                        player["weapons_collected"] += 1

                        print("Weapon purchased!")

                    else:
                        print("Not enough gold.")

        elif choice == 2:

            available = []

            for armor in ARMORS:

                if player["level"] >= armor["required_level"]:
                    available.append(armor)

            for number, armor in enumerate(available, 1):

                print(
                    number,
                    ".",
                    armor["name"],
                    "-",
                    armor["rank"],
                    "-",
                    armor["price"],
                    "Gold"
                )

            print("0. Cancel")

            selected = input("Choose armor: ")

            if selected.isdigit():

                selected = int(selected)

                if selected >= 1 and selected <= len(available):

                    armor = copy.deepcopy(available[selected - 1])

                    if player["gold"] >= armor["price"]:

                        player["gold"] -= armor["price"]

                        player["inventory"]["armors"].append(armor)

                        print("Armor purchased!")

                    else:
                        print("Not enough gold.")

        elif choice == 3:

            for number, potion in enumerate(POTIONS, 1):

                print(
                    number,
                    ".",
                    potion["name"],
                    "-",
                    potion["price"],
                    "Gold"
                )

            print("0. Cancel")

            selected = input("Choose a potion: ")

            if selected.isdigit():

                selected = int(selected)

                if selected >= 1 and selected <= len(POTIONS):

                    potion = POTIONS[selected - 1]

                    if player["gold"] >= potion["price"]:

                        player["gold"] -= potion["price"]

                        name = potion["name"]

                        if name not in player["potions"]:
                            player["potions"][name] = 0

                        player["potions"][name] += 1

                        print("Potion purchased!")

                    else:
                        print("Not enough gold.")

        elif choice == 4:
            manage_item(player, "sell")

        elif choice == 5:
            print("You left the shop.")
            break


# ==========================================
# 11. CREATE A RANDOM ENEMY
# ==========================================

def make_enemy(level):

    available = []

    for enemy in ENEMIES:

        if level >= enemy["min_level"] and level <= enemy["max_level"]:
            available.append(enemy)

    if len(available) == 0:
        available = ENEMIES

    enemy = copy.deepcopy(random.choice(available))

    # Scale enemy abilities according to the player's level.
    difference = level - enemy["min_level"]

    if difference < 0:
        difference = 0

    enemy["level"] = level

    enemy["hp"] += difference * 15
    enemy["max_hp"] = enemy["hp"]

    enemy["attack"] += difference * 3
    enemy["defense"] += difference

    enemy["exp"] += difference * 10
    enemy["gold"] += difference * 5

    enemy["is_boss"] = False

    return enemy


# ==========================================
# 12. CREATE A BOSS
# ==========================================

def make_boss(level):

    for boss in BOSSES:

        if boss["level"] == level:

            enemy = copy.deepcopy(boss)

            enemy["max_hp"] = enemy["hp"]
            enemy["is_boss"] = True
            enemy["turn_count"] = 0

            return enemy

    return None


# ==========================================
# 13. SELECT LOOT RARITY
# ==========================================

def choose_rarity(minimum_rare=False):

    rarities = list(RARITY_DROP_CHANCES.keys())

    chances = list(RARITY_DROP_CHANCES.values())

    if minimum_rare:

        rarities = [
            "Rare",
            "Super Rare",
            "Epic",
            "Mythical",
            "Legendary"
        ]

        chances = [
            RARITY_DROP_CHANCES[name]
            for name in rarities
        ]

    return random.choices(
        rarities,
        weights=chances,
        k=1
    )[0]


# ==========================================
# 14. DROP LOOT AFTER BATTLE
# ==========================================

def loot_drop(player, enemy):

    print("\n========== LOOT ==========")

    player["gold"] += enemy["gold"]

    print("You collected", enemy["gold"], "gold!")

    # Give the player a chance to find equipment.
    item_found = random.random() < 0.35

    # Bosses always give an equipment reward.
    if enemy["is_boss"]:
        item_found = True

    if item_found:

        if enemy["is_boss"]:
            rarity = choose_rarity(True)
        else:
            rarity = choose_rarity()

        category = random.choice(["weapon", "armor"])

        if category == "weapon":

            matching = []

            for weapon in WEAPONS:

                if weapon["rank"] == rarity:
                    matching.append(weapon)

            if len(matching) > 0:

                item = copy.deepcopy(random.choice(matching))

                player["inventory"]["weapons"].append(item)

                player["weapons_collected"] += 1

                print("Weapon found:", item["name"], "-", rarity)

        else:

            matching = []

            for armor in ARMORS:

                if armor["rank"] == rarity:
                    matching.append(armor)

            if len(matching) > 0:

                item = copy.deepcopy(random.choice(matching))

                player["inventory"]["armors"].append(item)

                print("Armor found:", item["name"], "-", rarity)

        if rarity not in ["Common", "Uncommon"]:
            player["rare_items_found"] += 1

    # Materials can also be collected.
    if random.random() < 0.40:

        material = random.choice(
            ["Magic Crystal", "Dragon Scale", "Ancient Stone", "Demon Essence"]
        )

        player["inventory"]["materials"].append(material)

        print("Material collected:", material)

    # A boss can drop a quest item.
    if enemy["is_boss"]:

        quest_item = enemy["name"] + "'s Emblem"

        player["inventory"]["quest_items"].append(quest_item)

        print("Quest item collected:", quest_item)

    print("===========================")


# ==========================================
# 15. PLAYER ATTACK
# ==========================================

def attack_enemy(player, enemy):

    damage = player_attack(player) - enemy["defense"]

    if damage < 1:
        damage = 1

    critical = random.randint(1, 100)

    if critical <= player_critical_chance(player):

        damage = int(damage * player["crit_damage"])

        print("\nCRITICAL HIT!")

    enemy["hp"] -= damage

    print("You attacked", enemy["name"])
    print("Damage:", damage)

    if enemy["hp"] < 0:
        enemy["hp"] = 0


# ==========================================
# 16. PLAYER SKILLS
# ==========================================

def use_skill(player, enemy):

    skills = CLASS_SKILLS[player["class"]]

    available = []

    print("\n========== YOUR SKILLS ==========")

    for skill in skills:

        if player["level"] >= skill["unlock_level"]:

            available.append(skill)

            print(
                len(available),
                ".",
                skill["name"],
                "- Mana:",
                skill["mana"]
            )

    if len(available) == 0:
        print("No skills available.")
        return False

    print("0. Cancel")

    selected = input("Choose a skill: ")

    if not selected.isdigit():
        print("Invalid choice.")
        return False

    selected = int(selected)

    if selected == 0:
        return False

    if selected < 1 or selected > len(available):
        print("Invalid skill.")
        return False

    skill = available[selected - 1]

    if player["mana"] < skill["mana"]:

        print("Not enough mana!")
        return False

    player["mana"] -= skill["mana"]

    damage = int(
        player_attack(player) * skill["multiplier"]
    )

    damage -= enemy["defense"]

    if damage < 1:
        damage = 1

    # Assassin's Instant Kill has a very low chance.
    if (
        player["class"] == "Assassin"
        and skill["name"] == "Instant Kill"
        and random.random() < 0.05
    ):

        enemy["hp"] = 0

        print("\nINSTANT KILL!")

        return True

    enemy["hp"] -= damage

    if enemy["hp"] < 0:
        enemy["hp"] = 0

    print("\nYou used", skill["name"])
    print("Damage:", damage)

    return True


# ==========================================
# 17. ENEMY ATTACK
# ==========================================

def enemy_attack(player, enemy, defending):

    damage = enemy["attack"]

    armor = player["equipped_armor"]

    # Bosses may use a special skill every third turn.
    if enemy["is_boss"]:

        enemy["turn_count"] += 1

        if enemy["turn_count"] % 3 == 0:

            skill = random.choice(enemy["skills"])

            print("\n", enemy["name"], "used", skill, "!")

            if skill in ["Healing Roots", "Rock Shield", "Dark Recovery"]:

                healing = int(enemy["max_hp"] * 0.10)

                enemy["hp"] += healing

                if enemy["hp"] > enemy["max_hp"]:
                    enemy["hp"] = enemy["max_hp"]

                print("Boss recovered", healing, "HP!")

                return

            damage = int(damage * 1.5)

    # Critical resistance reduces critical damage.
    critical = random.randint(1, 100)

    if critical <= 10:

        resistance = 0

        if armor:
            resistance = armor["critical_resistance"]

        damage = int(damage * 2 * (1 - resistance / 100))

        print("\nEnemy landed a CRITICAL HIT!")

    # Player defense reduces incoming damage.
    damage -= player_defense(player)

    if damage < 1:
        damage = 1

    # Defending reduces the next incoming attack by 50%.
    if defending:

        damage = int(damage * 0.5)

        if damage < 1:
            damage = 1

    player["hp"] -= damage

    if player["hp"] < 0:
        player["hp"] = 0

    print(enemy["name"], "attacked you!")
    print("Damage received:", damage)


# ==========================================
# 18. BATTLE SYSTEM
# ==========================================

def battle(player, enemy, is_boss=False):

    print("\n================================")
    print("          BATTLE START")
    print("================================")

    print("Enemy:", enemy["name"])
    print("Enemy HP:", enemy["hp"])

    defending = False

    while player["hp"] > 0 and enemy["hp"] > 0:

        print("\n--------------------------------")
        print(player["name"], "HP:", player["hp"], "/", player["max_hp"])
        print("Mana:", player["mana"], "/", player["max_mana"])

        print(enemy["name"], "HP:", enemy["hp"], "/", enemy["max_hp"])

        choice = ask_choice(
            "What will you do?",
            [
                "Attack",
                "Skills",
                "Heal",
                "Use Potion",
                "Defend",
                "Inventory",
                "View Stats",
                "Run"
            ]
        )

        took_turn = False

        if choice == 1:

            attack_enemy(player, enemy)

            took_turn = True

        elif choice == 2:

            took_turn = use_skill(player, enemy)

        elif choice == 3:

            player["hp"] += 50

            if player["hp"] > player["max_hp"]:
                player["hp"] = player["max_hp"]

            print("You recovered 50 HP!")

            took_turn = True

        elif choice == 4:

            took_turn = use_potion(player)

        elif choice == 5:

            defending = True

            print("You are defending!")

            took_turn = True

        elif choice == 6:

            inventory_menu(player)

        elif choice == 7:

            show_stats(player)

        elif choice == 8:

            if is_boss:

                print("You cannot escape from a boss battle!")

            else:

                if random.random() < 0.50:

                    print("You escaped successfully!")
                    return False

                print("You failed to escape!")

                took_turn = True

        # Enemy attacks after the player's action.
        if enemy["hp"] <= 0:
            break

        if took_turn:

            enemy_attack(player, enemy, defending)

            defending = False

            # Reduce temporary buff duration after a battle turn.
            if player["buffs"]["turns"] > 0:

                player["buffs"]["turns"] -= 1

                if player["buffs"]["turns"] == 0:

                    player["buffs"]["attack"] = 0
                    player["buffs"]["defense"] = 0
                    player["buffs"]["crit"] = 0

                    print("Your temporary boosts have ended.")

    # Check battle result.
    if player["hp"] <= 0:

        print("\nYou have been defeated!")

        return False

    print("\nYou defeated", enemy["name"], "!")

    if not is_boss:
        player["enemies_defeated"] += 1

    gain_exp(player, enemy["exp"])

    loot_drop(player, enemy)

    if is_boss:
        print("\nBOSS DEFEATED!")

    return True


# ==========================================
# 19. WORLD MAP
# ==========================================

def show_map(player):

    print("\n========== WORLD MAP ==========")

    for number, region in enumerate(REGIONS):

        if number <= player["unlocked_region"]:
            print("[UNLOCKED]", region)

        else:
            print("[LOCKED]", region)

    print("===============================")


# ==========================================
# 20. EXPLORE THE WORLD
# ==========================================

def explore(player):

    show_map(player)

    print("\nYou are exploring the world...")

    enemy = make_enemy(player["level"])

    print("\nAn enemy appeared!")
    print("Enemy:", enemy["name"])
    print("Enemy Level:", enemy["level"])

    return battle(player, enemy)
