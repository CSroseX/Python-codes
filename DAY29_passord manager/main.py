# Add a functionality such that when an already saved pss is present, ask the user if they want to overwrite it
# also make messagebox which shows all the list of websites saved 

from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

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
# ------------------------------- SEARCH ----------------------------------- #
def search():
    global website_ENTRY
    website_search = website_ENTRY.get()
    try:
        with open('data.json') as data_search:
            data = json.load(data_search)
    except FileNotFoundError:
        messagebox.showinfo(title='ERROR',message='No data file found !')
    else:
        if website_search in data:
            usr = data[website_search]['email']
            pss = data[website_search]['password']
            messagebox.showinfo(title=website_search, message=f'Email : {usr}\npassword : {pss}')
        else:
            messagebox.showinfo(title='Error',message=f'No details for {website_search} was found')
    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    
    global website_ENTRY,usr_ENTRY,pss_ENTRY
    website_data = website_ENTRY.get()
    usr_data = usr_ENTRY.get()
    pss_data = pss_ENTRY.get()
    new_data = {
        website_data :{
        'email' : usr_data,
        'password': pss_data,}
    }


    if len(website_data)==0 or len(usr_data)==0 or len(pss_data)==0:
        messagebox.askokcancel(title='Field(s) empty',message='You have left one or more fields empty')
    else:
        try:
            with open('data.json','r') as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open('data.json','w') as data_file:
                json.dump(new_data,data_file,indent=4)
        else:
            data.update(new_data)
            with open('data.json','w') as data_file:
                #Saving the updated data
                json.dump(data, data_file,indent=4)
        
        finally:
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

website_ENTRY = Entry(width=21)
website_ENTRY.focus()
website_ENTRY.grid(column=1,row=1)

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

search_BUTTON = Button(text='Search',command=search,width=15)
search_BUTTON.grid(column=2,row=1)

window.mainloop()
