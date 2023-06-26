###         BLACKJACK CAPSTONE PROJECT         ###
#this project is extremely poorly built. make it shorter and 

from import_function import blackjack_logo
from import_function import clear_screen
from import_function import line_divider_1
import time
import random
clear_screen()

print()
print(blackjack_logo)
print()

#card_list : last 3 10's are king,queen,jack and 11 is ace .//each one of these items are called cards
#card_list = ['11','2','3','4','5','6','7','8','9','10','10','10','10']
card_list = [11,2,3,4,5,6,7,8,9,10,10,10,10]

#FUNCTION: adding one card to the user_card
def add_user_card():
    user_cards.append(random.choice(card_list))
#FUNCTION : adding one card to the comp_card
def add_comp_card():
    comp_cards.append(random.choice(card_list))


#FUNCTION: to calculate user_score
user_score = 0
def calculate_user_score():
    return sum(user_cards)
#FUNCTION: to calculate comp_score
comp_score = 0
def calculate_comp_score():
    return sum(comp_cards)


# STEP I : choosing 2 random cards from card_list and assigning them both to user and comp
user_first_card = random.choice(card_list)
user_second_card = random.choice(card_list)
user_cards = [user_first_card,user_second_card]

comp_first_card = random.choice(card_list)
comp_second_card = random.choice(card_list)
comp_cards = [comp_first_card,comp_second_card]


# STEP II a : check for BLACKJACK
def blackjack_check(user_cards,comp_cards):
    if user_cards == [10,11] or user_cards == [11,10]:
        print ("YOU GOTTA BLACKJACK . YOU WIN !!! ")
    elif comp_cards == [10,11] or comp_cards == [11,10]:
        print("YOU LOSE")




# print(user_cards) #
# user_score = calculate_user_score(user_first_card,user_second_card)
# print (user_score)

# print(comp_cards) #
# comp_score = calculate_comp_score(comp_first_card,comp_second_card)
# print (comp_score)


# STEP II b : if user_score is greater than 21 then convert ACE=11 into ACE=1
if user_score>21:
    if user_first_card== 11:
        user_first_card == 1
    elif user_second_card== 11:
        user_second_card == 1


# STEP III 
want_to_continue = True
while want_to_continue:

    user_score = calculate_user_score()
    print (f"Your cards are {user_cards} and current score : {user_score} ")
    print (f"computer's first card is {comp_first_card} ")

    #checking if user_score >21
    if user_score >21:
        #does user has an ACE ?
        if (user_first_card == '11' or user_first_card == '1' ) or (user_second_card == '11' or user_second_card =='1' ):
            #if user's first card is 1 or 11 and still greater than 21, LOSE
            if (user_first_card =='1' or user_first_card=='11') and user_score >21 :
                #then computer's turn
                want_to_continue = False
            #if user's second card is 1 or 11 and still greater than 21, LOSE
            elif (user_second_card =='1' or user_second_card=='11') and user_score >21 :
                #then computer's turn
                want_to_continue = False
        else:
            want_to_continue = False
    
    elif user_score == 21:
        print(f"YOUR SCORE {user_score} .")
        blackjack_check(user_cards,comp_cards)
        #then computer's turn 
        want_to_continue = False

    else :
        draw_card = input("\ndo u want to draw a card ? (y/n) : ").lower()
        print()
        #if yes, then add 1 card to user and repeat from line (while condition)
        if draw_card == 'y':
            add_user_card()
        elif draw_card == 'n':
            want_to_continue = False
            break

#FUNCTION: computer's turn
def computer_turn():
    comp_turn = True
    while comp_turn:
        comp_score = calculate_comp_score()
        if comp_score >16:
            comp_turn = False
        else:
            add_comp_card()

computer_turn()

#FUNCTION: displaying final hand
def final_hand():
    print(line_divider_1)
    user_score = calculate_user_score()
    comp_score = calculate_comp_score()
    print (f"\nYour final hand {user_cards} and your score is {user_score}")
    print (f"Computer's final hand {comp_cards} and score is {comp_score}")
final_hand()

#FUNCTION: result declaration 
def result():
    user_score = calculate_user_score()
    comp_score = calculate_comp_score()
    if user_score>21:
        print("\nYOU WENT OVER !!! YOU LOSE")
    elif (user_score<=21) and (comp_score>21):
        print("\nCOMP WENT OVER. YOU WIN !!!")
    elif user_score > comp_score:
        print("\nYOU WIN")
    elif comp_score>user_score:
        print("\nYOU LOSE")
result()



print()
