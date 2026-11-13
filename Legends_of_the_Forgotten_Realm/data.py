
# ==========================================
# LEGENDS OF THE FORGOTTEN REALM
# File: data.py
# Purpose: Store all game information
# ==========================================


# 1. WEAPON RARITY INFORMATION

RARITY_MULTIPLIERS = {
    "Common": 1.0,
    "Uncommon": 1.1,
    "Rare": 1.3,
    "Super Rare": 1.5,
    "Epic": 1.8,
    "Mythical": 2.2,
    "Legendary": 2.8
}

RARITY_CRIT_BONUS = {
    "Common": 0,
    "Uncommon": 2,
    "Rare": 5,
    "Super Rare": 8,
    "Epic": 12,
    "Mythical": 18,
    "Legendary": 25
}

RARITY_DROP_CHANCES = {
    "Common": 50,
    "Uncommon": 25,
    "Rare": 15,
    "Super Rare": 6,
    "Epic": 3,
    "Mythical": 0.9,
    "Legendary": 0.1
}


# 2. CHARACTER CLASSES

CLASSES = {
    "Warrior": {
        "hp": 160,
        "mana": 55,
        "attack": 19,
        "defense": 14,
        "crit_chance": 5,
        "crit_damage": 2.0,
        "description": "Strong fighter with high health and defense."
    },

    "Mage": {
        "hp": 105,
        "mana": 150,
        "attack": 24,
        "defense": 6,
        "crit_chance": 12,
        "crit_damage": 2.0,
        "description": "Powerful magic user with high mana."
    },

    "Archer": {
        "hp": 120,
        "mana": 90,
        "attack": 17,
        "defense": 9,
        "crit_chance": 20,
        "crit_damage": 2.0,
        "description": "Accurate fighter with a higher critical chance."
    },

    "Assassin": {
        "hp": 95,
        "mana": 100,
        "attack": 25,
        "defense": 5,
        "crit_chance": 28,
        "crit_damage": 2.0,
        "description": "Fast attacker with high critical damage potential."
    }
}


# 3. WEAPONS
# Each weapon has a name, rarity, damage, critical bonus,
# price, and minimum required level.

WEAPONS = [
    {"name": "Wooden Sword", "rank": "Common",
        "damage": 5, "price": 50, "required_level": 1},
    {"name": "Iron Sword", "rank": "Common",
        "damage": 10, "price": 100, "required_level": 3},
    {"name": "Hunter Bow", "rank": "Common",
        "damage": 8, "price": 90, "required_level": 3},
    {"name": "Apprentice Staff", "rank": "Common",
        "damage": 9, "price": 100, "required_level": 3},

    {"name": "Steel Sword", "rank": "Uncommon",
        "damage": 15, "price": 250, "required_level": 5},
    {"name": "Silver Bow", "rank": "Uncommon",
        "damage": 13, "price": 300, "required_level": 7},
    {"name": "Battle Axe", "rank": "Uncommon",
        "damage": 18, "price": 350, "required_level": 8},

    {"name": "Flame Sword", "rank": "Rare", "damage": 25,
        "price": 600, "required_level": 10},
    {"name": "Frost Staff", "rank": "Rare", "damage": 23,
        "price": 650, "required_level": 12},
    {"name": "Shadow Dagger", "rank": "Rare",
        "damage": 27, "price": 700, "required_level": 15},

    {"name": "Dragon Bow", "rank": "Super Rare",
        "damage": 35, "price": 1200, "required_level": 20},
    {"name": "Thunder Hammer", "rank": "Super Rare",
        "damage": 40, "price": 1400, "required_level": 25},
    {"name": "Crystal Staff", "rank": "Super Rare",
        "damage": 38, "price": 1500, "required_level": 30},

    {"name": "Demon Slayer", "rank": "Epic", "damage": 55,
        "price": 2500, "required_level": 40},
    {"name": "Phoenix Blade", "rank": "Epic",
        "damage": 60, "price": 2800, "required_level": 45},
    {"name": "Storm Breaker", "rank": "Epic",
        "damage": 65, "price": 3000, "required_level": 50},

    {"name": "Celestial Staff", "rank": "Mythical",
        "damage": 85, "price": 5000, "required_level": 60},
    {"name": "Void Reaper", "rank": "Mythical",
        "damage": 95, "price": 6000, "required_level": 70},

    {"name": "God Slayer", "rank": "Legendary",
        "damage": 120, "price": 10000, "required_level": 80},
    {"name": "Eternal Dragon Blade", "rank": "Legendary",
        "damage": 140, "price": 15000, "required_level": 90},
    {"name": "Ancient Demon Fang", "rank": "Legendary",
        "damage": 160, "price": 20000, "required_level": 100}
]


# Add the rarity-based values to every weapon.
# The game will use these values when calculating damage.

for weapon in WEAPONS:
    weapon["damage_multiplier"] = RARITY_MULTIPLIERS[weapon["rank"]]
    weapon["critical_bonus"] = RARITY_CRIT_BONUS[weapon["rank"]]


# 4. ARMOR
# Armor improves defense, health, mana and critical resistance.

ARMORS = [
    {"name": "Cloth Armor", "rank": "Common", "defense": 3, "hp": 5,
        "mana": 5, "critical_resistance": 0, "price": 50, "required_level": 1},
    {"name": "Leather Armor", "rank": "Common", "defense": 6, "hp": 10,
        "mana": 0, "critical_resistance": 1, "price": 100, "required_level": 3},

    {"name": "Iron Armor", "rank": "Rare", "defense": 12, "hp": 20, "mana": 0,
        "critical_resistance": 3, "price": 500, "required_level": 10},
    {"name": "Mystic Robe", "rank": "Rare", "defense": 8, "hp": 10, "mana": 25,
        "critical_resistance": 3, "price": 600, "required_level": 12},

    {"name": "Knight Armor", "rank": "Super Rare", "defense": 20, "hp": 35,
        "mana": 0, "critical_resistance": 5, "price": 1200, "required_level": 20},
    {"name": "Ranger Armor", "rank": "Super Rare", "defense": 17, "hp": 25,
        "mana": 10, "critical_resistance": 6, "price": 1400, "required_level": 25},

    {"name": "Dragon Scale Armor", "rank": "Epic", "defense": 30, "hp": 50,
        "mana": 10, "critical_resistance": 10, "price": 2500, "required_level": 40},
    {"name": "Arcane Robe", "rank": "Epic", "defense": 25, "hp": 25, "mana": 50,
        "critical_resistance": 12, "price": 2800, "required_level": 45},

    {"name": "Phoenix Armor", "rank": "Mythical", "defense": 45, "hp": 75,
        "mana": 25, "critical_resistance": 15, "price": 5000, "required_level": 60},
    {"name": "Shadow Armor", "rank": "Mythical", "defense": 50, "hp": 60,
        "mana": 30, "critical_resistance": 18, "price": 6000, "required_level": 70},

    {"name": "Celestial Armor", "rank": "Legendary", "defense": 65, "hp": 100,
        "mana": 50, "critical_resistance": 25, "price": 10000, "required_level": 80},
    {"name": "Demon King Armor", "rank": "Legendary", "defense": 80, "hp": 150,
        "mana": 60, "critical_resistance": 30, "price": 15000, "required_level": 90}
]


# 5. POTIONS
# Potions can restore health/mana or temporarily improve abilities.

POTIONS = [
    {"name": "Small Health Potion", "type": "health", "value": 50, "price": 30},
    {"name": "Health Potion", "type": "health", "value": 100, "price": 60},
    {"name": "Large Health Potion", "type": "health", "value": 250, "price": 120},
    {"name": "Greater Health Potion", "type": "health", "value": 500, "price": 250},
    {"name": "Full Health Potion", "type": "health", "value": "full", "price": 500},

    {"name": "Small Mana Potion", "type": "mana", "value": 30, "price": 30},
    {"name": "Mana Potion", "type": "mana", "value": 75, "price": 60},
    {"name": "Large Mana Potion", "type": "mana", "value": 150, "price": 120},
    {"name": "Greater Mana Potion", "type": "mana", "value": 300, "price": 250},
    {"name": "Full Mana Potion", "type": "mana", "value": "full", "price": 500},

    {"name": "Healing Mix", "type": "mixed",
        "health": 50, "mana": 30, "price": 100},
    {"name": "Power Mix", "type": "mixed", "health": 100, "mana": 75, "price": 200},
    {"name": "Supreme Mix", "type": "mixed",
        "health": 250, "mana": 150, "price": 400},

    {"name": "Attack Boost Potion", "type": "buff",
        "effect": "attack", "value": 20, "duration": 3, "price": 150},
    {"name": "Defense Boost Potion", "type": "buff",
        "effect": "defense", "value": 20, "duration": 3, "price": 150},
    {"name": "Critical Boost Potion", "type": "buff",
        "effect": "crit", "value": 15, "duration": 3, "price": 200}
]


# 6. ENEMIES
# There are 25 different enemies across levels 1 to 100.
# Each enemy has a level range and basic battle statistics.

ENEMIES = [
    {"name": "Forest Slime", "min_level": 1, "max_level": 4,
        "hp": 40, "attack": 8, "defense": 2, "exp": 20, "gold": 10},
    {"name": "Wild Wolf", "min_level": 1, "max_level": 4, "hp": 55,
        "attack": 10, "defense": 3, "exp": 25, "gold": 15},
    {"name": "Goblin Scout", "min_level": 1, "max_level": 4,
        "hp": 65, "attack": 12, "defense": 4, "exp": 30, "gold": 20},

    {"name": "Cave Bat", "min_level": 5, "max_level": 8, "hp": 100,
        "attack": 18, "defense": 6, "exp": 50, "gold": 30},
    {"name": "Stone Lizard", "min_level": 5, "max_level": 8,
        "hp": 130, "attack": 20, "defense": 10, "exp": 60, "gold": 35},
    {"name": "Bandit Fighter", "min_level": 5, "max_level": 9,
        "hp": 145, "attack": 23, "defense": 8, "exp": 65, "gold": 40},

    {"name": "Desert Scorpion", "min_level": 11, "max_level": 19,
        "hp": 230, "attack": 35, "defense": 15, "exp": 100, "gold": 60},
    {"name": "Sand Wraith", "min_level": 11, "max_level": 19,
        "hp": 250, "attack": 38, "defense": 12, "exp": 110, "gold": 70},
    {"name": "Ruins Guardian", "min_level": 11, "max_level": 19,
        "hp": 300, "attack": 40, "defense": 20, "exp": 125, "gold": 80},

    {"name": "Vampire Spawn", "min_level": 21, "max_level": 29,
        "hp": 420, "attack": 55, "defense": 25, "exp": 180, "gold": 100},
    {"name": "Dark Knight", "min_level": 21, "max_level": 29, "hp": 470,
        "attack": 60, "defense": 30, "exp": 200, "gold": 120},
    {"name": "Cursed Archer", "min_level": 21, "max_level": 29,
        "hp": 390, "attack": 65, "defense": 20, "exp": 190, "gold": 110},

    {"name": "Lava Beast", "min_level": 31, "max_level": 39, "hp": 650,
        "attack": 80, "defense": 35, "exp": 300, "gold": 180},
    {"name": "Fire Elemental", "min_level": 31, "max_level": 39,
        "hp": 600, "attack": 90, "defense": 30, "exp": 320, "gold": 190},
    {"name": "Demon Hound", "min_level": 31, "max_level": 39, "hp": 700,
        "attack": 85, "defense": 40, "exp": 340, "gold": 200},

    {"name": "Ice Wolf", "min_level": 41, "max_level": 59, "hp": 900,
        "attack": 110, "defense": 45, "exp": 450, "gold": 250},
    {"name": "Frozen Knight", "min_level": 41, "max_level": 59,
        "hp": 1000, "attack": 120, "defense": 55, "exp": 500, "gold": 280},
    {"name": "Frost Witch", "min_level": 41, "max_level": 59, "hp": 850,
        "attack": 130, "defense": 40, "exp": 480, "gold": 270},

    {"name": "Sky Harpy", "min_level": 61, "max_level": 79, "hp": 1300,
        "attack": 160, "defense": 65, "exp": 650, "gold": 350},
    {"name": "Temple Sentinel", "min_level": 61, "max_level": 79,
        "hp": 1500, "attack": 170, "defense": 75, "exp": 700, "gold": 380},
    {"name": "Void Mage", "min_level": 61, "max_level": 79, "hp": 1250,
        "attack": 185, "defense": 60, "exp": 680, "gold": 370},

    {"name": "Demon Soldier", "min_level": 81, "max_level": 100,
        "hp": 1800, "attack": 220, "defense": 90, "exp": 900, "gold": 500},
    {"name": "Abyssal Beast", "min_level": 81, "max_level": 100, "hp": 2000,
        "attack": 240, "defense": 100, "exp": 1000, "gold": 550},
    {"name": "Dark Sorcerer", "min_level": 81, "max_level": 100,
        "hp": 1750, "attack": 250, "defense": 85, "exp": 950, "gold": 520},
    {"name": "Demon Champion", "min_level": 81, "max_level": 100,
        "hp": 2300, "attack": 260, "defense": 110, "exp": 1100, "gold": 600}
]


# 7. BOSSES
# A boss appears at every 10th level.
# Each boss has multiple special skills.

BOSSES = [
    {
        "name": "Goblin King",
        "level": 10,
        "hp": 600,
        "attack": 35,
        "defense": 15,
        "exp": 300,
        "gold": 250,
        "skills": ["Royal Strike", "Goblin Call", "Heavy Smash"]
    },
    {
        "name": "Forest Guardian",
        "level": 20,
        "hp": 1200,
        "attack": 60,
        "defense": 30,
        "exp": 600,
        "gold": 500,
        "skills": ["Root Crush", "Nature's Wrath", "Healing Roots"]
    },
    {
        "name": "Ancient Golem",
        "level": 30,
        "hp": 2000,
        "attack": 90,
        "defense": 50,
        "exp": 1000,
        "gold": 800,
        "skills": ["Earthquake", "Stone Fist", "Rock Shield"]
    },
    {
        "name": "Vampire Lord",
        "level": 40,
        "hp": 3000,
        "attack": 120,
        "defense": 65,
        "exp": 1500,
        "gold": 1200,
        "skills": ["Blood Drain", "Dark Bite", "Nightmare"]
    },
    {
        "name": "Dragon Rider",
        "level": 50,
        "hp": 4500,
        "attack": 160,
        "defense": 80,
        "exp": 2200,
        "gold": 1800,
        "skills": ["Dragon Fire", "Wing Storm", "Flame Breath"]
    },
    {
        "name": "Demon General",
        "level": 60,
        "hp": 6000,
        "attack": 200,
        "defense": 100,
        "exp": 3000,
        "gold": 2500,
        "skills": ["Demon Slash", "Hellfire", "Dark Recovery"]
    },
    {
        "name": "Ice Titan",
        "level": 70,
        "hp": 8000,
        "attack": 240,
        "defense": 125,
        "exp": 4000,
        "gold": 3500,
        "skills": ["Frozen Smash", "Ice Storm", "Absolute Zero"]
    },
    {
        "name": "Shadow Emperor",
        "level": 80,
        "hp": 10500,
        "attack": 290,
        "defense": 150,
        "exp": 5000,
        "gold": 4500,
        "skills": ["Shadow Strike", "Dark Prison", "Soul Drain"]
    },
    {
        "name": "Celestial Dragon",
        "level": 90,
        "hp": 13500,
        "attack": 340,
        "defense": 175,
        "exp": 6500,
        "gold": 6000,
        "skills": ["Celestial Fire", "Starfall", "Divine Roar"]
    },
    {
        "name": "Ancient Demon King",
        "level": 100,
        "hp": 18000,
        "attack": 400,
        "defense": 200,
        "exp": 10000,
        "gold": 10000,
        "skills": ["Apocalypse", "Demon Storm", "Soul Devour"]
    }
]


# 8. WORLD REGIONS
# The next region becomes available after defeating the boss.

REGIONS = [
    "Village",
    "Forest",
    "Cave",
    "Desert",
    "Ruins",
    "Castle",
    "Volcano",
    "Frozen Mountain",
    "Sky Temple",
    "Demon Realm"
]


# 9. CLASS SKILLS
# Skills will be used by the battle system.
# Mana cost and damage multiplier are stored here.

CLASS_SKILLS = {
    "Warrior": [
        {"name": "Slash", "mana": 5, "multiplier": 1.5, "unlock_level": 1},
        {"name": "Shield Bash", "mana": 10, "multiplier": 1.8, "unlock_level": 5},
        {"name": "Rage", "mana": 15, "multiplier": 2.2, "unlock_level": 10},
        {"name": "Earthquake", "mana": 30, "multiplier": 3.0, "unlock_level": 15}
    ],

    "Mage": [
        {"name": "Fireball", "mana": 10, "multiplier": 1.7, "unlock_level": 1},
        {"name": "Ice Blast", "mana": 15, "multiplier": 2.0, "unlock_level": 5},
        {"name": "Thunder Strike", "mana": 25,
            "multiplier": 2.5, "unlock_level": 10},
        {"name": "Meteor", "mana": 40, "multiplier": 3.5, "unlock_level": 15}
    ],

    "Archer": [
        {"name": "Multi Shot", "mana": 8, "multiplier": 1.5, "unlock_level": 1},
        {"name": "Poison Arrow", "mana": 12, "multiplier": 1.8, "unlock_level": 5},
        {"name": "Explosive Arrow", "mana": 20,
            "multiplier": 2.4, "unlock_level": 10},
        {"name": "Sniper Shot", "mana": 35, "multiplier": 3.2, "unlock_level": 15}
    ],

    "Assassin": [
        {"name": "Backstab", "mana": 8, "multiplier": 1.8, "unlock_level": 1},
        {"name": "Smoke Bomb", "mana": 12, "multiplier": 1.5, "unlock_level": 5},
        {"name": "Shadow Strike", "mana": 20,
            "multiplier": 2.5, "unlock_level": 10},
        {"name": "Instant Kill", "mana": 50, "multiplier": 5.0, "unlock_level": 15}
    ]
}
