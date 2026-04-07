import random

common = [
    {"name": "Stick", "ar":2},
    {"name": "Wooden Sword", "ar":3},
    {"name": "Iron Sword", "ar":10},
    {"name": "Old Sock", "ar":3},
    {"name": "Apprentice Sword", "ar":12},
]

rare = [
    {"name": "Steel Sword", "ar":15},
    {"name": "Wand of Fire", "ar":20},
]

mythical = [
    {"name": "Debug Stick", "ar":500},
    {"name": "Cheec Klaper", "ar":23},
]

def random_loot():
    lootselect = random.randint(0, 100)
    if lootselect <= 50 and lootselect >= 30:
        weapon = random.choice(common)
        return weapon
    elif lootselect >=51 and lootselect <= 60:
        weapon = random.choice(rare)
        return weapon
    elif lootselect <=99 and lootselect >= 97:
        weapon = random.choice(mythical)
        return weapon
    else:
        return "Nothing"
