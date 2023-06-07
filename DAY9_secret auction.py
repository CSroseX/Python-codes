####        SECRET AUCTION PROJECT          ####

import time
from import_function import clear_screen

clear_screen()
#print ASCII logo
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
print()


#FUNCTION: making dictionaries and adding bidder details to it
auction_list = []
def add_bidder_details(arg_name,arg_bid):
    auction_list.append({
        'name' : arg_name,
        'bid' : arg_bid
    })


#asking bidder details
ask = True
while ask:
    name = input("\nWhat is your name : ")
    bid  = int(input("How much do you bid : $"))
    print()

    #if ask is other than yes/no
    ask = input ("Any other bidders ? : ").lower()
    while ask!='yes' and ask!='no':
        print("Invalid input. Please enter 'yes' or 'no'.")
        ask = input("Any other bidders? (yes/no): ").lower()
    
    if ask == 'yes':
        add_bidder_details(arg_name=name, arg_bid=bid)
        clear_screen()
    elif ask == 'no':
        print("Thank you.")
        print()
        ask = False

#now to compare the bids and its bidder to highest amount
highest_bid = 0
highest_bidder = ''
for dictionary in auction_list:
    temp_bid = dictionary['bid']
    if temp_bid > highest_bid:
        highest_bid = temp_bid
        highest_bidder = dictionary['name']



#print the winner
result_text = f"highest bidder is {highest_bidder}, with a bid of ${highest_bid} ."
for i in result_text.split():
    print(i,end=" ",flush=True)
    time.sleep(0.1)
print()    