#modifications that cn be added : add round system, where for example, 3 rounds and decide who won the whole match....

##                   STONE , PAPER, SCISSOR GAME PROJECT             ###

import time
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
---'   ____)________
          __________)
          __________)
         ___________)
---.______________)
'''

scissors = '''
    _______
---'   ____)_____
          _______)
       ____________)
      (____)
---.__(___)
'''
########################
print()
print("WELCOME TO ROCK,PAPER,SCISSORS GAME\n")

available_moves = ['rock', 'paper', 'scissor']
print()

choose_move = "Choose your move (type 'rock','paper' or 'scissor'): "
for i in choose_move.split():
    print(i,end = " ",flush =True)
    time.sleep(0.1)
move = input()

while move not in available_moves:
    print("Invalid move! Please choose again.")
    move = input("Choose your move: ")

if move == 'rock':
    chosen_1 = rock
elif move == 'paper':
    chosen_1 = paper
elif move == 'scissor':
    chosen_1 = scissors

random_move = random.choice(available_moves)
if random_move == 'rock':
    chosen_2 = rock
elif random_move == 'paper':
    chosen_2 = paper
elif random_move == 'scissor':
    chosen_2 = scissors

print()    

###  print moves
print("Your move:")
print(chosen_1)

time.sleep(0.5)

print("My move:")
print(chosen_2)

time.sleep(1)

###  results

if move == 'rock' and random_move == 'rock':
    print("DRAW")
elif move == 'rock' and random_move == 'scissor':
    print("U WIN")
elif move == 'rock' and random_move == 'paper':
    print("U LOSE")
elif move == 'scissor' and random_move == "rock":
    print("U LOSE")
elif move == 'scissor' and random_move == "scissor":
    print("DRAW")
elif move == 'scissor' and random_move == "paper":
    print("U WIN")
elif move == 'paper' and random_move == "rock":
    print("U WIN")
elif move == 'paper' and random_move == "scissor":
    print("U LOSE")
elif move == 'paper' and random_move == "paper":
    print("DRAW")

print()