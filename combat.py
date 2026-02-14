import random

enemies = [
    {"name": "Bandit", "hp": 50, "attack": 10},
    {"name": "Orc", "hp": 80, "attack": 20},
    {"name": "Wolf", "hp": 30, "attack": 6},
    {"name": "Crazy Rat", "hp": 10, "attack": 1},
    {"name": "Mushroom Man", "hp": 15, "attack": 5},
    {"name": "Greg", "hp": 1, "attack": 1},
    {"name": "Archibald", "hp": 5, "attack": 5},
    {"name": "Graham", "hp": 150, "attack": 1},
]

def combat():
    enemy = random.choice(enemies)
    return enemy

#combat()
