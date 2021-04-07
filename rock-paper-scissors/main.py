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

game_images = [rock, paper, scissors]
choice = int(input("What do you choose ? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))


if choice >=3 or choice < 0:
  print("You typed invalid number. You lose!")
else:

  computer = random.randint(0,2)
  print(game_images[choice])
  print("Computer chose: \n")
  print(game_images[computer])
  
  if choice == 0 and computer == 2:
    print("You win!")
  elif choice == 2 and computer == 0:
    print("You lose!")
  elif computer > choice:
    print("You lose!")
  elif choice > computer:
    print("You win!")
  elif computer == choice:
    print("It's a draw")

  
