#who's gonna pay the bill random generator ! 

import random

names = input ("Enter the names of the participants seperated by a comma : ")

name_list = names.split(",")
random_person = random.choice(name_list)


print(f"{random_person} will pay the bill ! ")
