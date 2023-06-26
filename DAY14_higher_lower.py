####        HIGHER_LOWER PROJECT         ####
print()
from import_function import higher_lower
from import_function import vs
from import_function import clear_screen
from import_function import higher_lower_list
import random

#choosing a celeb for random slot A
slot_a = random.choice(higher_lower_list)

#MAIN CODE
end = False
score = 0
ans_correct = 0
while not end:
    slot_b = random.choice(higher_lower_list)
    print_a = (f"Compare A : {slot_a['name']}, a {slot_a['description']}, from {slot_a['country']}.")
    print_b = (f"Against B : {slot_b['name']}, a {slot_b['description']}, from {slot_b['country']}.")
    
   #display
    clear_screen()
    print(higher_lower,end='\n')

    if ans_correct == 1: #to display score
        print(f"\nCORRECT ANSWER ! your score is {score}")

    print(print_a,end='')
    print(vs,end='\n')
    print(print_b,end='\n\n')

    follower_a = slot_a['follower_count']
    follower_b = slot_b['follower_count']

    #conditions
    answer = input("Who has more followers ? (A/B)").lower()
    while answer not in ['a','b']:
        answer = input("\nPlease input a valid answer\nWho has more followers ? (A/B)").lower()
    if answer=='a' and follower_a>follower_b:
        ans_correct = 1 
        score+=1
        slot_a,slot_b = slot_b,slot_a

    elif answer=='a' and follower_a<follower_b:
        print(f"\nWRONG ANSWER \nYour score is {score}")
        end=True

    elif answer=='b' and follower_a<follower_b:
        ans_correct = 1 
        score+=1
        slot_a,slot_b = slot_b,slot_a

    elif answer=='b' and follower_a>follower_b:
        print(f"\nWRONG ANSWER \nYour score is {score}")
        end=True
    
print()