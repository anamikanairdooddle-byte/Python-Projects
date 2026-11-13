
# ==========================================
# LEGENDS OF THE FORGOTTEN REALM
# File: storage.py
# Purpose: Save and load player progress
# ==========================================

import json
import os


# Name of the file where game progress is stored.
SAVE_FILE = "savegame.json"


# 1. SAVE THE GAME

def save_game(player):

    try:

        # Open the save file in write mode.
        with open(SAVE_FILE, "w") as file:

            # Convert the player dictionary into JSON.
            json.dump(player, file, indent=4)

        print("\nGame saved successfully!")

    except OSError:

        print("\nUnable to save the game.")


# 2. LOAD THE GAME

def load_game():

    # Check whether a save file exists.
    if not os.path.exists(SAVE_FILE):

        print("\nNo saved game found.")
        return None

    try:

        # Open the saved game.
        with open(SAVE_FILE, "r") as file:

            # Convert JSON information back into a dictionary.
            player = json.load(file)

        print("\nGame loaded successfully!")

        return player

    except (OSError, json.JSONDecodeError):

        print("\nUnable to load the saved game.")
        return None


# 3. DELETE THE SAVED GAME

def delete_save():

    if os.path.exists(SAVE_FILE):

        try:

            os.remove(SAVE_FILE)

            print("\nSaved game deleted.")

        except OSError:

            print("\nUnable to delete the saved game.")

    else:

        print("\nNo saved game exists.")
