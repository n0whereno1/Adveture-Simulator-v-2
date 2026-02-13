import random

armors = [
    {"name": "Old Shirt", "ar":2},
    {"name": "Leather Armor", "ar":5},
    {"name": "Iron Plate", "ar":10},
    {"name": "Steel Mail", "ar":15},
    {"name": "Wizard Robe", "ar":3},
    {"name": "Debug Hat", "ar":500},
]


def random_armor():
    lootselect = random.randomint(0, 100)
    if lootselect <= 50:
        armor = random.choice(armors)
        return armor
    else:
        print("You found nothing")
        return "Nothing"
