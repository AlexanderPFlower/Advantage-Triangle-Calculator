import subprocess, random

def clear():
    subprocess.call('clear')

def mainLogic():
  clear()
  print("ADVANTAGE TRIANGLE CALCULATOR")
  print("X = you : Y = PC")
  print("0 1 2")
  print("G W F = Grass,    Water,  Fire   [Pokémon]")
  print("S A L = Sword,      Axe, Lance   [Fire Emblem]")
  print("R S P = Rock,  Scissors, Paper   [Paper, Scissors, Rock]\n")
  print("RESULT:")
  types = [0,1,2]
  x = random.choice(types)
  y = random.choice(types)
  print(x,y)
  if x == y:                                # Is it a tie / no advantage?
      print('No advantage/it\'s a tie!')
  elif x == y-2:                            # Is your opponent 2 while we are 0?
      print("Opponent has advantage/won!")
  elif x < y:                               # If they're not 2, are we 1 value less?
      print("You have advantage/won!")
  else:                                     # If no match, nobody is 2, and you're not 1 less, the opponent wins
      print("Opponent has advantage/won!")
  x = input("\nENTER. Replay  2. Quit\n> ")
  if x == '1':
      mainLogic()
  elif x == '2':
      quit()
  else:
      mainLogic() 

mainLogic()
