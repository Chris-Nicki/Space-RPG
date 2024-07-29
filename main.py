import os
import shutil
import random
# from rules import Rules

###################################################################################
# Line Break Function
def line_break():
    terminal_width = shutil.get_terminal_size().columns
    line = '-' * terminal_width
    print(line)

# Clear Function
def clear():
    os.system('cls')

# Draw Function
def draw():
    print("Xx----------------------------xX")

##################################################################################
#  Game Loops
run = True
menu = True
play = False
rules = False
key1 = False
key2 = False
fight = False
standing = True
buy = False
speak =  False
boss1 = False
boss2 = False
astroid_damage = False

# Character Traits
HP = 100
HPMAX = HP
ATK = 5
shield_boost = 1
ship_repair = 0
quantanium = 0
x = 0
y = 0
key1 = 0
key2 = 0


# MAPPING
# Map           x=0                    x=1              x=2                x=3             x=4              x=5
map = [ [  "seraphin_station",         "space", "astroid_field",         "space",       "orrison",  "cave_orrison"], # y = 0
        [             "space",         "space",        "arc_l1",         "space",         "space",         "space"], # y = 1
        [             "space",         "lyria",         "space",         "space", "astroid_field",         "wreck"], # y = 2
        [             "space",         "space",         "space",          "yela",         "space", "astroid_field"], # y = 3
        [     "astroid_field",         "space", "astroid_field",         "space",       "hurl_l1",         "space"], # y = 4
        ["hurston_jump_point", "astroid_field",         "wreck", "astroid_field",         "space",        "arc_l2"], # y = 5
        [            "daymar",         "space", "astroid_field", "astroid_field",         "space",         "space"], # y = 6
        [     "astroid_field",         "space",      "grim_hex",         "space",       "hurston",       "hurl_l2"], # y = 7
                                                                                                     
       ]

y_len = len(map) - 1
x_len = len(map[0]) - 1

biom = {
    "seraphin_station": {
        "t": "SERAPHIN STATION",
        "enemy": False,
        "trader": True},
    "space": {
        "t": "SPACE",
        "enemy": True,
        "trader": False},
    "astroid_field": {
        "t": "ASTROID FIELD",
        "enemy": False,
        "trader": False},
    "orrison": {
        "t": "ORRISON",
        "enemy": True,
        "trader": True},
    "cave_orrison" : { # Gives you key to hurston jump point, needs Boss 1 ?
        "t": "CAVE ON ORRISON",
        "enemy": False,
        "trader": False},
    "arc_l1": {
        "t": "ARC-L1",
        "enemy": False,
        "trader": False},
    "lyria": {
        "t": "LYRIA",

        "enemy": True,
        "trader": True},
    "wreck": { # Gives you key to Cave on orrison, needs connie spawn only
        "t": "WRECK",
        "enemy": True,
        "trader": False},
    "yela": {
        "t": "YELA",
        "enemy": True,
        "trader": True},
    "hurl_l1": {
        "t": "HURL-L1",
        "enemy": False,
        "trader": True},
    "hurston_jump_point": { # Entry with key from cave-1, needs Arrasta spawn only
        "t": "HURSTON JUMP POINT",
        "enemy": False,
        "trader": False},
    "arc_l2": {
        "t": "ARC_L2",
        "enemy": False,
        "trader": True},
    "daymar": {
        "t": "DAYMAR",
        "enemy": True,
        "trader": True},
    "grim_hex": { # Lower trading prices, need to be in high risk area, may be enemy spawn as before trader?
        "t": "GRIM HEX",
        "enemy": True,
        "trader": True},
    "hurston": {
        "t": "HURSTON",
        "enemy": False,
        "trader": True},
    "hurl_l2": {
        "t": "HURL_L2",
        "enemy": False,
        "trader": True}
    }

current_tile = map[y][x]

# Enemy Ships
enemy_list = ["Vulture", "Cutlass-Black", "F7C1_Fighter", "Constellation-Andromeda"]

ships = {
    "Vulture": {
        "hp": 20,
        "at": 2,
        "quant": 10
    },
    "Cutlass-Black": {
        "hp": 20,
        "at": 2,
        "quant": 20
    },
    "F7C1_Fighter": {
        "hp": 20,
        "at": 2,
        "quant": 25
    },
    "Constellation-Andromeda": {
        "hp": 20,
        "at": 2,
        "quant": 45
    },
    "OT-Mega": { # Cave 1 Boss
        "hp": 20,
        "at": 2,
        "quant": 75
    },
    "Arrasta": { # Cave 2 Boss
        "hp": 20,
        "at": 2,
        "quant": 100
    }
}

# Save Function
def save():
    list = [
        name,
        str(HP),
        str(ATK),
        str(shield_boost),
        str(ship_repair),
        str(quantanium),
        str(x),
        str(y),
        str(key1),
        str(key2)
    ]

    f = open("load.txt", "w")

    for item in list:
        f.write(item + "\n")
    f.close()

# Heal Function
def heal(amount):
    global HP
    if HP + amount < HPMAX:
        HP += amount
    else:
        HP = HPMAX
        print(f"{name} 's HP refilled to  {HP}!")

# Battle Function
def battle():
    global fight, play, run, menu, HP, shield_boost, ship_repair, quantanium, boss1, boss2, key2
    
    boss1 = "OT_Mega"
    boss2 = "Arrasta"

    if not boss1 or boss2:
        enemy = random.choice(enemy_list)

    elif boss1:
        enemy = "OT-Mega"
              
    else:
        enemy = "Arrasta"

    hp = ships[enemy]["hp"]
    hpmax = hp 
    atk = ships[enemy]["at"]
    q = ships[enemy]["quant"]

    while fight:
        clear()
        draw()
        print(f"Enemy ship inbound, defeat the {enemy}!")
        draw()
        print(f"{enemy}'s HP: {str(hp)} / {str(hpmax)}")
        print(f"{name}'s HP: {HP} / {HPMAX}")
        print(f"Shield Boost:  {shield_boost}")
        print(f"Ship Repair: {ship_repair}")
        draw()
        print("1 - ATTACK")
        if shield_boost > 0:
            print("2 - USE SHIELD BOOST (25HP")
        if ship_repair > 0:
            print("3 - USE SHIP REPAIR (50HP)")
        draw()

        choice = input("# ")
        
        if choice == "1":
            hp -= ATK
            print(f"{name} dealt {ATK} damage to the {enemy}.")
            if hp > 0:
                HP -= atk 
                print(f"{enemy} dealt {atk} damage to {name}.")
            input("> ")

        elif choice == "2":
            if shield_boost > 0:
                shield_boost - 1
                heal(25)
                HP -= atk
                print(f"{enemy} dealt {atk} damage to {name}.")
            else:
                print("No shield boosts!")
            input("> ")

        elif choice == "3":
            if ship_repair > 0:
                ship_repair - 1
                heal(50)
                HP -= atk
                print(f"{enemy} dealt {atk} damage to {name}.")
            else:
                print("No ship repair kits!")
            input("> ")
        
        if HP <= 0:
            print(f"{enemy} defeated {name}.....")
            draw()
            fight = False
            play = False
            run = False
            print("Game Over")
            input("> ")

        if hp <= 0:
            print(f"{name} defeated the {enemy}!")               
            draw()
            fight = False
            quantanium += q
            print(f"You've found {q} quantanium!")
            if random.randint(0, 100) < 25:
                shield_boost += 1
                print("You've found a shield boost!")

        if enemy == "OT-Mega":
            draw()
            print("Congratulations, you have destroyed the OT-Mega! Take the access card for Hurston Jump Point.")
            boss1 = False
            key2 = True
            play = True
            run = True
        input("> ")

        if enemy == "Arrasta":
            draw()
            print("Congratulations, you've finished the game!")        
            boss2 = False
            play = False
            run = False
        input("> ")
        clear()

def astroid_field():
    global HP, play, astroid_damage
    clear()
    draw()
    print("""!!!WARNING!!!
            !!!WARNING!!!
            ***ASTROID INCOMING***
            Take evasive action to avoid being hit.
            1. Roll Right
            2. Roll Left
            3. Increase Altitude
            4. Decrease Altitude
          """)
    draw()

    choice = input("# ")
    if choice == "1":
        while astroid_damage:
            if random.randint(0,100) < 33:
                print(f"Not quick enough, brace for impact!")
                HP -= 10
                if HP <=0:
                    print("YOU ARE DEAD, GAME OVER!")
                    astroid_damage =False
                    play = False
                else:
                    astroid_damage = False
            else:
                print("Rolled right, contact avoided!")
                astroid_damage = False
    if choice == "2":
        while astroid_damage:
            if random.randint(0,100) < 33:
                print(f"Not quick enough, brace for impact!")
                HP -= 10
                if HP <=0:
                    print("YOU ARE DEAD, GAME OVER!")
                    astroid_damage =False
                    play = False
                else:
                    astroid_damage = False
            else:
                print("Rolled left, contact avoided!")
                astroid_damage = False
    if choice == "3":
        while astroid_damage:
            if random.randint(0,100) < 33:
                print(f"Not quick enough, brace for impact!")
                HP -= 10
                if HP <=0:
                    print("YOU ARE DEAD, GAME OVER!")
                    astroid_damage =False
                    play = False
                else:
                    astroid_damage = False
            else:
                print("Altitude increased, contact avoided!")
                astroid_damage = False
    if choice == "4":
        while astroid_damage:
            if random.randint(0,100) < 33:
                print(f"Not quick enough, brace for impact!")
                HP -= 10
                if HP <=0:
                    print("YOU ARE DEAD, GAME OVER!")
                    astroid_damage =False
                    play = False
                else:
                    astroid_damage = False
            else:
                print("Altitude decreased, contact avoided!")
                astroid_damage = False
   

# Wreck Function
def wreck():
    global speak, key1

    while speak:
        clear()
        draw()
        print(f"Welcome {name}, glad to see you made it through the astroid field!")
        if ATK < 10 :
            print("You're weapons are not strong enough to fight the OT-Mega. Keep destroying enemies to earn quantanium to upgrade your weapons.")
            key1 = False
        else:
            print("Head to the the cave on Orrison, you will find the OT_Mega there. Destroy the ship and take it's contents")
            key1 = True

        draw()
        print("1 - Leave")
        draw()

        choice = input("# ")

        if choice == "1":
            speak = False

# Orrison Cave Boss1 Battle
def cave_orrison():
    global key1, key2, boss1, fight

    while boss1:
        clear()
        draw()
        print("You have arrived at the cave on Orrison, would you like to enter? ")
        draw()
        if key1:
            print("""1. Use Access Card
                    2. Turn Back
                  """)  
        else:
            print("You need the Access Card from the wreck to enter the cave!")
        draw()

        choice = input("# ")

        if choice == "1":
            if key1:
                fight = True
                battle()
        elif choice == "2":
            boss1 = False

# Hurston Jump Point Battle(ENDGAME)
def hurston_jump_point():
    global key2, boss2, fight

    while boss2:
        clear()
        draw()
        print("You have arrived at the Hurston Jump Point, would you like to enter? ")
        draw()
        if key2:
            print("""1. Use Access Card
                     2. Turn Back
                  """)  
        else:
            print("You need the Access Card from the cave on Orrison to end the Hurston Jump Point!")
        draw()

        choice = input("# ")

        if choice == "1":
            if key2:
                fight = True
                battle()
        elif choice == "2":
            boss2 = False
        
# Trader Function
def trader():
    global buy, quantanium, shield_boost, ship_repair, ATK

    while buy:
        clear()
        draw()
        print("Welcome to the trader!")
        draw()
        print(f"Quantanium: {quantanium}")
        print(f"Shield Boost: {shield_boost}")
        print(f"Ship Repair Kits: {ship_repair}")
        print(f"Weapons Level: {ATK}")
        draw()
        print("""
            What would you like to buy?
              1. Buy Shield Boost: +25HP - 10 Quantanium
              2. Buy Ship Repair Kits: +50HP - 20 Quantanium
              3. Buy Weapons Level: +5ATK - 35 Quantanium
              4. Exit Trader
              """)
        
        choice = input("# ")

        if choice == "1":
            if quantanium >= 10:
                shield_boost += 1
                quantanium -= 10
                print("You've purchased shield boost!")
            else:
                print("You don't have enough quantanium!")
                input("> ")
        elif choice == "2":
            if quantanium >= 20:
                ship_repair += 1
                quantanium -= 10
                print("You've purchased a ship repair kit!")
            else:
                print("You don't have enough quantanium!")
                input("> ")
        elif choice == "3":
            if quantanium >= 35:
                ATK += 5
                quantanium -= 10
                print("You've purchased a weapon upgrade!")
            else:
                print("You don't have enough quantanium!")
                input("> ")
        elif choice == "4":
            buy = False
        else:
            print("Please enter a valid choice!")

# Run Function
clear()
print("Mission Statement......")
draw()
print("""The year is 3033, you are a mining operator for the Lost Corp Mining Org. You mission is to successfully destroy enemy ships and take back the quantanium. 
      """)
while run:
    while menu:
            draw()
            print("""
          1. New Game
          2. Load Game
          3. Rules
          4. Quit Game
        """)
            draw()
            choice = input('What would you like to do? ')
            if choice == "1":
                clear()
                draw()
                name = input("What is your name? ")
                draw()
                menu = False
                play = True
            elif choice == "2":
                try:
                    f = open("load.txt", "r")
                    load_list = f.readlines()
                    if len(load_list) == 10:
                        name = load_list[0][:-1]
                        HP = int(load_list[1][:-1])
                        ATK = int(load_list[2][:-1])
                        shield_boost = int(load_list[3][:-1])
                        ship_repair = int(load_list[4][:-1])
                        quantanium = int(load_list[5][:-1])
                        x = int(load_list[6][:-1])
                        y = int(load_list[7][:-1])
                        key1 = load_list[8][:-1]
                        key2 = load_list[9][:-1]
                        clear()
                        draw()
                        print(f'        Welcome back {name}!')
                        draw()
                        input("> ")
                        menu = False
                        play = True 
                    else:
                        print("Corrupt save file!")
                        input(">")
                except OSError:
                    print("There is no loadable file!")
                    input(">")
            elif choice == "3":   
                rules = True
            elif choice == "4":
                break
            else:
                print('Please enter a valid choice.')

            # Rules Loop
            if rules:
                print("I'm the creator of this game, here are the rules.")
                rules = True
                choice = ""
                input(">")

    # Play Loop
    while play:
        save() # autosave
        clear()

        if not standing:
            if biom[map[y][x]]["enemy"]:
                if random.randint(0,100) < 30:
                    fight = True
                    battle()
        if not standing:
            if map[y][x] == "astroid_field":
                if random.randint(0,100) < 33:
                    astroid_damage = True
                    astroid_field()
    
        if play:
            draw()
            print("LOCATION: " + biom[map[y][x]]["t"])
            draw()
            print("NAME: " + name)
            print("HP: " + str(HP) + "/" + str(HPMAX))
            print("ATK: " + str(ATK))
            print("Shield Boost: " + str(shield_boost))
            print("Ship Repair: " + str(ship_repair))
            print("QUANTANIUM: " + str(quantanium))
            print("COORD: ",x,y)
            draw()
            print("0 - Save and Quit")
            if y > 0:
                print("1 - NORTH")
            if x < x_len:
                print("2 - East")
            if y < y_len:
                print("3 - SOUTH")
            if x > 0:
                print("4 - WEST")
            if shield_boost >= 0:
                print("5 - USE SHIELD BOOST (25HP)")
            if ship_repair >= 0:
                print("6 - USE SHIP REPAIR (50HP)")
            if biom[map[y][x]]["trader"] or map[y][x] == "wreck" or map[y][x] == "cave_orrison" or map[y][x] == "hurston_jump_point":
                print("7 - ENTER")
            draw()

            dest = input("# ")

            if dest == "0":
                play = False
                menu = True
                save()
            elif dest == "1":
                if y > 0:
                    y -= 1
                    standing = False
            elif dest == "2":
                if x < x_len:
                    x += 1
                    standing = False
            elif dest == "3":
                if y < y_len:
                    y += 1
                    standing = False
            elif dest == "4":
                if x > 0:
                    x -= 1
                    standing = False
            elif dest == "5":
                if shield_boost > 0:
                    shield_boost -= 1
                    heal(25)
                else:
                    print("No Med Pens!")
                input("> ")
                standing = True
            elif dest == "6":
                if ship_repair > 0:
                    ship_repair -= 1
                    heal(50)
                else:
                    print("No Oxygen Pens!")
                input("> ")
                standing = True
            elif dest == "7":
                if biom[map[y][x]]["trader"]:
                    buy = True
                    trader()
                if map[y][x] == "wreck":
                    speak = True
                    wreck()
                if map[y][x] == "cave_orrison":
                    boss_1 = True
                    cave_orrison()
                if map[y][x] == "hurston_jump_point":
                    boss_2 = True
                    hurston_jump_point()
            else:
                standing = True

            