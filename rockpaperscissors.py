import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcome to the ROCK, PAPER and SCISSORS game")
game_pic = [rock, paper, scissors]
user_num = int(input("Please choose a number: \n0-->ROCK \n1-->PAPER \n2-->SCISSORS\n"))
print(f"You chose: {game_pic[user_num]}\n")

comp_num = random.randint(0, 2)
print(f"The computer chose: {game_pic[comp_num]}")

if(user_num >= 3 or user_num < 0):
    print(f"You idiot{user_num} is not on the list!!! YOU LOST!!!!!!!!!")
elif(user_num == 0 and comp_num == 2):
    print("YOU WON!!!")
elif(comp_num == 0 and user_num == 2):
    print("YOU LOST!!!")
elif(user_num < comp_num):
    print("YOU LOST!!!")
elif(comp_num < user_num):
    print("YOU WON!!!")
else:
    print("IT'S A DRAW!!!")

