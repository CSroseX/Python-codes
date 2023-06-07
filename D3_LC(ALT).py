print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

lower_name1 = name1.lower()  #lower() function is used to lowercase , upercase letters.
lower_name2 = name2.lower()

combined_name = lower_name1+lower_name2

count_t = combined_name.count("t")    #count() function to count the frequency of a letter. 
count_r = combined_name.count("r")
count_u = combined_name.count("u")
count_e = combined_name.count("e")
count_l = combined_name.count("l")
count_o = combined_name.count("o")
count_v = combined_name.count("v")

digit_1 = count_t+count_r+count_u+count_e
digit_2 = count_l+count_o+count_v+count_e

digit_1 = str(digit_1)
digit_2 = str(digit_2)

number = digit_1+digit_2

print(number)