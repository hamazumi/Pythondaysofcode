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

import random
option = [rock, paper, scissors]

x = input("Choose rock, paper, scissors. \n").lower()
num = random.randint(0, 2)

if x == "rock":
  print(rock)
  print("CPU chooses" + option[num])
  if num == 0:
    print("Draw")
  elif num == 1:
    print("CPU WINS")
  elif num == 2:
    print("YOU WIN!!!")
  else:
    print("error")  
elif x == "paper":
  print(paper)
  print("CPU chooses" + option[num])
  if num == 0:
    print("YOU WIN!!")
  elif num == 1:
    print("Draw")
  elif num == 2:
    print("YOU LOSE!!!")
  else:
    print("error")   
elif x == "scissors":
  print(scissors)
  print("CPU chooses" + option[num])
  if num == 0:
    print("YOU LOSE!!")
  elif num == 1:
    print("YOU WIN!!!")
  elif num == 2:
    print("DRAW!!!")
  else:
    print("error")   
else:
  print("not an option")