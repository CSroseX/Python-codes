from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
GREEN2 = '#8EAC50'
GREEN_DARK = '#1A5D1A'
YELLOW = "#FFE4A7"
ORANGE = '#FF8551'
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_fnc():
    window.after_cancel(timer)
    canvas.itemconfig(timer_countdown,text='00:00')
    timer_label.config(text='timer')
    tick.config(text='')
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_fnc():
    global reps 
    reps +=1
    


    if reps%8==0:
        timer_label.config(text='Long Break',fg=RED)
        count_down(LONG_BREAK_MIN)
    elif reps%2 == 0:
        timer_label.config(text='Short Break',fg=PINK)
        count_down(SHORT_BREAK_MIN)
    else :
        timer_label.config(text='WORK',fg=GREEN2)
        count_down(WORK_MIN*60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    
    count_min = math.floor(count/60)
    count_sec = count%60
    if count_sec == 0:
        count_sec = '00'
    elif count_sec <10:
        count_sec = f'0{count_sec}'

    canvas.itemconfig(timer_countdown, text=f'{count_min}:{count_sec}')
    
    if count>0:
        global timer
        timer = window.after(1000,count_down,count-1)
    else:
        start_fnc()
        marks = ''
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += '✔️'
        tick.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100,pady=50,background=YELLOW)


canvas = Canvas(width=200,height=224,background=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100,112,image=tomato_img)
timer_countdown = canvas.create_text(103,130,text='00:00',font=(FONT_NAME,35,'bold'),fill='white')
canvas.grid(column=1,row=1)



timer_label = Label(text='Timer')
timer_label.config(fg=GREEN2,background=YELLOW,font=(FONT_NAME,40,'bold'))
timer_label.grid(column=1,row=0)



start_button = Button(text='Start',command=start_fnc)
start_button.config(background=ORANGE)
start_button.grid(column=0,row=2)


reset_button = Button(text='Reset',command=reset_fnc)
reset_button.config(background=ORANGE)
reset_button.grid(column=2,row=2)

tick = Label(background=YELLOW,fg=GREEN_DARK)
tick.grid(column=1,row=3)

window.mainloop()