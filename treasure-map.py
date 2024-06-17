print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

road_input = (input("You're at a intersection. Do you want to take a left or a right? ")).lower()
if(road_input == 'left'):
  river_input = (input("You find yourself a river. Proceed to swim or wait? ")).lower()
  if(river_input == 'wait'):
    door_input = (input("A dillema has struck upon you. There are three doorways: Red, Blue and Yellow. To which door shall you go through? ")).lower()
    if(door_input == 'blue'):
      print("Eaten by beasts. GAME OVER!!!💀")
    elif(door_input == 'yellow'):
      print("YOU WIN!!!!!!!!! The great treaure is yours.🤑🤑🤑🤑 ")
    elif(door_input == 'red'):
      print("Burned by fire. GAME OVER!!!💀")
    else:
      print("GAME OVER!!!💀")
  else:
    print("Attacked by a trout. GAME OVER!!!💀")
else:
  print("You fall into a hole. GAME OVER!!!💀")
  
