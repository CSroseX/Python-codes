from tkinter import *

window = Tk()
window.title('Miles to Km converter')
window.minsize(width=290,height=190)
window.config(padx=30,pady=30)

miles_entry = Entry(width=10)
miles_entry.grid(column=1,row=0,padx=10,pady=10)

def calculate():
    miles = miles_entry.get()
    km = float(miles)*1.6
    L_answer.config(text=km)

L_miles = Label(text='Miles')
L_miles.grid(column=2,row=0)

L_isequalto = Label(text='is equal to ')
L_isequalto.grid(column=0,row=1)

L_answer = Label(text='  ')
L_answer.grid(column=1,row=1,padx=10,pady=10)

L_km = Label(text=' Km')
L_km.grid(column=2,row=1,padx=10,pady=10)

button_calculate = Button(text='Calculate',command=calculate)
button_calculate.grid(column=1,row=2)
button_calculate.config(background='grey')


window.mainloop()