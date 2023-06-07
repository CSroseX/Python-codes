
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

count_t = count_r = count_u = count_e = count_l = count_o = count_v = 0

for i in name1:
    if i == 't' or i == 'T':
        count_t +=1
    if i == 'r' or i == 'R':
        count_r +=1
    if i == 'u' or i == 'U':
        count_u +=1
    if i == 'e' or i == 'E':
        count_e +=1
    if i == 'l' or i == 'L':
        count_l +=1
    if i == 'o' or i == 'O':
        count_o +=1
    if i == 'v' or i == 'V':
        count_v +=1

for i in name2:
    if i == 't' or i == 'T':
        count_t +=1
    if i == 'r' or i == 'R':
        count_r +=1
    if i == 'u' or i == 'U':
        count_u +=1
    if i == 'e' or i == 'E':
        count_e +=1
    if i == 'l' or i == 'L':
        count_l +=1
    if i == 'o' or i == 'O':
        count_o +=1
    if i == 'v' or i == 'V':
        count_v +=1

dig1 = count_t + count_r + count_u + count_e
dig2 = count_l + count_o + count_v + count_e

dig1 = str(dig1)
dig2 = str(dig2)

number = int(dig1+dig2)
if number<10 or number>90:
    print(f"Your score is {number}, you go together like coke and mentos.")
elif number>40 and number<50:
    print(f"Your score is {number}, you are alright together.")
if number>10 and number<40:
    print(f"Your score is {number}.")
if number>50 and number<90:
    print(f"Your score is {number}.")