import random
import combat
import loot

state = 0
playing = True
playerInfo = {"Health":"100", "Weapon":"", "Armor":"", "Potions":"2", "Sanity":"100"}
enemy = []


def input_validator(pCHoice):
    valid = False
    while valid == False:
        if pCHoice == "Stats" or pCHoice == "stats":
            #stat_Check()
            print(playerInfo)
            pCHoice = input("Make a selection: ")
        elif pCHoice.isnumeric() and int(pCHoice) > 0 and int(pCHoice) < 4:
            valid == True
            playing == True
            return pCHoice
        else:
            print("Invalid Input, Please use the number associated with the option.\n")
            pCHoice = input("Enter the number associated with the option! ")

def Random_Encounter():
    if random.randomint(0, 100) <= 30:
        enemy = combat()
        print(f"A {enemy['name']} appears!")
        enemyhealth = enemy['health']
        enemyattack = enemy['attack']

def chest_loot():
    if random.randomint(0, 100) <= 30:
        itemget = loot()
        if itemget == "Nothing":
            print("You found nothing")
        else:
            print(f"You found an Item!\n It is {itemget[name]}!")


print ("Welcome to Adventure simulator!! Please choose an option: (Use the number associated to continue)")
print ("1. Dark Forest")
print ("2. Coastal Beach")
print ("3. Flower Filled Meadow")

#pCHoice = input()
#input_validator(pCHoice)
pCHoice = input_validator(input("Enter the number associated with the option! "))

match pCHoice:
    case "1":
        state = 1
    case "2":
        state = 2
    case "3":
        state = 3


while playing == True:

    match state:
        case 1:
            print("You enter the dark forest and you see a path surrounded by thick pine and oak trees, choose the option you wish to procede with\n 1. Travel down the path\n 2. Go through the trees\n 3. Stay where you are")
            pCHoice = pCHoice = input_validator(input("Enter the number associated with the option! "))
            match pCHoice:
                case "1":
                    state = 4
                case "2":
                    state = 5
                    print("boo")
                case "3":
                    state = 6
                    print("boo")
        case 2:
            print("You stand on a coastal beach. The sun is glistening on the water surface choose the option you wish to procede with\n 1. Go North\n 2. Go South\n 3. Swim into the sea")
            pCHoice = pCHoice = input_validator(input("Enter the number associated with the option! "))
            match pCHoice:
                case "1":
                    state = 7
                    print("boo")
                case "2":
                    state = 8
                    print("boo")
                case "3":
                    state = 9
                    print("boo")
        case 3:
            print("The floor under your feet caves in and you get knocked out on the fall. When you wake you are in an aged room walled with mossy bricks. There are three doors, choose the option you wish to procede with\n 1. Left\n 2. Center\n 3. Right")
            pCHoice = pCHoice = input_validator(input("Enter the number associated with the option! "))
            match pCHoice:
                case "1":
                    state = 10
                    print("boo")
                case "2":
                    state = 11
                    print("boo")
                case "3":
                    state = 12
                    print("boo")
        case 4:
            print("Traveling down the path you hear a sound that sounds like a scream and see a fork in the path. What do you do?\n 1. Follow it\n 2. Turn down the path\n 3. Turn back and run")
            pCHoice = pCHoice = input_validator(input("Enter the number associated with the option! "))
            match pCHoice:
                case "1":
                    state = 10
                    print("boo")
                case "2":
                    state = 11
                    print("boo")
                case "3":
                    state = 12
                    print("boo")
        case 5:
            print("Traveling down the path you hear a sound that sounds like a scream and see a fork in the path. What do you do?\n 1. Follow it\n 2. Turn down the path\n 3. Turn back and run")
            pCHoice = pCHoice = input_validator(input("Enter the number associated with the option! "))
            match pCHoice:
                case "1":
                    state = 10
                    print("boo")
                case "2":
                    state = 11
                    print("boo")
                case "3":
                    state = 12
                    print("boo")
        case 6:
            print("Traveling down the path you hear a sound that sounds like a scream and see a fork in the path. What do you do?\n 1. Follow it\n 2. Turn down the path\n 3. Turn back and run")
            pCHoice = pCHoice = input_validator(input("Enter the number associated with the option! "))
            match pCHoice:
                case "1":
                    state = 10
                    print("boo")
                case "2":
                    state = 11
                    print("boo")
                case "3":
                    state = 12
                    print("boo")
        case 7:
            print("Traveling down the path you hear a sound that sounds like a scream and see a fork in the path. What do you do?\n 1. Follow it\n 2. Turn down the path\n 3. Turn back and run")
            pCHoice = pCHoice = input_validator(input("Enter the number associated with the option! "))
            match pCHoice:
                case "1":
                    state = 10
                    print("boo")
                case "2":
                    state = 11
                    print("boo")
                case "3":
                    state = 12
                    print("boo")