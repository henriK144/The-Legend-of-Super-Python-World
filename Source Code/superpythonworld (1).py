#A module containing functions for use in the game.
import os,sys,random,time

n = open("name.txt","r")
name = n.read()
n.close()

def clear():
  os.system('clear')
#Clears the console "screen", used for all image updates.

def wait(t):
  time.sleep(t)
#Waits t seconds.

def end_game():
  sys.exit()
#Ends the game.

def print_for_seconds(text,t):
  print(text)
  wait(t)
#Leaves text displayed for t seconds.

def percentChance(n):
  if n >= 100*random.random():
    return True
  else:
    return False
#Has an n% chance of returning True.

def pickRandom(container):
  return random.choice(container)
#Picks a random element from an ordered iterable.

def dialogue(file, line, formatname=0, twoformat=0, triformat=0, arg1=0, arg2=0, arg3=0):
  f = open(file)
  lines = f.readlines()

  if bool(formatname):
    
    print((lines[line - 1]).format(name))
  elif bool(twoformat):
    print((lines[line - 1]).format(arg1,arg2))
  elif bool(triformat):
    print((lines[line - 1]).format(arg1,arg2,arg3))
  else:
    print(lines[line - 1])

  f.close()
#Accesses a dialogue text file, and prints a line from it. The optional args are as follows: formatname=1 inserts the player's name into the curly brackets, twoformat=1 inserts arg1 and arg2 into the two curly bracket sets and triformat=1 inserts arg1, arg2, and arg3 into the three curly bracket sets.

def ask_until_valid(prompt, invalidMsg, validSet, integer=0):
  i = input(prompt)
  if bool(integer): i = int(i)

  if i in validSet:
    return i
  elif bool(integer):
    print_for_seconds(invalidMsg,1)
    ask_until_valid(prompt,invalidMsg,validSet,1)
  else:
    print_for_seconds(invalidMsg,1)
    ask_until_valid(prompt,invalidMsg,validSet)
#Repeatedly asks for input until the input is within a set/list of valid inputs. prompt is the message printed, invalidMsg is what is printed if you put in something invalid, and validSet is the set of allowed inputs. If integer=1, the input is taken to be an int.