import random

weapons = [
    {"name": "Stick", "ar":2},
    {"name": "Wooden Sword", "ar":3},
    {"name": "Iron Sword", "ar":10},
    {"name": "Sword of Annihilation", "ar":50},
    {"name": "Old Sock", "ar":3},
    {"name": "Steel Sword", "ar":15},
    {"name": "Wand of Fire", "ar":20},
    {"name": "Debug Stick", "ar":500},
    {"name": "Cheec Klaper", "ar":23},
    {"name": "Apprentice Sword", "ar":12},
]


def random_loot():
    lootselect = random.randomint(0, 100)
    if lootselect <= 50:
        weapon = random.choice(weapons)
        return weapon
    else:
        print("You found nothing")
        return "Nothing"
