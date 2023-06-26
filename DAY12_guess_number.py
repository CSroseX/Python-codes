print()

import random
from import_function import number_one_to_hundred
from import_function import clear_screen

clear_screen()
#import logo/display art

print("WELCOME TO THE GUESSING GAME\n")
print("I'm thinking of a number between 1 and 100 (1 and 100 being included)")
number = random.choice(number_one_to_hundred)

choice = input("easy or hard ? : ").lower()
while choice not in ['easy','hard']:
    choice = input("Please provide a valid input \ntype 'easy' or 'hard' :").lower()
if choice == 'easy':
    attempts = 10
    print("You have 10 attempts.\n")
elif choice == 'hard':
    attempts = 5
    print("You have 5 attempts.\n")


def guess_try():
    global attempts
    while attempts!=0:
        try :
            guess = int(input("make a guess : "))
            if guess == number:
                print("RIGHT GUESS")
                break
            elif guess>number:
                print("You're high, go lower\n")
                print(f"You have {attempts -1} attempts left")
            elif guess<number:
                print("You're low, go higher\n")
                print(f"You have {attempts -1} attempts left")
        except ValueError:
            print("please provide a valid integer input")
            print(f"You have {attempts -1} attempts left")
        attempts-=1

guess_try()

print()