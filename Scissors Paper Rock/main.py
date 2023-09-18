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

print("Welcome to the simple game of Rock, Paper, Scissors!")
player_choice = int(input("Choose: 0 - Rock, 1 - Paper, or 2 - Scissors\n"))

player_list = [rock, paper, scissors]
cpu_list = [rock, paper, scissors]
map = [player_list, cpu_list]


random_cpu = random.choice(cpu_list)

print(f"You have chosen:\n {player_list[int(player_choice)]}\nComputer Chose:\n  {random_cpu}")

if player_list[int(player_choice)] == random_cpu:
	print("Draw.\n")
elif player_list[int(player_choice)] == paper and random_cpu == rock:
	print("You Won.")
elif player_list[int(player_choice)] == rock and random_cpu == scissors:   
	print("You Won.")
elif player_list[int(player_choice)] == scissors and random_cpu == paper:   
	print("You Won.")
else:
	print("Computer Wins. Try again...")