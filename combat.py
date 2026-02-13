import random

enemies = {
1:["Crazy Rat", 10, 1],
2:["Aggressive Rock", 50, 0],
3:["Mushroom Man", 15, 5]
}

def combat():
    enemySelect = random.randint(1, 3)
    enemy = enemies[enemySelect]
    return enemy
   # name = enemy[0]
  #  eHealth = enemy[1]
 #   eDamage = enemy[2]
#    print(name, eHealth, eDamage)
