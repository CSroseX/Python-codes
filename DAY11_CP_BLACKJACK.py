###         BLACKJACK CAPSTONE PROJECT         ###
from import_function import blackjack_logo
from import_function import clear_screen
import time
import random
clear_screen()

print()
print(blackjack_logo)
print()

#card_list : last 3 10's are king,queen,jack and 11 is ace .//each one of these items are called cards
card_list = ['11','2','3','4','5','6','7','8','9','10','10','10','10']


#FUNCTION: to calculate user_score
user_score = 0
def calculate_user_score(user_first_card,user_second_card):
    return int(user_first_card)+int(user_second_card)
#FUNCTION: to calculate comp_score
def calculate_comp_score(comp_first_card,comp_second_card):
    return int(comp_first_card)+int(comp_second_card)


#choosing 2 random cards from card_list and assigning them both to user and comp
user_first_card = random.choice(card_list)
user_second_card = random.choice(card_list)
user_cards = [user_first_card,user_second_card]
print(user_cards) #
user_score = calculate_user_score(user_first_card,user_second_card)
print (user_score)



comp_first_card = random.choice(card_list)
comp_second_card = random.choice(card_list)
comp_cards = [comp_first_card,comp_second_card]
print(comp_cards) #
comp_score = calculate_comp_score(comp_first_card,comp_second_card)
print (comp_score)


#checking for BLACKJACK
if user_cards == ['10','11'] or user_cards == ['11','10']:
    print ("YOU WIN")
elif comp_cards == ['10','11'] or comp_cards == ['11','10']:
    print("YOU LOSE")


#if user_score is greater than 21 then convert ACE=11 into ACE=1
if user_score>21:
    if user_first_card=='11':
        user_first_card =='1'
    elif user_second_card=='11':
        user_second_card =='1'



condition_1 = True
#checking if user_score >21
while condition_1:
    if user_score >21:
        #does user has an ACE ?
        if (user_first_card == '11' or user_first_card == '1' ) or (user_second_card == '11' or user_second_card =='1' ):
            #if user's first card is 1 or 11 and still greater than 21, LOSE
            if (user_first_card =='1' or user_first_card=='11') and user_score >21 :
                print("YOU LOSE")
            elif (user_second_card =='1' or user_second_card=='11') and user_score >21 :
                print("YOU LOSE")
            else : #ask user if they want to draw a card .
                print("adding continues... ")
                condition_1 = False
                break
    else :
        print("do u want to draw a card ? ")
        #if yes, then add 1 card to user and repeat from line 47(while condition)
        condition_1 = False












print()