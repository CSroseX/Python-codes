###             CAESER CYPHER PROJECT           ###
#improvements : try making the code shorter by accessing user-defined functions from other files by means of importing. 

import time
print()

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print()
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
#if input is other than 'encode' or 'decode'
ans = True
while ans:
    if direction=='encode' or direction=='decode':
        ans = False
        break
    else:
        direction = input("Please input a valid answer .\n\nType 'encode' to encrypt or type 'decode' to decrypt : ")

text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#if user input shift more than 20
shift_check = True
while shift_check:
    if shift>26 :
        shift = shift%26
    else:
        break

#FUNCTION : repeat() . repeats the process of encryption/decryption based on 'yes' or 'no'
def repeat():
    print()
    repeat = input("Encrypt/Decrypt another message ?\nType 'yes' or 'no' : ").lower()
    print()
    if repeat == 'yes':
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        #if input is other than 'encode' or 'decode'
        ans = True
        while ans:
            if direction=='encode' or direction=='decode':
                ans = False
                break
            else:
                direction = input("Please input a valid answer .\n\nType 'encode' to encrypt or type 'decode' to decrypt : ")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        #if user input shift more than 20
        shift_check = True
        while shift_check:
            if shift>26 :
                shift = shift%26
            else:
                break
        #after asking all the paramenters, call caeser()
        caeser(text,shift,direction)
    else : 
        print("Thank You !\n")
    
            

#FUNCTION : caeser . encrypts / decrypts message based on direction
def caeser(text, shift, direction):     
    crypted_mssg = ''
    
    if direction=='decode':
        shift*= -1
    
    for char in text:
        if char in alphabet:
            index = alphabet.index(char)
            shifted_letter = alphabet[index+shift]
            crypted_mssg += shifted_letter
        else:
            crypted_mssg+=char
    result_text = f"The {direction}d text is {crypted_mssg}\n"
    #print result in a fancy way
    for i in result_text.split():
        print(i, end=" ",flush=True)
        time.sleep(0.1)
    print()
    repeat()

caeser(text,shift,direction)

print()