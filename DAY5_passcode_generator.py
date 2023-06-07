####           PASSWORD GENERATOR PROJECT          #####
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("\n           ...WELCOME TO PASSWORD GENERATOR...\n")

num_letters = int(input("How many letters would you like in your password?\n")) 
num_symbols = int(input(f"How many symbols would you like?\n"))
num_numbers = int(input(f"How many numbers would you like?\n"))
print()

#initializing variables
gen_letters =''
gen_symbols=''
gen_numbers=''

#series of for loops to generate LL , SS and NN seperately
for i in range (num_letters):                                       
    random_letter = random.choice(letters)
    gen_letters +=random_letter
for j in range (num_symbols):
    random_symbols = random.choice(symbols)
    gen_symbols +=random_symbols
for k in range (num_numbers):
    random_numbers = random.choice(numbers)
    gen_numbers +=random_numbers

#combining LL, SS and NN into a single string
ordered_characters = gen_letters+gen_symbols+gen_numbers
pass_list = list(ordered_characters)                                        

#shuffling ordered pass_list to unordered / random pass_list
random.shuffle(pass_list)   

#converting shuffled list to a string
password = ''.join(pass_list)
print(f"Your generated password is : {password}")