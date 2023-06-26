#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = '[name]'

with open('Input/Names/invited_names.txt') as invited_names:
    names = invited_names.readlines()

with open('Input/Letters/starting_letter.txt') as starting_letter:
    letter_content = starting_letter.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER,stripped_name)
        with open(f'Output/ReadyToSend/letter for {stripped_name}.txt',mode='w') as completed_letter:
            completed_letter.write(new_letter)