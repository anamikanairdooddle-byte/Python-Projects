
# ==========================================
# LEGENDS OF THE FORGOTTEN REALM
# File: game.py
# Purpose: Connect all game systems
# ==========================================

import time

from data import CLASSES, BOSSES

from player import create_player

from systems import (
    ask_choice,
    show_stats,
    inventory_menu,
    shop,
    explore,
    show_map,
    make_boss,
    battle
)

from storage import save_game, load_game


# ==========================================
# 1. DISPLAY GAME TITLE
# ==========================================

def show_title():

    print("\n")
    print("==============================================")
    print("       LEGENDS OF THE FORGOTTEN REALM")
    print("==============================================")
    print("       A Journey Through Darkness")
    print("==============================================")


# ==========================================
# 2. DISPLAY INSTRUCTIONS
# ==========================================

def instructions():

    show_title()

    print("\n========== GAME INSTRUCTIONS ==========")

    print("\nSTORY")
    print("The kingdom of Eldoria has fallen into darkness.")
    print("You must become a hero and defeat the Ancient Demon King.")

    print("\nCHARACTER CLASSES")
    print("Warrior  - Strong health and defense.")
    print("Mage     - Powerful magic and mana.")
    print("Archer   - High critical hit chance.")
    print("Assassin - High attack and critical damage.")

    print("\nBATTLE ACTIONS")
    print("1. Attack       - Perform a normal attack.")
    print("2. Skills       - Use your class abilities.")
    print("3. Heal         - Restore 50 health.")
    print("4. Use Potion   - Restore health or mana.")
    print("5. Defend       - Reduce the next attack by 50%.")
    print("6. Inventory    - Manage your items.")
    print("7. View Stats   - Check your character.")
    print("8. Run          - Try to escape a normal battle.")

    print("\nLEVELS AND BOSSES")
    print("Bosses appear at every 10th level.")
    print("Defeat each boss to unlock the next level range.")
    print("Reach level 100 and defeat the Ancient Demon King.")

    print("\nSAVING")
    print("Use Save Game in the adventure menu.")
    print("Choose Continue from the main menu to load progress.")

    print("\n=======================================")

    input("\nPress Enter to return to the main menu...")


# ==========================================
# 3. CREATE A NEW CHARACTER
# ==========================================

def character_creation():

    show_title()

    print("\n========== CREATE YOUR HERO ==========")

    while True:

        name = input("Enter your character name: ").strip()

        if name != "":
            break

        print("Name cannot be empty.")

    class_names = list(CLASSES.keys())

    print("\nChoose your character class:")

    for number, class_name in enumerate(class_names, 1):

        details = CLASSES[class_name]

        print("\n", number, ".", class_name)
        print(details["description"])

        print("HP:", details["hp"])
        print("Mana:", details["mana"])
        print("Attack:", details["attack"])
        print("Defense:", details["defense"])

    choice = ask_choice(
        "Select your class:",
        class_names
    )

    selected_class = class_names[choice - 1]

    player = create_player(name, selected_class)

    print("\n================================")
    print("Your hero has been created!")
    print("================================")

    print("Name:", player["name"])
    print("Class:", player["class"])

    return player


# ==========================================
# 4. CHECK WHETHER A BOSS IS REQUIRED
# ==========================================

def boss_encounter(player):

    next_boss_level = (
        player["bosses_defeated"] + 1
    ) * 10

    # The player must fight the boss at the milestone level.
    if player["level"] == next_boss_level:

        boss = make_boss(next_boss_level)

        if boss is None:
            print("Boss information could not be found.")
            return False

        print("\n================================")
        print("         BOSS CHALLENGE")
        print("================================")

        print("A powerful enemy blocks your journey!")
        print("Boss:", boss["name"])
        print("Boss Level:", boss["level"])
        print("Boss HP:", boss["hp"])

        input("\nPress Enter to begin the boss battle...")

        won = battle(player, boss, True)

        if not won:

            if player["hp"] <= 0:
                return False

            print("\nYou escaped the boss challenge.")
            return True

        # Update progression after defeating the boss.
        player["bosses_defeated"] += 1

        player["unlocked_region"] = min(
            player["bosses_defeated"],
            9
        )

        print("\n================================")
        print("       NEW REGION UNLOCKED!")
        print("================================")

        if player["bosses_defeated"] < 10:

            from data import REGIONS

            print(
                "You unlocked:",
                REGIONS[player["unlocked_region"]]
            )

        return True

    return True


# ==========================================
# 5. VICTORY SUMMARY
# ==========================================

def victory_summary(player, start_time):

    total_time = int(time.time() - start_time)

    minutes = total_time // 60
    seconds = total_time % 60

    final_score = (
        player["level"] * 100
        + player["gold"]
        + player["bosses_defeated"] * 500
        + player["enemies_defeated"] * 50
        + player["rare_items_found"] * 100
    )

    show_title()

    print("\n==============================================")
    print("             CONGRATULATIONS!")
    print("==============================================")

    print("You defeated the Ancient Demon King!")
    print("Eldoria has been saved from darkness.")

    print("\n========== VICTORY SUMMARY ==========")

    print("Player Name:", player["name"])
    print("Final Level:", player["level"])
    print("Total Gold:", player["gold"])

    print("Bosses Defeated:", player["bosses_defeated"])
    print("Enemies Defeated:", player["enemies_defeated"])

    print("Weapons Collected:", player["weapons_collected"])
    print("Rare Items Found:", player["rare_items_found"])

    print(
        "Total Play Time:",
        minutes,
        "minutes",
        seconds,
        "seconds"
    )

    print("Final Score:", final_score)

    print("=====================================")

    save_game(player)

    input("\nPress Enter to return to the main menu...")


# ==========================================
# 6. GAME OVER MENU
# ==========================================

def game_over(player):

    while True:

        print("\n================================")
        print("            GAME OVER")
        print("================================")

        print("Your adventure has ended.")

        choice = ask_choice(
            "What would you like to do?",
            [
                "Retry",
                "Load Save",
                "Exit"
            ]
        )

        if choice == 1:

            # Restart with the same name and character class.
            new_player = create_player(
                player["name"],
                player["class"]
            )

            return new_player

        elif choice == 2:

            loaded_player = load_game()

            if loaded_player is not None:
                return loaded_player

        elif choice == 3:

            return None


# ==========================================
# 7. MAIN ADVENTURE MENU
# ==========================================

def adventure(player):

    start_time = time.time()

    while True:

        # Check whether the player has been defeated.
        if player["hp"] <= 0:

            player = game_over(player)

            if player is None:
                return

            start_time = time.time()

        # Check whether the final boss has been defeated.
        if player["bosses_defeated"] >= 10:

            victory_summary(player, start_time)

            return

        # Automatically start a boss battle at each milestone.
        boss_result = boss_encounter(player)

        if not boss_result:
            continue

        if player["hp"] <= 0:
            continue

        if player["bosses_defeated"] >= 10:
            continue

        print("\n================================")
        print("          ADVENTURE MENU")
        print("================================")

        print("Hero:", player["name"])
        print("Class:", player["class"])
        print("Level:", player["level"])
        print("Gold:", player["gold"])

        choice = ask_choice(
            "What would you like to do?",
            [
                "Explore",
                "Visit Village Shop",
                "Inventory",
                "View Player Stats",
                "World Map",
                "Save Game",
                "Return to Main Menu"
            ]
        )

        if choice == 1:

            won = explore(player)

            if not won and player["hp"] <= 0:
                continue

        elif choice == 2:

            shop(player)

        elif choice == 3:

            inventory_menu(player)

        elif choice == 4:

            show_stats(player)

        elif choice == 5:

            show_map(player)

        elif choice == 6:

            save_game(player)

        elif choice == 7:

            print("\nReturning to the main menu...")

            return


# ==========================================
# 8. MAIN MENU
# ==========================================

def main_menu():

    while True:

        show_title()

        choice = ask_choice(
            "========== MAIN MENU ==========",
            [
                "New Game",
                "Continue",
                "Instructions",
                "Exit"
            ]
        )

        if choice == 1:

            player = character_creation()

            adventure(player)

        elif choice == 2:

            player = load_game()

            if player is not None:
                adventure(player)

        elif choice == 3:

            instructions()

        elif choice == 4:

            print("\nThank you for playing!")
            print("May your legend never be forgotten.")

            break
