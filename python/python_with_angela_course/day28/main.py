from tkinter import *
from tkinter.font import BOLD
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global timer
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    title_label.config(text='Timer')
    check_mark.config(text='')
    global reps
    reps = 0



# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1

    if reps % 2 == 0 and reps != 8:
        title_label.config(text='Short Break!', fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)

    elif reps == 8:
        title_label.config(text='Long Break!', fg=RED)
        count_down(LONG_BREAK_MIN*60)

    else:
        title_label.config(text='Work Time!', fg=GREEN)
        count_down(WORK_MIN * 60)





# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60

    if count_sec <= 9:
        count_sec = f'0{count_sec}'

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        work_sessions = math.floor(reps/2)

        for x in range(work_sessions):
            mark = ''
            mark += '✓'
        check_mark.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro Program')
window.config(padx=100, pady=50, bg=YELLOW)


title_label = Label(text='Timer', fg=GREEN, bg=YELLOW, font=('Arial', 40, 'bold'))
title_label.grid(row=0, column=1)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, BOLD))
canvas.grid(row=1,column=1)



start_button = Button(text='Start', command=start_timer)
start_button.grid(row=2, column=0)


reset_button = Button(text='Reset', command=reset_timer)
reset_button.grid(row=2, column=2)


check_mark =  Label(text='', fg=GREEN, bg=YELLOW, font=('Arial', 10, 'bold'))
check_mark.grid(row=3, column=1)


window.mainloop()