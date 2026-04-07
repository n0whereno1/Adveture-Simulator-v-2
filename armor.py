import random

common = [
    {"name": "Old Shirt", "ar":2},
    {"name": "Leather Armor", "ar":5},
    {"name": "Iron Plate", "ar":10},
    {"name": "Ring of Zhitpaant", "ar":0},
]

rare = [
    {"name": "Steel Mail", "ar":15},
    {"name": "Wizard Robe", "ar":3},
]

mythical = [
    {"name": "Debug Hat", "ar":500},
]


#def random_armor():
#    lootselect = random.randomint(0, 100)
#    if lootselect <= 50:
#        armor = random.choice(armors)
#        return armor
#    else:
#        print("You found nothing")
#        return "Nothing"

def random_armor():
    lootselect = random.randint(0, 100)
    if lootselect <= 50 and lootselect >= 30:
        armor = random.choice(common)
        return armor
    elif lootselect >=51 and lootselect <= 60:
        armor = random.choice(rare)
        return armor
    elif lootselect <=99 and lootselect >= 97:
        armor = random.choice(mythical)
        return armor
    else:
        return "Nothing"