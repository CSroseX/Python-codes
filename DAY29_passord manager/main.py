from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    pass_letters = [random.choice(letters) for _ in range(nr_letters)]
    pass_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    pass_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = pass_letters+pass_numbers+pass_symbols
    random.shuffle(password_list)

    password = ''.join(password_list)
    pss_ENTRY.insert(0,password)

    pyperclip.copy(password)

    #find a way to show a label that says password copied for 5 seconds
    busted_display = Label(window, text="*Password copied !", font=("arial", "9"))
    busted_display.grid(column=0,row=5)
    window.after(2000, busted_display.destroy)
    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    
    global website_ENTRY,usr_ENTRY,pss_ENTRY
    website_data = website_ENTRY.get()
    usr_data = usr_ENTRY.get()
    pss_data = pss_ENTRY.get()


    if len(website_data)==0 or len(usr_data)==0 or len(pss_data)==0:
        messagebox.askokcancel(title='Field(s) empty',message='You have left one or more fields empty')
    
    else:
        is_ok = messagebox.askokcancel(title='Save?',message=f'Here are your details\n  Website: {website_data}\n  email/username: {usr_data}\n  password: {pss_data}\nWanna confirm save ?')
        if is_ok :
            #save to data.txt
            data_file = open('data.txt','a')
            data_file.write(f'{website_data} | {usr_data} | {pss_data} \n')
            data_file.close()

            #remove existing contents from the UI
            website_ENTRY.delete(0,'end')
            pss_ENTRY.delete(0,'end')

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50,pady=50)

canvas = Canvas(width=200,height=200,highlightthickness=0)
pss_img = PhotoImage(file='logo.png')
canvas.create_image(100,100,image=pss_img)
canvas.grid(column=1,row=0)

website_LABEL = Label(text='Website:')
website_LABEL.grid(column=0,row=1)

website_ENTRY = Entry(width=39)
website_ENTRY.focus()
website_ENTRY.grid(column=1,row=1,columnspan=2)

usr_LABEL = Label(text='Email/Username: ')
usr_LABEL.grid(column=0,row=2)

usr_ENTRY = Entry(width=39)
usr_ENTRY.insert(0,'@gmail.com')
usr_ENTRY.grid(column=1,row=2,columnspan=2)

pss_LABEL = Label(text='Password:')
pss_LABEL.grid(column=0,row=3)

pss_ENTRY = Entry(width=21)
pss_ENTRY.grid(column=1,row=3)

generate_BUTTON = Button(text='Generate Password',command=generate_password)
generate_BUTTON.grid(column=2,row=3)

add_BUTTON = Button(text='Add',width=36,command=save)
add_BUTTON.grid(column=1,row=4,columnspan=2)

window.mainloop()