#The Legend of Super Python World. A videogame with a story, "open-world" exploration, turn-based combat, boss fights and  dialogue - illustrated using ASCII and Unicode characters. The title is a reference to the classic NES and SNES games The Legend of Zelda and Super Mario World.
#Instructions and controls are given in-game. By Henri K.

#IMPORTANT NOTE: If running in Replit, you may need to use the slider to adjust the screen size to ensure the graphics are displayed correctly.

name = input("Enter your name.")
n = open("name.txt","w")
n.write(name)
n.close()
#Because it has to be retrieved by a module, this sends the player's name to a .txt file at the very start.
import os
os.system('clear')

import superpythonworld as pyworld
from backdrops import scenes_main, scenes_alt, scenes_alt_squared, battle_scenes, bossbattle_scenes

player_input = ''
pyworld.wait(2)
if pyworld.ask_until_valid("""Type 'new' to start a new game, or 'continue' to continue from a save state.\n""","Invalid input.",['new','continue']) == 'new':
  pyworld.print_for_seconds("-New Game-",3)
  pyworld.clear()
  pyworld.wait(1)
  player_input = 'new'
else:
  player_input = input("Please enter your save state code.")
  save_state = player_input.split("-")
#Takes input for whether the player is starting a new game or continuing a previous one.


if player_input == 'new':
  inventory = [5,0,0,0,"","","","","","","","",""]
  boolset = [False,False,False,False,False,False,False,False,False]
  position = level = 0
  #boolset indicator: [shortcut open], [castle open], [guards defeated], [owl talked to], [owl quiz beat], [goblin den 1 beat], [goblin den 2 beat], [goblin den 3 beat], [treasure obtained].

  pyworld.wait(2)

  for i in range (1,4):
    pyworld.dialogue("intro.txt",i,1)
    pyworld.wait(10)

  pyworld.dialogue("intro.txt",4)
  player_input = input()

  if player_input == 'yes':
    pyworld.dialogue("intro.txt",5,1)
    pyworld.wait(4)
    pyworld.clear()
    pyworld.wait(2)
  else:
    pyworld.dialogue("intro.txt",6)
    pyworld.wait(4)
    pyworld.end_game()
#Sets up a new game and does the intro sequence.
else:
  try:
    import re
    inventory = []
    boolset = []
    position = level = 0

    stacks = re.findall("..",save_state[1])
    for i in range(4):
      inventory.append(int(stacks[i]))

    for i in range(3):
      if save_state[2][i] == "n":
        inventory.append("")
      else:
        if i == 0:
          if save_state[2][i] == "w":inventory.append("Wooden Sword")
          if save_state[2][i] == "s":inventory.append("Stone Sword")
          if save_state[2][i] == "i":inventory.append("Iron Sword")
          if save_state[2][i] == "t":inventory.append("Titanium Sword")
        if i == 1:inventory.append("Bow")
        if i == 2:
          if save_state[2][i] == "l":inventory.append("Leather Armour")
          if save_state[2][i] == "i":inventory.append("Iron Armour")

    misc_items = ["Book Of Much Knowledge", "Boat", "Particularly Tall Ladder", "Forest Key", "Lake Key", "Mountain Key"]
    for i in range(6):
      if bool(int(save_state[3][i])):
        inventory.append(misc_items[i])
      else:
        inventory.append("")

    for i in range(9):
      if save_state[4][i] == "t":
        boolset.append(True)
      else:
        boolset.append(False)

    coords = re.findall("...",save_state[5])
    coordpair = []
    
    for i in [0,1]:
      if coords[i][0] == "p": 
        coordpair.append(int(str(coords[i][1])+str(coords[i][2])))

      if coords[i][0] == "n": 
        coordpair.append(-1*int(str(coords[i][1])+str(coords[i][2])))

    position,level = coordpair[0], coordpair[1]

    pyworld.print_for_seconds("Save state successfully loaded.",3)
    pyworld.clear()
    pyworld.wait(2)
  
  except:
    print("Error - Invalid save state. Check your code carefully and try again, otherwise you may load a glitched game instead of getting this message.")
    pyworld.wait(3)
    pyworld.end_game()
#Loads the data encoded in the save state.

entering = True

#---<Shop and Player Inventory>---#

shop_items = "Wooden Sword : $5\nStone Sword : $12\nIron Sword : $18\nTitanium Sword : $30\nBow : $15\nArrow : $4\nBomb : $8\nLeather Armour : $10\nIron Armour : $20\nHealth Potion : $15\nBook Of Much Knowledge : $15\nBoat : $20\nParticularly Tall Ladder : $25"

prices = {"Wooden Sword":(5,1), "Stone Sword":(12,2), "Iron Sword":(18,3), "Titanium Sword":(30,4), "Bow":(15,5), "Arrow":(4,6), "Bomb":(8,7), "Leather Armour":(10,9), "Iron Armour":(20,10), "Health Potion":(15,8), "Book Of Much Knowledge":(15,11), "Boat":(20,12), "Particularly Tall Ladder":(25,13)}
#A dictionary containing every store item with a tuple value indicating its price and the desc.txt file line with its description.

def purchase(item):
  if inventory[0] < prices[item][0]:
    pyworld.dialogue("errors.txt",5)
  else:
    inventory[0] -= prices[item][0]
    print("You got " + item + ".")

    if item[-5:] == "Sword":invslot = 4
    if item[-6:] == "Armour":invslot = 6
    if item == "Bow":invslot = 5
    if item == "Arrow":invslot = 1
    if item == "Bomb":invslot = 2
    if item == "Health Potion":invslot = 3
    if item == "Book Of Much Knowledge":invslot = 7
    if item == "Boat":invslot = 8
    if item == "Particularly Tall Ladder":invslot = 9

    if invslot < 4:
      inventory[invslot] += 1
    else:
      inventory[invslot] = item
#Buys an item.

def inventory_display():
  keywords = ["Gold : ","Arrows : ","Bombs : ","Health Potions : "]
  display = []

  display.append(keywords[0]+str(inventory[0]))

  for i in range (1,4):
    if bool(inventory[i]):display.append(keywords[i]+str(inventory[i]))

  for i in range(4,13):
    if bool(inventory[i]):display.append(inventory[i])

  return display
#Displays the player's inventory in a readable way.

def get_save_state(position,level):
  save_state = ""

  def decimal_form(n):
    if n < 10:
      return ("0"+str(n))
    else:
      return str(n)

  save_state += name
  save_state += "-"
  save_state += str(decimal_form(inventory[0]))

  for i in range (1,4):
    save_state += str(decimal_form(inventory[i]))
  save_state += "-"
  for i in range (4,7):
    if bool(inventory[i]):
      save_state += (inventory[i][0]).lower()
    else:
      save_state += "n"
  save_state += "-"
  for i in range (7,13):
    if bool(inventory[i]):
      save_state += "1"
    else:
      save_state += "0"

  save_state += "-"

  for e in boolset:
    if e:
      save_state += "t"
    else:
      save_state += "f"

  save_state += "-"

  coords = [position,level]

  for coord in coords :
    if coord < 0:
      save_state += "n"
    else:
      save_state += "p"

    save_state += str(decimal_form(abs(coord)))

  return save_state
#Generates a save state code. For it to work, I added the in-game restriction that gold and stackables cannot exceed 99.

def shop_cycle():
  global level

  pyworld.clear()
  print(scenes_alt[-8])

  player_input = input()


  if player_input == 't':
    for i in range(4,8):
      pyworld.dialogue("shopkeeper.txt",i)
      pyworld.wait(5)

  if player_input == 'e':
    pyworld.dialogue("shopkeeper.txt",8,1)
    pyworld.wait(3)
    level += 1
    global entering
    entering = True

  if player_input == 'l':
    print(shop_items)
    player_input = input()

    if player_input == 'r':
      pass
    elif player_input.title() in prices:
      selection = player_input.title()
      pyworld.clear()

      print(scenes_alt[-8])
      print()
      print(selection)
      pyworld.dialogue("desc.txt",prices[selection][1])
      pyworld.wait(2)

      if selection in ["Stone Sword", "Iron Sword", "Titanium Sword", "Leather Armour", "Iron Armour"]:print("[Buying a sword or armour will replace the sword/armour you currently have.]",)

      player_input = input("Type 'p' to purchase, or 'r' to go back.")

      if player_input == 'p':
        if selection in ["Arrow", "Bomb", "Health Potion"]:
          player_input = int(input("How many do you want?"))

          for i in range(player_input):
            purchase(selection)

          pyworld.wait(3)
        else:
          purchase(selection)
          pyworld.wait(3)
      else:
        pass

  if player_input == 'i':
    print(inventory_display())
    player_input = input("▽ ")

  if player_input == 's':
    print("Your save state code is: " + get_save_state(position,level))
    player_input = input("▽ ")
#The game cycle for inside the shop.

#---</Shop and Player Inventory>---#


#---<Goblins and Battle>---#

damageValue = {"":0,"Wooden Sword":3, "Stone Sword":5, "Iron Sword":8, "Titanium Sword":12, "Bow and Arrow":10, "Bomb":4}

player_hp = 20
player_atk = damageValue[inventory[4]]
player_def = 1
weapon = inventory[4]

def battle_init():
  global player_hp, player_atk, player_def

  player_hp = 20

  if "Iron Armour" in inventory:
    player_def = 0.6
  elif "Leather Armour" in inventory:
    player_def = 0.8
  else:
    player_def = 1
#Initializes the player's battle statistics based on the combat gear in their inventory.
goblinPreset = [["Peon"],["Thief"],["Brute"],["Archer"],["Bomber"]]

goblinDuoPresets1 = [["Peon","Thief"],["Peon","Brute"],["Archer","Archer"]]
goblinDuoPresets2 = [["Peon","Thief"],["Peon","Brute"],["Brute","Archer"],["Archer","Archer"],["Bomber","Bomber"],["Thief","Bomber"],] 
goblinDuoPresets3 = [["Peon","Thief"],["Peon","Brute"],["Brute","Archer"],["Archer","Archer"],["Bomber","Bomber"],["Thief","Bomber"],["Brute","Brute"], ["Brute","Thief"], ["Thief","Thief"], ["Peon","Brawler"], ["Brute","Brawler"], ["Brawler","Archer"]] 

goblinTrioPresets1 = [["Peon","Peon","Peon"],["Peon","Archer","Bomber"],["Peon","Peon","Brute"]]
goblinTrioPresets2 = [["Peon","Peon","Peon"],["Peon","Archer","Bomber"],["Peon","Peon","Brute"], ["Brute", "Archer", "Archer"], ["Brute","Thief","Thief"],["Peon","Thief","Bomber"]]
goblinTrioPresets3 = [["Peon","Peon","Peon"], ["Peon","Archer","Bomber"], ["Peon","Peon","Brute"], ["Brute", "Archer", "Archer"], ["Brute","Thief","Thief"], ["Peon","Thief","Bomber"], ["Archer","Bomber","Archer"], ["Brute","Brute","Peon"], ["Thief","Thief","Thief"], ["Peon","Brute","Brawler"], ["Archer","Brawler","Archer"], ["Peon","Bomber","Brawler"], ["Thief","Thief","Brawler"],["Archer","Bomber","Brawler"]]
#The many presets for goblin encounter spawns.

class Goblin: 
  def __init__(self, div, hp, atk, atkName, title):
    self.div = div
    self.hp = hp
    self.atk = atk
    self.atkName = atkName
    self.title = title
  
  def attack(self):
    if bool(self.hp):
      global player_hp
      player_hp -= int(round(self.atk*player_def))
      if player_hp <= 0: player_hp = 0
  
  def get_attacked(self):
    if bool(self.hp):
      global player_atk
      self.hp -= (player_atk)
      if self.hp <= 0: self.hp = 0

  def generatedrops(self):
    if self.div == "Peon":
      g = [1,2]
      drops = pyworld.pickRandom(g), 0, 0
    if self.div == "Thief":
      g = [5,6]
      drops = pyworld.pickRandom(g), 0, 0
    if self.div == "Brute":
      g = [3,4]
      drops = pyworld.pickRandom(g), 0, 0
    if self.div == "Archer":
      g = [3,4]
      if pyworld.percentChance(80):
        drops = pyworld.pickRandom(g), 1, 0
      else:
        drops = pyworld.pickRandom(g), 2, 0
    if self.div == "Bomber":
      g = [4,5]
      if pyworld.percentChance(80):
        drops = pyworld.pickRandom(g), 0, 1
      else:
        drops = pyworld.pickRandom(g), 0, 2
    if self.div == "Brawler":
      g = [5,6]
      drops = pyworld.pickRandom(g), 0, 0
    if self.div == "Guard":
      g = [7,8]
      drops = pyworld.pickRandom(g), 0, 0

    global inventory
    inventory[0] += drops[0]

    if drops[2] != 0:
      inventory[2] += drops[2]
      print("You got " + str(drops[0]) + " gold and " + str(drops[2]) + " bombs.")
    elif drops[1] != 0:
      inventory[1] += drops[1]
      print("You got " + str(drops[0]) + " gold and " + str(drops[1]) + " arrows.")
    else:
      print("You got " + str(drops[0]) + " gold.")

    pyworld.wait(1)
    
  #Returns a tuple of drops, of the form (gold, arrows, bombs).
#This is the goblin class: Its properties are division (what type it is, determining most of its other properties), hp (health points remaining), atk (attack damage), atkName (the name of its attack), and title (The wording that appears under it in-game). The attack and get_attacked methods are self-explanatory.

class Boss(Goblin):
  def __init__(self, div, hp, atk, atkmultiplier, dfs, moveset, selectedMove, selectedMoveType, halfHealth, abilityUsed):
    self.div = div
    self.hp = hp
    self.atk = atk
    self.atkmultiplier = atkmultiplier
    self.dfs = dfs
    self.moveset = moveset
    self.selectedMove = selectedMove
    self.selectedMoveType = selectedMoveType
    self.halfHealth = halfHealth
    self.abilityUsed = abilityUsed

  def attack(self):
    if bool(self.hp):
      global player_hp
      player_hp -= int(round(self.atk*self.atkmultiplier*player_def))
      if player_hp <= 0: player_hp = 0

  def get_attacked(self):
    if bool(self.hp):
      global player_atk
      self.hp -= int(round(player_atk*self.dfs))
      if self.hp <= 0: self.hp = 0
  #The attack and aattacked methods are slightly different for bosses, as they have defense and attack multipliers.
  def selectMove(self):
    

    if self.hp > self.halfHealth:
      if pyworld.percentChance(50):
        self.selectedMove = self.moveset[0]
      else:
        self.selectedMove = self.moveset[1]
    else:
      if pyworld.percentChance(50):
        self.selectedMove = self.moveset[2]
      else:
        if pyworld.percentChance(50):
          self.selectedMove = self.moveset[0]
        else:
          self.selectedMove = self.moveset[1]

    if self.selectedMove == "Magic Shot":
      self.atk = 5
    elif self.selectedMove == "Flame Shot":
      self.atk = 6
    elif self.selectedMove == "Cannonball":
      self.atk = 6
    elif self.selectedMove == "Double Cannonball":
      self.atk = 12
    elif self.selectedMove == "Stab":
      self.atk = 9
    elif self.selectedMove == "Armour Tear":
      self.atk = 3
    elif self.selectedMove == "Sceptre Strike":
      self.atk = 10
    elif self.selectedMove == "Lifesteal":
      self.atk = 8
    else:
      self.atk = 0

    if self.selectedMove in ["Heal","Anchor","Imbue","Seizure"]:
      self.selectedMoveType = "b"
    else:
      self.selectedMoveType = "a"

  #Picks a move to use.

  def Effect(self):
    if self.selectedMove == "Flame Shot":
      global inventory
      import math
      inventory[1] *= 1/2
      inventory[1] = math.floor(inventory[1])
      pyworld.dialogue("battle.txt",15)
    elif self.selectedMove == "Heal":
      self.hp += 7
      if not self.abilityUsed:
        pyworld.dialogue("boss.txt",3)
        self.abilityUsed = True
    elif self.selectedMove == "Anchor":
      self.dfs -= 0.1
      if not self.abilityUsed:
        pyworld.dialogue("boss.txt",7)
        self.abilityUsed = True
    elif self.selectedMove == "Armour Tear":
      global player_def
      player_def += 0.1
      pyworld.dialogue("battle.txt",16)
    elif self.selectedMove == "Imbue":
      self.atkmultiplier *= 1.25
      if not self.abilityUsed:
        pyworld.dialogue("boss.txt",13)
        self.abilityUsed = True
    elif self.selectedMove == "Lifesteal":
      self.hp += int(8*player_def)
    elif self.selectedMove == "Seizure":
      
      i = pyworld.pickRandom([1,2,3,4])
      inventory[i-1] = 0
      pyworld.dialogue("battle.txt",(16+i))
      #In the real program, use i to access inventory slots.
    else:
      pass

  def generatedrops(self):
    key_key = {"Sorcerer":"Forest Key", "Cannoneer":"Lake Key", "Swordfighter":"Mountain Key", "King":"the Goblin King has been defeated"}
    global inventory
    
    if key_key[self.div] == "Forest Key":slot=10
    elif key_key[self.div] == "Lake Key":slot=11
    elif key_key[self.div] == "Mountain Key":slot=12
    else:slot=0

    inventory[0] += 10
    if bool(slot):inventory[slot] = key_key[self.div]
    print("You got 10 gold and " + key_key[self.div] + "!")
    pyworld.wait(1)
    print("▽ ")
  #Applies the additional effects.
#This is the boss subclass of goblins, which have in addition to higher stats, a list of multiple attacks/moves to choose from. 
    
def spawn_goblin1(type):
  if type == "Peon":
    h,a,n = 8,3,"Punch"
  if type == "Thief":
    h,a,n = 6,4,"Dagger Strike"
  if type == "Brute":
    h,a,n = 10,4,"Club"
  if type == "Archer":
    h,a,n = 6,4,"Arrow Shot"
  if type == "Bomber":
    h,a,n = 6,6,"Bomb"
  if type == "Brawler":
    h,a,n = 14,7,"Gloved Punch"
  if type == "Guard":
    h,a,n = 18,5,"Spear Strike"

  global goblin1
  goblin1 = Goblin(type,h,a,n,type)  
def spawn_goblin2(type):
  if type == "Peon":
    h,a,n = 8,3,"Punch"
  if type == "Thief":
    h,a,n = 6,4,"Dagger Strike"
  if type == "Brute":
    h,a,n = 10,4,"Club"
  if type == "Archer":
    h,a,n = 6,4,"Arrow Shot"
  if type == "Bomber":
    h,a,n = 6,6,"Bomb"
  if type == "Brawler":
    h,a,n = 14,7,"Gloved Punch"
  if type == "Guard":
    h,a,n = 18,5,"Spear Strike"

  global goblin2
  goblin2 = Goblin(type,h,a,n,type) 
def spawn_goblin3(type):

  if type == "Peon":
    h,a,n = 8,3,"Punch"
  if type == "Thief":
    h,a,n = 6,4,"Dagger Strike"
  if type == "Brute":
    h,a,n = 10,4,"Club"
  if type == "Archer":
    h,a,n = 6,4,"Arrow Shot"
  if type == "Bomber":
    h,a,n = 6,6,"Bomb"
  if type == "Brawler":
    h,a,n = 14,7,"Gloved Punch"
  if type == "Guard":
    h,a,n = 18,5,"Spear Strike"

  global goblin3
  goblin3 = Goblin(type,h,a,n,type) 
def spawn_boss(type):
  if type == "Sorcerer":
    h,d = 30,1
    ms = ["Magic Shot","Flame Shot","Heal"]
  if type == "Cannoneer":
    h,d = 45,1
    ms = ["Cannonball","Double Cannonball","Anchor"]
  if type == "Swordfighter":
    h,d = 60,0.8
    ms = ["Stab","Armour Tear","Imbue"]
  if type == "King":
    h,d = 70,0.8
    ms = ["Sceptre Strike","Lifesteal","Seizure"]
  
  global boss
  boss = Boss(type,h,0,1,d,ms,ms[0],"a",h/2,False)
#Spawns a goblin in the position. The types are "Peon", "Thief", "Brute", "Archer", "Bomber", and "Guard".
def render_title_1(t1):
  s = ""
  s += "Goblin"
  s += "\n"
  for i in range (44):
    s += " "
  s += t1
  return s
def render_title_2(t1, t2):
  s = ""
  s += "Goblin   Goblin"
  s += "\n"
  for i in range (43):
    s += " "
  s += t1
  s += "   "
  s += t2
  return s
def render_title_3(t1, t2, t3):
  s = ""
  s += "Goblin   Goblin   Goblin"
  s += "\n"
  for i in range (35):
    s += " "
  s += t1
  s += "   "
  s += t2
  s += "    "
  s += t3
  return s
#Gets the goblin title set to render.
def display_battle_1():
  pyworld.clear()

  if bool(goblin1.hp):
    disp_g1 = goblin1.hp
  else:
    disp_g1 = "-"

  print (battle_scenes[1].format(player_hp,disp_g1,render_title_1(goblin1.title)))
def display_battle_2():
  pyworld.clear()

  if bool(goblin1.hp):
    disp_g1 = goblin1.hp
  else:
    disp_g1 = "-"
  if bool(goblin2.hp):
    disp_g2 = goblin2.hp
  else:
    disp_g2 = "-"
  print (battle_scenes[2].format(player_hp,disp_g1,disp_g2,render_title_2(goblin1.title, goblin2.title)))
def display_battle_3():
  pyworld.clear()

  if bool(goblin1.hp):
    disp_g1 = goblin1.hp
  else:
    disp_g1 = "-"
  if bool(goblin2.hp):
    disp_g2 = goblin2.hp
  else:
    disp_g2 = "-"
  if bool(goblin3.hp):
    disp_g3 = goblin3.hp
  else:
    disp_g3 = "-"

  print (battle_scenes[3].format(player_hp,disp_g1,disp_g2,disp_g3,render_title_3(goblin1.title,goblin2.title,goblin3.title)))
def display_bossbattle(super="a"):
  pyworld.clear()
  if super=="a":
    if boss.div == "Sorcerer":
      print(bossbattle_scenes[1].format(boss.hp, player_hp))
    if boss.div == "Cannoneer":
      print(bossbattle_scenes[3].format(player_hp,boss.hp))
    if boss.div == "Swordfighter":
      print(bossbattle_scenes[5].format(player_hp,boss.hp))
    if boss.div == "King":
      print(bossbattle_scenes[7].format(player_hp,boss.hp))
  else:
    if boss.div == "Sorcerer":
      print(bossbattle_scenes[2].format(boss.hp, player_hp))
    if boss.div == "Cannoneer":
      print(bossbattle_scenes[4].format(player_hp,boss.hp))
    if boss.div == "Swordfighter":
      print(bossbattle_scenes[6].format(player_hp,boss.hp))
    if boss.div == "King":
      print(bossbattle_scenes[8].format(player_hp,boss.hp))
#Displays the updated battleground.

def selectWeapon(w):
  
  global weapon, player_atk, player_hp, inventory

  if w == "s" : 
    weapon = inventory[4]
    
  elif w == "b": 
    weapon = "Bow and Arrow"
    inventory[1] -= 1
    
  elif w == "d": 
    weapon = "Bomb"
    inventory[2] -= 1

  elif w == "h": 
    inventory[3] -= 1
    player_hp = 20
  player_atk = damageValue[weapon]
def invalidSelection(w):
  global inventory

  if not w in ["s","b","d","h"]:
    return True
  elif (w == "b" and (inventory[1] == 0 or (not "Bow" in inventory))) or (w == "d" and inventory[2] == 0) or (w == "h" and inventory[3] == 0):
    return True
  else:
    return False 
#Selects a weapon to use. If you enter something invalid, the second function is called.

prev_battle_result = 0
#Stores a binary digit representing whether you won or lost the previous battle, for use in the game loop.

def battle_cycle_1():
  while True:
    global inventory,prev_battle_result

    pyworld.dialogue("battle.txt",3)
    pyworld.wait(1)
    pyworld.dialogue("battle.txt",4)
    if inventory[1] != 0 and "Bow" in inventory: pyworld.dialogue("battle.txt",5)
    if inventory[2] != 0: pyworld.dialogue("battle.txt",6)
    if inventory[3] != 0: pyworld.dialogue("battle.txt",7)
    w = input()
    if invalidSelection(w): w = "s" 
    selectWeapon(w)

    if w != "h":
      goblin1.get_attacked()

    display_battle_1()
    if w != "h":
      pyworld.dialogue("battle.txt",1,0,0,1,weapon,("Goblin " + goblin1.title),player_atk)
    pyworld.wait(3)

    if not(bool(goblin1.hp)):
      pyworld.dialogue("battle.txt",12)
      pyworld.wait(1)
      goblin1.generatedrops()
      print("▽ ")
      pyworld.wait(4)
      prev_battle_result = 1
      break

    goblin1.attack()
    display_battle_1()
    pyworld.dialogue("battle.txt",2,0,0,1,("Goblin " + goblin1.title),goblin1.atkName,int(round(goblin1.atk*player_def)))
    pyworld.wait(2)

    if not(bool(player_hp)):
      pyworld.dialogue("battle.txt",13)
      pyworld.wait(1)
      inventory[0] = int(inventory[0]*0.5)
      pyworld.dialogue("battle.txt",21)
      pyworld.wait(4)
      prev_battle_result = 0
      break

    display_battle_1()
def battle_cycle_2():
  while True:
    global inventory,prev_battle_result

    pyworld.dialogue("battle.txt",3)
    pyworld.wait(1)
    pyworld.dialogue("battle.txt",4)
    if inventory[1] != 0 and "Bow" in inventory: pyworld.dialogue("battle.txt",5)
    if inventory[2] != 0: pyworld.dialogue("battle.txt",6)
    if inventory[3] != 0: pyworld.dialogue("battle.txt",7)
    w = input()
    if invalidSelection(w): w = "s"
    selectWeapon(w)
    if w != "h" and w != "d":
      pyworld.dialogue("battle.txt",8)
      pyworld.wait(1)
      if bool(goblin1.hp):pyworld.dialogue("battle.txt",9)
      if bool(goblin2.hp):pyworld.dialogue("battle.txt",10)
      i = input()

    if w == "d":
      goblin1.get_attacked()
      goblin2.get_attacked()
      display_battle_2()
      group = "Goblin " + goblin1.title + " and " + "Goblin " + goblin2.title
      pyworld.dialogue("battle.txt",1,0,0,1,weapon,group,player_atk)
    else:
      if i == "1" : 
        if w != "h":goblin1.get_attacked()
        display_battle_2()
        if w != "h":pyworld.dialogue("battle.txt",1,0,0,1,weapon,("Goblin " + goblin1.title),player_atk)
      if i == "2" : 
        if w != "h":goblin2.get_attacked()
        display_battle_2()
        if w != "h":pyworld.dialogue("battle.txt",1,0,0,1,weapon,("Goblin " + goblin2.title),player_atk)
    pyworld.wait(3)

    if not(bool(goblin1.hp)) and not(bool(goblin2.hp)):
      pyworld.dialogue("battle.txt",12)
      pyworld.wait(1)
      goblin1.generatedrops()
      goblin2.generatedrops()
      print("▽ ")
      pyworld.wait(4)
      prev_battle_result = 1
      break

    goblin1.attack()
    display_battle_2()
    if bool(goblin1.hp):
      pyworld.dialogue("battle.txt",2,0,0,1,("Goblin " + goblin1.title),goblin1.atkName,int(round(goblin1.atk*player_def)))
      pyworld.wait(2)

    goblin2.attack()
    display_battle_2()
    if bool(goblin2.hp):
      pyworld.dialogue("battle.txt",2,0,0,1,("Goblin " + goblin2.title),goblin2.atkName,int(round(goblin2.atk*player_def)))
      pyworld.wait(2)

    if not(bool(player_hp)):
      pyworld.dialogue("battle.txt",13)
      pyworld.wait(1)
      inventory[0] = int(inventory[0]*0.5)
      pyworld.dialogue("battle.txt",21)
      pyworld.wait(4)
      prev_battle_result = 0
      break

    display_battle_2()
def battle_cycle_3():
  while True:
    global inventory,prev_battle_result

    pyworld.dialogue("battle.txt",3)
    pyworld.wait(1)
    pyworld.dialogue("battle.txt",4)
    if inventory[1] != 0 and "Bow" in inventory: pyworld.dialogue("battle.txt",5)
    if inventory[2] != 0: pyworld.dialogue("battle.txt",6)
    if inventory[3] != 0: pyworld.dialogue("battle.txt",7)
    w = input()
    if invalidSelection(w): w = "s"
    selectWeapon(w)
    if w != "h" and w != "d":
      pyworld.dialogue("battle.txt",8)
      pyworld.wait(1)
      if bool(goblin1.hp): pyworld.dialogue("battle.txt",9)
      if bool(goblin2.hp): pyworld.dialogue("battle.txt",10)
      if bool(goblin3.hp): pyworld.dialogue("battle.txt",11)
      i = input()

    if w == "d":
      goblin1.get_attacked()
      goblin2.get_attacked()
      goblin3.get_attacked()
      display_battle_3()
      group = "Goblin " + goblin1.title + " and " + "Goblin " + goblin2.title + " and " + "Goblin " + goblin3.title
      pyworld.dialogue("battle.txt",1,0,0,1,weapon,group,player_atk)
    else:
      if i == "1" : 
        if w != "h":goblin1.get_attacked()
        display_battle_3()
        if w != "h":pyworld.dialogue("battle.txt",1,0,0,1,weapon,("Goblin " + goblin1.title),player_atk)
      if i == "2" : 
        if w != "h":goblin2.get_attacked()
        display_battle_3()
        if w != "h":pyworld.dialogue("battle.txt",1,0,0,1,weapon,("Goblin " + goblin2.title),player_atk)
      if i == "3" : 
        if w != "h":goblin3.get_attacked()
        display_battle_3()
        if w != "h":pyworld.dialogue("battle.txt",1,0,0,1,weapon,("Goblin " + goblin3.title),player_atk)
    pyworld.wait(3)

    if not(bool(goblin1.hp)) and not(bool(goblin2.hp)) and not(bool(goblin3.hp)):
      pyworld.dialogue("battle.txt",12)
      pyworld.wait(1)
      goblin1.generatedrops()
      goblin2.generatedrops()
      goblin3.generatedrops()
      print("▽ ")
      pyworld.wait(4)
      prev_battle_result = 1
      break
    
    goblin1.attack()
    display_battle_3()
    if bool(goblin1.hp):
      pyworld.dialogue("battle.txt",2,0,0,1,("Goblin " + goblin1.title),goblin1.atkName,int(round(goblin1.atk*player_def)))
      pyworld.wait(2)

    goblin2.attack()
    display_battle_3()
    if bool(goblin2.hp):
      pyworld.dialogue("battle.txt",2,0,0,1,("Goblin " + goblin2.title),goblin2.atkName,int(round(goblin2.atk*player_def)))
      pyworld.wait(2)

    goblin3.attack()
    display_battle_3()
    if bool(goblin3.hp):
      pyworld.dialogue("battle.txt",2,0,0,1,("Goblin " + goblin3.title),goblin3.atkName,int(round(goblin3.atk*player_def)))
      pyworld.wait(2)

    if not(bool(player_hp)):
      pyworld.dialogue("battle.txt",13)
      pyworld.wait(1)
      inventory[0] = int(inventory[0]*0.5)
      pyworld.dialogue("battle.txt",21)
      pyworld.wait(4)
      prev_battle_result = 0
      break

    display_battle_3()
def bossbattle_cycle():
  while True:
    global inventory, position,level

    pyworld.dialogue("battle.txt",3)
    pyworld.wait(1)
    pyworld.dialogue("battle.txt",4)
    if inventory[1] != 0 and "Bow" in inventory: pyworld.dialogue("battle.txt",5)
    if inventory[2] != 0: pyworld.dialogue("battle.txt",6)
    if inventory[3] != 0: pyworld.dialogue("battle.txt",7)
    w = input()
    if invalidSelection(w): w = "s" 
    selectWeapon(w)

    if w != "h":
      boss.get_attacked()

    display_bossbattle()
    if w != "h":
      pyworld.dialogue("battle.txt",1,0,0,1,weapon,("Goblin " + boss.div),str(int(round(player_atk*boss.dfs))))
    pyworld.wait(3)

    if not(bool(boss.hp)):
      if boss.div == "Sorcerer":
        respawn_location = (-16,0)
        pyworld.dialogue("boss.txt",4)
        pyworld.wait(3)
      if boss.div == "Cannoneer":
        respawn_location = (14,0)
        pyworld.dialogue("boss.txt",8)
        pyworld.wait(3)
      if boss.div == "Swordfighter":
        respawn_location = (5,0)
        pyworld.dialogue("boss.txt",14,1)
        pyworld.wait(3)
      if boss.div == "King":
        respawn_location = (0,-1)
        pyworld.dialogue("boss.txt",17)
        pyworld.wait(3)

      pyworld.dialogue("battle.txt",12)
      pyworld.wait(2)
      boss.generatedrops()
      pyworld.wait(4)
      position,level = respawn_location[0], respawn_location[1]

      if boss.div == "King":
        pyworld.clear()
        for i in range(1,4):
          pyworld.dialogue("outro.txt",i,1)
          pyworld.wait(4)
        pyworld.end_game()

      break

    boss.selectMove()
    boss.attack()
    display_bossbattle(boss.selectedMoveType)
    if boss.selectedMoveType == "a":
      pyworld.dialogue("battle.txt",2,0,0,1,("Goblin " + boss.div),boss.selectedMove,str(int(round(boss.atk*boss.atkmultiplier*player_def))))

      if boss.selectedMove == "Lifesteal":
        pyworld.wait(1)
        pyworld.dialogue("battle.txt",23,0,1,0,"Goblin King",str(int(8*player_def)))
    elif boss.selectedMoveType == "b":
      pyworld.dialogue("battle.txt",14,0,1,0,("Goblin " + boss.div),boss.selectedMove)
    pyworld.wait(2)
    boss.Effect()
    pyworld.wait(2)

    if not(bool(player_hp)):
      pyworld.dialogue("battle.txt",13)
      pyworld.wait(1)
      inventory[0] = int(inventory[0]*0.5)
      pyworld.dialogue("battle.txt",22)
      pyworld.wait(4)

      if boss.div == "Sorcerer":
        respawn_location = (-16,0)
      if boss.div == "Cannoneer":
        respawn_location = (14,0)
      if boss.div == "Swordfighter":
        respawn_location = (5,0)
      if boss.div == "King":
        respawn_location = (0,-1)

      position,level = respawn_location[0], respawn_location[1]
      break

    display_bossbattle()
#Initializes the proper player stats before a battle commences.

#---</Goblins and Battle>---#

#---<Game Main Section>---#

controlslist = """Walk left - '<'\nWalk right - '>'\nEnter or exit through door - 'e'\nUse certain pathways when prompted -'u'\nTalk - 't'\nDisplay inventory - 'i'\nGet save state code - 's'\nOpen treasure chest - 'o'\nRead book - 'b'\nView shop items - 'l'\nSelect shop item - '[item name]'\nHint/Help - '?'\nControls - '!'\n(Other specific controls will be prompted)\n(Some controls are unavailable for indoor areas)"""

blurblocations = {-16:13, -15:0, -14:0, -13:15, -12:2, -11:1, -10: 0, -9:0, -8:0, -7:0, -6:3, -5:0, -4:4, -3:0, -2:0, -1:0, 0:0, 1:0, 2:0, 3:0, 4:5, 5:7, 6:0, 7:0, 8:0, 9:0, 10:0, 11:9, 12:0, 13:0, 14:13, 15:0, 16:0}
blurblocations_alt = {-16:0, -15:0, -14:0, -13:0, -12:0, -11:0, -10: 0, -9:0, -8:0, -7:0, -6:3, -5:0, -4:0, -3:0, -2:0, -1:0, 0:10, 1:0, 2:0, 3:0, 4:6, 5:0, 6:0, 7:0, 8:0, 9:0, 10:14, 11:0, 12:0, 13:0, 14:0, 15:0, 16:0}
blurblocations_alt_squared = {-16:0, -15:0, -14:0, -13:0, -12:0, -11:11, -10: 0, -9:0, -8:0, -7:0, -6:3, -5:0, -4:12, -3:0, -2:0, -1:0, 0:0, 1:0, 2:0, 3:0, 4:0, 5:8, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0, 14:0, 15:0, 16:0}
#Some dictionaries designating which in-game hint "blurbs" are associated with each map location.
def display_scene():
  pyworld.clear()
  global level
  if level == 0: print(scenes_main[position])
  if level == -1: print(scenes_alt[position])
  if level == 1: print(scenes_alt_squared[position])
#Displays the current scene to the "screen".

def left_wall():
  if (position,level) in [(-16,0),(-16,-1),(-8,-1),(-4,-1),(4,-1),(-11,1),(-11,-1),(14,-1),(5,1)] or (position == -13 and not boolset[4]):
    return True
  else: 
    return False

def right_wall():
  if (position,level) in [(16,0),(10,-1),(-4,1),(0,-1),(-8,-1),(-11,-1),(-14,-1)] or (position == 11 and not "Boat" in inventory):
    return True
  else:
    return False

def at_door():
  if position in [14,4,-8,-11,-16] or (position == -4 and boolset[1]):
    return True
  else:
    return False

def at_lvlplusonespot():
  if (position == -11 and boolset[0]) or (position == -4 and boolset[0]) or (position == 5 and "Particularly Tall Ladder" in inventory):
    return True
  else:
    return False

def boss_defeated():
  if (position == -16 and  "Forest Key" in inventory) or (position == 14 and  "Lake Key" in inventory) or (position == 5 and  "Mountain Key" in inventory):
    return True
  else:
    return False
#Some functions returning booleans for whether or not you can do a certain movement/action in-game.

def goblin_encounter(txt,line,group):
  pyworld.dialogue(txt,line)
  pyworld.wait(4)
  battle_init()

  input("▽ ")

  if len(group) == 1:
    spawn_goblin1(group[0])
    display_battle_1()
    battle_cycle_1()

  if len(group) == 2:
    spawn_goblin1(group[0])
    spawn_goblin2(group[1])
    display_battle_2()
    battle_cycle_2()

  if len(group) == 3:
    spawn_goblin1(group[0])
    spawn_goblin2(group[1])
    spawn_goblin3(group[2])
    display_battle_3()
    battle_cycle_3()
#Executes up a random or scripted goblin encounter.

def game_cycle():
    global position,level

    if ("Forest Key" in inventory and "Lake Key" in inventory and "Mountain Key" in inventory) and not (boolset[1]):boolset[1]=True

    player_input = input()

    if player_input == '>': 
      if right_wall():
        if position == 11 and not "Boat" in inventory:
          pyworld.dialogue("errors.txt",6)
          pyworld.wait(1)
        else:
          pyworld.dialogue("errors.txt",2)
          pyworld.wait(1)
      else:
        position += 1

    if player_input == '<': 
      if left_wall():
        if position == -13 and not boolset[4]:
          pyworld.dialogue("owl.txt",3)
          pyworld.wait(1)
        else:
          pyworld.dialogue("errors.txt",1)
          pyworld.wait(1)
      else:
        position -= 1

    if player_input == 'e': 
      if at_door() and (not boss_defeated()) and (not (position == 4 and (not bool(inventory[4])))):
        if level == 0:
          level = -1
        elif level == -1:
          level = 0
      elif (position,level) == (0,-1):
        level = 1
      else:
        if position == -4:
          pyworld.dialogue("errors.txt",4)
          pyworld.wait(1)
        elif boss_defeated():
          pyworld.dialogue("errors.txt",7)
          pyworld.wait(1)
        elif position == 4 and (not bool(inventory[4])):
          pyworld.dialogue("errors.txt",8)
          pyworld.wait(3)
        else:
          pyworld.dialogue("errors.txt",3)
          pyworld.wait(1)

    if player_input == 'u' and at_lvlplusonespot() and (not boss_defeated()): 
      if level == 0 or level == -1:
        level = 1
      elif level == 1:
        if position == -11 or position == -4:
          level = -1
        else:
          level = 0
      
    if player_input == 'i':
      print(inventory_display())
      if "Book Of Much Knowledge" in inventory:
        pyworld.dialogue("game.txt",3)
      player_input = input("▽ ")

    if player_input == 's':
      print("Your save state code is: " + get_save_state(position,level))
      player_input = input("▽ ")

    if player_input == 'o' and (position,level) == (10,-1) and not boolset[8]:
      boolset[8] = True
      inventory[0] += 25
      pyworld.print_for_seconds("You got 25 gold.",4)

    if player_input == 'b' and "Book Of Much Knowledge" in inventory:
      player_input = pyworld.ask_until_valid("There are 10 pages. Type in a page number to read.","Invalid Page Number.",range(1,11),1)

      pyworld.dialogue("book.txt",player_input)
      pyworld.wait(6)

    if player_input == 'debug':
      print("position and level:")
      print(position,level)
      print("boolset:")
      print(boolset)
      print("inventory:")
      print(inventory)
      player_input = input("▽ ")

    if player_input == '?':
      if level == 1:
        if bool(blurblocations_alt_squared[position]):
          pyworld.dialogue("blurbs.txt",blurblocations_alt_squared[position])
        else:
          pyworld.dialogue("game.txt",2)
      if level == 0:
        if bool(blurblocations[position]):
          pyworld.dialogue("blurbs.txt",blurblocations[position])
        else:
          pyworld.dialogue("game.txt",2)
      if level == -1:
        if bool(blurblocations_alt[position]):
          pyworld.dialogue("blurbs.txt",blurblocations_alt[position])
        else:
          pyworld.dialogue("game.txt",2)

      player_input = input("▽ ")

    if player_input == '!':
      print(controlslist)
      player_input = input("▽ ")

    
    display_scene()
        

#The cycle which loops in the main game, with the exception of locations where you talk to people or animals. Those loops have their own dialogue tree loops.


def owlspot_cycle():
  global position
  player_input = input()

  if player_input == '>':position += 1
  if player_input == '<':
    if boolset[4]:
      position -= 1
    else:
      pyworld.dialogue("owl.txt",3)
      pyworld.wait(3)

  if player_input == 'i':
      print(inventory_display())
      player_input = input("▽ ")

  if player_input == 's':
      print("Your save state code is: " + get_save_state(position,level))
      player_input = input("▽ ")

  if player_input == '?':
      if level == 1:
        if bool(blurblocations_alt_squared[position]):
          pyworld.dialogue("blurbs.txt",blurblocations_alt_squared[position])
        else:
          pyworld.dialogue("game.txt",2)
      if level == 0:
        if bool(blurblocations[position]):
          pyworld.dialogue("blurbs.txt",blurblocations[position])
        else:
          pyworld.dialogue("game.txt",2)
      if level == -1:
        if bool(blurblocations_alt[position]):
          pyworld.dialogue("blurbs.txt",blurblocations_alt[position])
        else:
          pyworld.dialogue("game.txt",2)

      player_input = input("▽ ")

  if player_input == 't':
    if boolset[4]:
      pyworld.dialogue("owl.txt",12)
      pyworld.wait(3)
      
    else:

      if boolset[3]:
        pyworld.dialogue("owl.txt",2)
      else:
        pyworld.dialogue("owl.txt",1)
        
        boolset[3] = True

      player_input = input()

      if player_input == 'n':
        pyworld.dialogue("owl.txt",5)
        pyworld.wait(2)
      elif player_input == 'y':
        pyworld.dialogue("owl.txt",4)
        pyworld.wait(2)

        quizdict = {1:["delta"],2:["lake", "a lake"],3:["stan"]}
        for i in range (1,4):
          pyworld.clear()
          display_scene()

          pyworld.dialogue("owl.txt",(i+5))
          pyworld.wait(1)

          player_input = input()

          if player_input.lower() in quizdict[i]:
            pyworld.dialogue("owl.txt",9)
            pyworld.wait(2)

            if i == 3:
              pyworld.dialogue("owl.txt",12)
              pyworld.wait(8)
              
              boolset[4] = True
              
          else:
            pyworld.dialogue("owl.txt",10)
            pyworld.wait(2)
            pyworld.dialogue("owl.txt",11,1)
            pyworld.wait(6)
            break

          
  display_scene()
#The cycle for the forest owl's quiz.

def shortcutspot_cycle():
  global level
  player_input = input()

  if player_input == '<':
    pyworld.dialogue("errors.txt",1)
  if player_input == '>':
    pyworld.dialogue("errors.txt",2)
  if player_input == 'e':
    level += 1
    global entering
    entering = True

  if player_input == 'u' and at_lvlplusonespot() and (not boss_defeated()): 
      if level == 0 or level == -1:
        level = 1
      elif level == 1:
        if position == -11 or position == -4:
          level = -1
        else:
          level = 0

  if player_input == 'i':
      print(inventory_display())
      player_input = input("▽ ")

  if player_input == 's':
      print("Your save state code is: " + get_save_state(position,level))
      player_input = input("▽ ")

  if player_input == 't':
    if boolset[0]:
      pyworld.dialogue("shortcutguy.txt",9)
      pyworld.wait(2)
    else:
      for i in range (2,6):
        pyworld.dialogue("shortcutguy.txt",i)
        pyworld.wait(4)

  if player_input == 'a':
    pyworld.dialogue("shortcutguy.txt",6)
    player_input = input()

    if player_input == 'y':
      global inventory
      if inventory[0] >= 99:
        inventory[0] -= 99
        boolset[0] = True
        pyworld.dialogue("shortcutguy.txt",8)
        pyworld.wait(2)
        pyworld.dialogue("shortcutguy.txt",10)
        pyworld.wait(6)
      else:
        pyworld.dialogue("shortcutguy.txt",7,1)
        pyworld.wait(4)
#The cycle for the house of the guy who owns the shortcut.
  
#---</Game Main Section>---#

#---<Game-Operating Loop>---#

display_scene()
if player_input == 'yes':
  pyworld.dialogue("game.txt",1)
  game_cycle()
#Displays the game's introductory prompt and controls if starting a new game.

while True:
  display_scene()
  #Updates the game "screen" and the goblin encounter chance.

  for i in range(4):
    if inventory[i] > 99 : inventory[i] = 99
  #Limits the stackable items to 99.

  if pyworld.percentChance(4) and bool(inventory[4]) and level == 0 and not position == -13:
    pyworld.wait(1.5)
    power_level = 0
    for i in range(10,13):
      if bool(inventory[i]):
        power_level += 1

    if power_level == 0: 
      loadout = pyworld.pickRandom(goblinPreset)
    if power_level == 1:
      loadout = pyworld.pickRandom(pyworld.pickRandom([goblinPreset, goblinDuoPresets1, goblinTrioPresets1]))
    if power_level == 2:
      loadout = pyworld.pickRandom(pyworld.pickRandom([goblinPreset, goblinDuoPresets2, goblinTrioPresets2]))
    if power_level == 3:
      loadout = pyworld.pickRandom(pyworld.pickRandom([goblinDuoPresets3, goblinTrioPresets3]))

    goblin_encounter("goblin.txt",1,loadout)
  #A random goblin encounter.

  if (position,level) == (5,-1) and not boolset[5]:
    goblin_encounter("goblin.txt",2,["Brute"])
    if bool(prev_battle_result):
      boolset[5] = True
    else:
      position,level = 4,0
  if (position,level) == (7,-1) and not boolset[6]:
    goblin_encounter("goblin.txt",3,["Bomber","Brute"])
    if bool(prev_battle_result):
      boolset[6] = True
    else:
      position,level = 4,0
  if (position,level) == (9,-1) and not boolset[7]:
    goblin_encounter("goblin.txt",4,["Archer","Brute","Thief"])
    if bool(prev_battle_result):
      boolset[7] = True
    else:
      position,level = 4,0
  if (position,level) == (-2,-1) and not boolset[2]:
    goblin_encounter("goblin.txt",5,["Guard","Guard"])
    if bool(prev_battle_result):
      boolset[2] = True
    else:
      position,level = -4,0
  #All scripted goblin encounters.

  if (position,level) == (-14,-1):
    pyworld.wait(0.7)
    pyworld.dialogue("boss.txt",1)
    pyworld.wait(5)
    pyworld.dialogue("boss.txt",2,1)
    pyworld.wait(7)
    spawn_boss("Sorcerer")
    battle_init()
    display_bossbattle()
    bossbattle_cycle()
  elif (position,level) == (16,-1):
    pyworld.wait(0.7)
    pyworld.dialogue("boss.txt",5)
    pyworld.wait(5)
    pyworld.dialogue("boss.txt",6,1)
    pyworld.wait(7)
    spawn_boss("Cannoneer")
    battle_init()
    display_bossbattle()
    bossbattle_cycle()
  elif (position,level) == (7,1):
    pyworld.wait(0.7)
    pyworld.dialogue("boss.txt",9,1)
    pyworld.wait(3)
    pyworld.dialogue("boss.txt",10)
    pyworld.wait(4)
    pyworld.dialogue("boss.txt",11)
    pyworld.wait(5)
    pyworld.dialogue("boss.txt",12)
    pyworld.wait(6)
    spawn_boss("Swordfighter")
    battle_init()
    display_bossbattle()
    bossbattle_cycle()
  elif (position,level) == (0,1):
    pyworld.wait(0.7)
    pyworld.dialogue("boss.txt",15,1)
    pyworld.wait(5)
    pyworld.dialogue("boss.txt",16,1)
    pyworld.wait(7)
    spawn_boss("King")
    battle_init()
    display_bossbattle()
    bossbattle_cycle()
  #A boss encounter.


  if position == -13:
    owlspot_cycle()
  elif (position,level) == (-11,-1):

    if entering:
      pyworld.dialogue("shortcutguy.txt",1,1)
      pyworld.wait(4)
      entering = False
      pyworld.clear()
    display_scene()
    shortcutspot_cycle()
  elif (position,level) == (-8,-1):

    if entering:
      power_level = 0
      for i in range(10,13):
        if bool(inventory[i]):
          power_level += 1

      if power_level == 0:pyworld.dialogue("shopkeeper.txt",1,1)
      if power_level == 1 or power_level == 2:pyworld.dialogue("shopkeeper.txt",2)
      if power_level == 3:pyworld.dialogue("shopkeeper.txt",3,1)
      pyworld.wait(4)
      entering = False
    shop_cycle()
  else:
    game_cycle()
  #The main game loops.


#---</Game-Operating Loop>---#
