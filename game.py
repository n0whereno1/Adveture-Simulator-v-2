import random
import combat

state = 0
playerInfo = {"Health":"100", "Weapon":"", "Armor":"", "Potions":"2", "Sanity":"100"}
enemy = []

weapons = {
"Stick":1,
"Wooden Sword":2,
"Iron Sword":10,
"Sword of Annihilation":50,
"Old Sock":5,
"Feather":1,
"Steel Sword":15,
"Wand of Fire":13
}

armors = {
"Old Shirt":2,
"Leather Armor":5,
"Iron Plate":10,
"Steel Mail":15,
"Wizard Robes":3
}


def input_validator(pCHoice):
    valid = False
    while valid == False:
        if pCHoice == "Stats" or pCHoice == "stats":
            #stat_Check()
            print(playerInfo)
            pCHoice = input("Make a selection: ")
        elif pCHoice.isnumeric() and int(pCHoice) > 0 and int(pCHoice) < 4:
            valid == True
            return pCHoice
        else:
            print("Invalid Input, Please use the number associated with the option.\n")
            pCHoice = input("Enter the number associated with the option! ")


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

match state:
    case 1:
        print("You enter the dark forest and you see a path surrounded by thick pine and oak trees, choose the option you wish to procede with\n1. Travel down the path\n 2. Go through the trees\n 3. Stay where you are")
        pCHoice = pCHoice = input_validator(input("Enter the number associated with the option! "))
        match pCHoice:
            case "1":
                print("boo")
            case "2":
                print("boo")
            case "3":
                print("boo")
    case 2:
        print("You stand on a coastal beach. The sun is glistenig on the water surface choose the option you wish to procede with\n1. Travel down the path\n 2. Go through the trees\n 3. Stay where you are")
        pCHoice = pCHoice = input_validator(input("Enter the number associated with the option! "))
    case 3:
        print("You enter the dark forest and you see a path surrounded by thick pine and oak trees, choose the option you wish to procede with\n1. Travel down the path\n 2. Go through the trees\n 3. Stay where you are")
        pCHoice = pCHoice = input_validator(input("Enter the number associated with the option! "))
